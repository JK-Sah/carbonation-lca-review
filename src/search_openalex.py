"""Re-runs the eight OpenAlex queries and rebuilds the record set.

Writes search/openalex_records.json. No API key, no institutional access.
Reproduces the 934 retrieved / 713 unique counts of Section 4.1 and S1.
"""
import json
import os
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEARCH = os.path.join(ROOT, "search")

ENDPOINT = "https://api.openalex.org/works"
FILTERS = "from_publication_date:2000-01-01,type:article"
FIELDS = "id,doi,title,publication_year,primary_location,authorships,cited_by_count"
PAGE_SIZE = 200
RETRIES = 6


def _page(query, cursor):
    params = {
        "filter": f"title_and_abstract.search:{query},{FILTERS}",
        "per-page": str(PAGE_SIZE),
        "cursor": cursor,
        "select": FIELDS,
    }
    url = f"{ENDPOINT}?{urllib.parse.urlencode(params)}"
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                return json.load(response)
        except Exception:
            if attempt == RETRIES - 1:
                raise
            time.sleep(3 * (attempt + 1))


def fetch(query):
    hits, cursor = [], "*"
    while cursor:
        page = _page(query, cursor)
        results = page["results"]
        if not results:
            break
        hits.extend(results)
        cursor = page["meta"].get("next_cursor")
        time.sleep(2)
    return hits


def load_queries():
    path = os.path.join(SEARCH, "search_queries.json")
    with open(path) as fh:
        return json.load(fh)["primary_search"]["queries"]


def main():
    queries = load_queries()
    records, counts = {}, {}

    for name, query in queries.items():
        hits = fetch(query)
        counts[name] = len(hits)
        print(f"{name:28} {len(hits):>5}")
        for work in hits:
            key = (work.get("doi") or work["id"]).lower()
            records.setdefault(key, work)

    print(f"\ntotal retrieved {sum(counts.values())} | unique {len(records)}")

    payload = {
        "queries": queries,
        "counts_per_query": counts,
        "records": list(records.values()),
    }
    with open(os.path.join(SEARCH, "openalex_records.json"), "w") as fh:
        json.dump(payload, fh, indent=1)


if __name__ == "__main__":
    main()
