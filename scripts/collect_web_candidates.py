from __future__ import annotations

import csv
import html
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("WEB_CANDIDATE_OUT", ROOT / "data" / "raw_web_candidates.csv"))
TERMS = ["AGENTS.md", "agents.md", "CLAUDE.md"]
UA = "Mozilla/5.0 AgentInstructionSourceCorpus/0.1"


@dataclass(frozen=True)
class Site:
    name: str
    sitemaps: tuple[str, ...]
    include_patterns: tuple[str, ...] = ()
    max_urls: int = 3000


SITES = [
    Site("AGENTS.md", ("https://agents.md/sitemap.xml",)),
    Site("OpenAI Developers", ("https://developers.openai.com/sitemap.xml",), (r"/codex",)),
    Site("OpenAI", ("https://openai.com/sitemap.xml",), (r"agent", r"codex")),
    Site("Anthropic Docs", ("https://docs.anthropic.com/sitemap.xml",), (r"claude-code",)),
    Site("Anthropic", ("https://www.anthropic.com/sitemap.xml",), (r"engineering", r"claude")),
    Site("Amp", ("https://ampcode.com/sitemap.xml",)),
    Site("Jules", ("https://jules.google/sitemap.xml", "https://jules.google/docs/sitemap.xml")),
    Site("Google AI", ("https://ai.google.dev/sitemap.xml",), (r"gemini-api", r"agent")),
    # Very large sitemaps are intentionally not crawled here. Their known URLs
    # are pulled from source_registry.csv and search-led manual expansion.
    Site("GitHub Docs", ("https://docs.github.com/sitemap.xml",), (r"/copilot/",), 1200),
    Site("GitHub Blog", ("https://github.blog/sitemap.xml",), (r"copilot", r"agent", r"ai-and-ml", r"changelog"), 1200),
    Site("VS Code", ("https://code.visualstudio.com/sitemap.xml",), (r"copilot", r"updates")),
    Site("Cursor", ("https://docs.cursor.com/sitemap.xml", "https://cursor.com/sitemap.xml"), (r"rules", r"agent", r"context", r"changelog")),
    Site("Factory Docs", ("https://docs.factory.ai/sitemap.xml",), (r"agent", r"agents-md", r"guideline", r"setup", r"readiness")),
    Site("Factory", ("https://factory.ai/sitemap.xml",), (r"agent", r"agents-md", r"news")),
    Site("Roo Code", ("https://docs.roocode.com/sitemap.xml",), (r"agent", r"agents", r"custom-instructions", r"rules", r"memory", r"update-notes")),
    Site("Kilo", ("https://kilo.ai/sitemap.xml", "https://kilocode.ai/sitemap.xml", "https://blog.kilo.ai/sitemap.xml"), (r"agent", r"agents", r"custom", r"memory", r"cli")),
    Site("opencode", ("https://opencode.ai/sitemap.xml",), (r"agent", r"agents", r"rules", r"config")),
    Site("Zed", ("https://zed.dev/sitemap.xml",), (r"/docs/ai", r"/releases", r"agent")),
    Site("Warp", ("https://docs.warp.dev/sitemap.xml",), (r"agent", r"agents", r"rules", r"migrate", r"coding")),
    Site("Windsurf", ("https://docs.windsurf.com/sitemap.xml",), (r"agent", r"agents", r"cascade", r"memory", r"rules", r"guidelines")),
    Site("Devin", ("https://docs.devin.ai/sitemap.xml",), (r"agent", r"agents", r"cascade", r"memory", r"rules", r"guidelines"), 900),
    Site("Augment Docs", ("https://docs.augmentcode.com/sitemap.xml",), (r"agent", r"agents", r"rules", r"guideline", r"context")),
    Site("Augment", ("https://www.augmentcode.com/sitemap.xml",), (r"blog", r"agent")),
    Site("Junie", ("https://junie.jetbrains.com/sitemap.xml",)),
    Site("JetBrains", ("https://www.jetbrains.com/sitemap.xml",), (r"junie", r"ai-assistant", r"agent"), 1200),
    Site("Ona", ("https://ona.com/sitemap.xml",), (r"/docs/", r"/templates/", r"/stories/", r"/guides/")),
    Site("Aider", ("https://aider.chat/sitemap.xml",), (r"/docs/", r"HISTORY")),
    Site("goose", ("https://block.github.io/goose/sitemap.xml",)),
    Site("Semgrep Docs", ("https://docs.semgrep.dev/sitemap.xml",)),
    Site("Semgrep", ("https://semgrep.dev/sitemap.xml",), (r"blog", r"guardian", r"agent")),
    Site("Hugging Face", ("https://huggingface.co/sitemap.xml",), (r"/docs/", r"/blog/", r"/changelog"), 1200),
    Site("OWASP", ("https://owasp.org/sitemap.xml",), (r"LLM", r"llm", r"genai", r"AI", r"ai"), 1000),
    Site("Meta Wearables", ("https://wearables.developer.meta.com/sitemap.xml", "https://developers.meta.com/sitemap.xml"), (r"agent", r"ai-assisted"), 1000),
    Site("UiPath", ("https://docs.uipath.com/sitemap.xml", "https://www.uipath.com/sitemap.xml"), (r"coding-agent", r"coded-agent", r"autopilot", r"agent"), 1000),
]


def fetch(url: str, timeout: int = 20) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None


def parse_sitemap(url: str, seen: set[str], budget: int = 5000) -> list[str]:
    if url in seen:
        return []
    seen.add(url)
    if budget <= 0:
        return []
    raw = fetch(url, timeout=12)
    if not raw:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    locs = [el.text.strip() for el in root.iter() if el.tag.endswith("loc") and el.text]
    urls: list[str] = []
    for loc in locs:
        if loc.endswith(".xml") or "sitemap" in urllib.parse.urlparse(loc).path.lower():
            if len(urls) < budget:
                urls.extend(parse_sitemap(loc, seen, budget - len(urls)))
        else:
            urls.append(loc)
        if len(urls) >= budget:
            break
    return urls


def passes_path_filter(url: str, patterns: tuple[str, ...]) -> bool:
    if not patterns:
        return True
    return any(re.search(pat, url, re.IGNORECASE) for pat in patterns)


def textify(raw: bytes) -> str:
    text = raw.decode("utf-8", errors="ignore")
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def check_url(site: str, url: str) -> dict | None:
    raw = fetch(url)
    if not raw:
        return None
    text = textify(raw)
    hits = [term for term in TERMS if term.lower() in text.lower() or term.lower() in url.lower()]
    if not hits:
        return None
    low = text.lower()
    positions = [low.find(term.lower()) for term in hits if low.find(term.lower()) >= 0]
    pos = min(positions) if positions else 0
    snippet = text[max(0, pos - 180) : pos + 420]
    title_match = re.search(r"<title[^>]*>(.*?)</title>", raw.decode("utf-8", errors="ignore"), re.I | re.S)
    title = html.unescape(re.sub(r"\s+", " ", title_match.group(1)).strip()) if title_match else ""
    return {
        "site": site,
        "url": url,
        "terms": ";".join(sorted(set(hits))),
        "title": title,
        "snippet": snippet,
    }


def load_registry_urls() -> list[tuple[str, str]]:
    registry = ROOT / "data" / "source_registry.csv"
    if not registry.exists():
        return []
    rows: list[tuple[str, str]] = []
    with registry.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            url = (row.get("url") or "").strip()
            site = (row.get("tool_or_site") or row.get("source_family") or "registry").strip()
            if url and "news.ycombinator.com" not in url:
                rows.append((site, url))
    return rows


def main() -> None:
    url_to_site: dict[str, str] = {}
    filter_text = os.environ.get("SITE_FILTER", "").strip().lower()
    selected_sites = [s for s in SITES if not filter_text or filter_text in s.name.lower()]
    for site in selected_sites:
        discovered: list[str] = []
        seen_sitemaps: set[str] = set()
        for sitemap in site.sitemaps:
            discovered.extend(parse_sitemap(sitemap, seen_sitemaps, budget=max(site.max_urls * 3, 1000)))
        filtered = [u for u in dict.fromkeys(discovered) if passes_path_filter(u, site.include_patterns)]
        for url in filtered[: site.max_urls]:
            url_to_site.setdefault(url, site.name)
        print(f"{site.name}: discovered={len(discovered)} filtered={len(filtered)} queued={min(len(filtered), site.max_urls)}", file=sys.stderr)

    if not filter_text:
        for site, url in load_registry_urls():
            url_to_site.setdefault(url, site)

    rows: list[dict] = []
    items = list(url_to_site.items())
    with ThreadPoolExecutor(max_workers=16) as ex:
        futures = {ex.submit(check_url, site, url): (site, url) for url, site in items}
        for i, fut in enumerate(as_completed(futures), 1):
            row = fut.result()
            if row:
                rows.append(row)
            if i % 500 == 0:
                print(f"checked={i}/{len(items)} hits={len(rows)}", file=sys.stderr)
            time.sleep(0.005)

    rows.sort(key=lambda r: (r["site"].lower(), r["url"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["site", "url", "terms", "title", "snippet"])
        writer.writeheader()
        writer.writerows(rows)
    print({"queued_urls": len(items), "matching_urls": len(rows), "output": str(OUT)})


if __name__ == "__main__":
    main()
