from __future__ import annotations

import csv
import html
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


API = "https://hn.algolia.com/api/v1/search"
TERMS = ["AGENTS.md", "CLAUDE.md"]
OUT = Path(__file__).resolve().parents[1] / "data" / "raw_hn_candidates.csv"


@dataclass(frozen=True)
class Window:
    lo: int
    hi: int


def fetch_json(params: dict[str, str | int]) -> dict:
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                import json

                return json.loads(resp.read().decode("utf-8"))
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("unreachable")


def count_hits(term: str, window: Window) -> int:
    data = fetch_json(
        {
            "query": term,
            "tags": "(story,comment)",
            "numericFilters": f"created_at_i>={window.lo},created_at_i<{window.hi}",
            "hitsPerPage": 1,
        }
    )
    return int(data.get("nbHits", 0))


def split_windows(term: str, window: Window) -> list[Window]:
    n = count_hits(term, window)
    if n <= 900 or window.hi - window.lo <= 86400:
        return [window]
    mid = (window.lo + window.hi) // 2
    return split_windows(term, Window(window.lo, mid)) + split_windows(term, Window(mid, window.hi))


def normalize_text(value: str | None) -> str:
    if not value:
        return ""
    return html.unescape(value).replace("\n", " ").replace("\r", " ").strip()


def has_exact_term(hit: dict, term: str) -> bool:
    haystack = " ".join(
        normalize_text(hit.get(k))
        for k in ["title", "story_title", "comment_text", "url"]
    ).lower()
    return term.lower() in haystack


def collect_term(term: str, window: Window) -> list[dict]:
    rows: dict[str, dict] = {}
    windows = split_windows(term, window)
    for w in windows:
        data = fetch_json(
            {
                "query": term,
                "tags": "(story,comment)",
                "numericFilters": f"created_at_i>={w.lo},created_at_i<{w.hi}",
                "hitsPerPage": 100,
                "page": 0,
            }
        )
        pages = min(int(data.get("nbPages", 0)), 10)
        for page in range(pages):
            if page == 0:
                page_data = data
            else:
                page_data = fetch_json(
                    {
                        "query": term,
                        "tags": "(story,comment)",
                        "numericFilters": f"created_at_i>={w.lo},created_at_i<{w.hi}",
                        "hitsPerPage": 100,
                        "page": page,
                    }
                )
            for hit in page_data.get("hits", []):
                if not has_exact_term(hit, term):
                    continue
                object_id = str(hit.get("objectID", ""))
                if not object_id:
                    continue
                item_id = hit.get("story_id") or hit.get("objectID")
                rows[object_id] = {
                    "term": term,
                    "object_id": object_id,
                    "item_id": item_id,
                    "kind": "comment" if hit.get("comment_text") else "story",
                    "created_at": hit.get("created_at", ""),
                    "title": normalize_text(hit.get("title") or hit.get("story_title")),
                    "url": hit.get("url") or f"https://news.ycombinator.com/item?id={item_id}",
                    "direct_hn_url": f"https://news.ycombinator.com/item?id={object_id}",
                    "thread_hn_url": f"https://news.ycombinator.com/item?id={item_id}",
                    "text_snippet": normalize_text(hit.get("comment_text"))[:300],
                }
        time.sleep(0.15)
    return list(rows.values())


def main() -> None:
    # HN launched in 2007; upper bound is 2026-07-06 23:59:59 Asia/Shanghai
    # converted approximately to Unix seconds.
    root = Window(1167609600, 1783353599)
    all_rows: dict[tuple[str, str], dict] = {}
    for term in TERMS:
        for row in collect_term(term, root):
            all_rows[(row["term"], row["object_id"])] = row
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "term",
                "object_id",
                "item_id",
                "kind",
                "created_at",
                "title",
                "url",
                "direct_hn_url",
                "thread_hn_url",
                "text_snippet",
            ],
        )
        writer.writeheader()
        writer.writerows(all_rows.values())

    unique_objects = len({row["object_id"] for row in all_rows.values()})
    unique_items = len({str(row["item_id"]) for row in all_rows.values()})
    by_term = {term: 0 for term in TERMS}
    for row in all_rows.values():
        by_term[row["term"]] += 1
    print({"rows": len(all_rows), "unique_objects": unique_objects, "unique_threads": unique_items, "by_term": by_term})


if __name__ == "__main__":
    main()
