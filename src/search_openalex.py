"""
Primary search — re-executes the eight OpenAlex queries and regenerates the record set.

Reproduces the 934 retrieved / 713 unique counts reported in manuscript Section 4.1 and
Supplementary S1. Requires no institutional subscription and no API key.

    python3 search_openalex.py            # writes search/openalex_records.json
"""
import json, os, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEARCH = os.path.join(ROOT, "search")

BASE = "https://api.openalex.org/works"
FILTERS = "from_publication_date:2000-01-01,type:article"

QUERIES = json.load(open(os.path.join(SEARCH, "search_queries.json")))["primary_search"]["queries"]


def fetch(q, tries=6):
    out, cursor = [], "*"
    while True:
        url = BASE + "?" + urllib.parse.urlencode({
            "filter": f"title_and_abstract.search:{q},{FILTERS}",
            "per-page": "200", "cursor": cursor,
            "select": "id,doi,title,publication_year,primary_location,authorships,cited_by_count"})
        for attempt in range(tries):
            try:
                with urllib.request.urlopen(url, timeout=60) as f:
                    page = json.load(f)
                break
            except Exception:
                if attempt == tries - 1:
                    raise
                time.sleep(3 * (attempt + 1))
        out += page["results"]
        cursor = page["meta"].get("next_cursor")
        if not cursor or not page["results"]:
            break
        time.sleep(2)
    return out


def main():
    records, counts = {}, {}
    for name, q in QUERIES.items():
        hits = fetch(q)
        counts[name] = len(hits)
        print(f"{name:28} {len(hits):>5}")
        for w in hits:
            records.setdefault((w.get("doi") or w["id"]).lower(), w)
    print(f"\ntotal retrieved {sum(counts.values())} | unique {len(records)}")
    json.dump({"queries": QUERIES, "counts_per_query": counts,
               "records": list(records.values())},
              open(os.path.join(SEARCH, "openalex_records.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
