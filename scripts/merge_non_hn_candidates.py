from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw_non_hn_candidates.csv"


def main() -> None:
    rows: dict[str, dict] = {}

    registry = ROOT / "data" / "source_registry.csv"
    if registry.exists():
        with registry.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                url = (row.get("url") or "").strip()
                if not url or "news.ycombinator.com" in url:
                    continue
                rows[url] = {
                    "url": url,
                    "site": row.get("tool_or_site", ""),
                    "collection_channel": "manual_seed",
                    "terms": row.get("term_hit", ""),
                    "title": row.get("title", ""),
                    "source_file": "source_registry.csv",
                }

    for path in (ROOT / "data").glob("raw_web_candidates_*.csv"):
        with path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                url = (row.get("url") or "").strip()
                if not url:
                    continue
                existing = rows.get(url)
                if existing:
                    existing["collection_channel"] = "manual_seed;sitemap_exact_term"
                    existing["terms"] = row.get("terms") or existing.get("terms", "")
                    existing["source_file"] = existing["source_file"] + ";" + path.name
                else:
                    rows[url] = {
                        "url": url,
                        "site": row.get("site", ""),
                        "collection_channel": "sitemap_exact_term",
                        "terms": row.get("terms", ""),
                        "title": row.get("title", ""),
                        "source_file": path.name,
                    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["url", "site", "collection_channel", "terms", "title", "source_file"],
        )
        writer.writeheader()
        writer.writerows(sorted(rows.values(), key=lambda r: r["url"]))

    print({"unique_non_hn_candidate_urls": len(rows), "output": str(OUT)})


if __name__ == "__main__":
    main()
