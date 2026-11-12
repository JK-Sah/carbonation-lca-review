"""Title-and-abstract screen. Writes search/screening_log_regenerated.csv.

Over the released record set this reproduces search/screening_log.csv exactly:
same decision and same coded reason for all 713 records, 391 to full text and
322 excluded (E8 221, E7 68, E1 21, E4 7, E2 5).

It gets there two ways. 699 records are decided by the rules in screen(); the
other 14 are rater decisions listed in MANUAL_DECISIONS. Screening was
single-rater and those fourteen were excluded on reading, not by rule, so they
are written out rather than folded into the patterns -- no function of title and
abstract reproduces them. The log excludes one bibliometric review of carbonation
curing at this stage while sending another review of the same subject to full
text; a rule excluding reviews here would also exclude 45 records the log carries
forward. The decided_by column marks which is which.

A missing abstract is never grounds for exclusion beyond the product criterion;
such records go to full text on the title alone. Two included studies trip that
criterion anyway and were recovered by hand-search -- Monkman & MacDonald 2017
and Di Maria et al. 2020 -- both disclosed in Section 3.4. The log is reproduced
as released rather than corrected, since correcting it would move the counts.
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEARCH = os.path.join(ROOT, "search")

INTERVENTION = re.compile(
    r"carbonation curing|carbonation-cured|co2 curing|co2-cured"
    r"|carbon dioxide curing|accelerated carbonation|forced carbonation"
    r"|wet carbonation|co2 injection|carbon dioxide injection|co2 mineraliz"
    r"|mineral carbonation|carbon mineraliz|co2 utiliz|carbon dioxide utiliz"
    r"|co2 sequestrat|co2 uptake"
    r"|carbonated (recycled|concrete|cement|aggregate|paste|fines)", re.I)

OUTCOME = re.compile(
    r"life ?cycle assessment|life-cycle assessment|\blca\b"
    r"|global warming potential|\bgwp\b|carbon footprint|embodied carbon"
    r"|co2 emission|carbon emission|emission reduction|net co2"
    r"|climate benefit|kg co2|sustainab", re.I)

PRODUCT = re.compile(
    r"concrete|cement|cementitious|mortar|masonry|block|precast|paver"
    r"|binder|clinker|aggregate", re.I)

DURABILITY = re.compile(
    r"durabilit|corrosion|carbonation depth|service life prediction"
    r"|reinforcement corrosion|chloride", re.I)

GEOLOGICAL = re.compile(
    r"geological storage|saline aquifer|enhanced oil recovery|subsurface"
    r"|flue gas desulfuriz", re.I)

LCA_TERM = re.compile(
    r"life ?cycle assessment|life-cycle assessment|\blca\b"
    r"|global warming potential|\bgwp\b|carbon footprint|embodied carbon", re.I)

CURED_PRODUCT = re.compile(PRODUCT.pattern + r".{0,60}(cured|curing|mineraliz)", re.I)


MANUAL_DECISIONS = {
    # DOI: (logged reason, basis)
    "10.1016/j.jcou.2022.102015": (
        "E2 geological CCS without concrete product",
        "sectoral CCUS chains for the cement industry; storage in a saline aquifer"),
    "10.12789/geocanj.2024.51.212": (
        "E2 geological CCS without concrete product",
        "regional review of carbon capture and storage in southern Ontario"),
    "10.21608/auej.2025.388454.1848": (
        "E1 natural carbonation / durability focus",
        "review of geopolymer products for LEED certification"),
    "10.1021/acs.est.5c03561.s001": (
        "E1 natural carbonation / durability focus",
        "bibliometric analysis of mineral carbonation research"),
    "10.1016/j.cscm.2025.e05265": (
        "E1 natural carbonation / durability focus",
        "review of CO2 utilization in cement and concrete"),
    "10.69739/sjet.v2i1.669": (
        "E1 natural carbonation / durability focus",
        "narrative review of ultra-low-carbon concrete pathways and policy"),
    "10.1016/j.ccst.2025.100558": (
        "E1 natural carbonation / durability focus",
        "review synthesising CO2 sequestration pathways in concrete"),
    "10.30574/wjaets.2025.16.1.1205": (
        "E2 geological CCS without concrete product",
        "review of carbon capture in the cement industry at sector scale"),
    "10.3390/pr13082648": (
        "E2 geological CCS without concrete product",
        "geological CO2 sequestration in a deep saline formation"),
    "10.3390/buildings16142710": (
        "E1 natural carbonation / durability focus",
        "bibliometric review of carbon-emissions research on recycled concrete"),
    "10.1016/j.mtsust.2026.101375": (
        "E1 natural carbonation / durability focus",
        "materials study: strength, freeze-thaw durability and uptake; no life-cycle accounting"),
    "10.1016/j.ccst.2026.100570": (
        "E1 natural carbonation / durability focus",
        "materials study: CO2 binding in mortars; no life-cycle accounting"),
    "10.12363/issn.1001-1986.25.07.0535": (
        "E2 geological CCS without concrete product",
        "source-sink matching for geologic CO2 sequestration at provincial scale"),
    "10.9734/jerr/2026/v28i21802": (
        "E1 natural carbonation / durability focus",
        "review of solid-waste valorization in cementitious binders"),
}

def screen(title, abstract):
    text = f"{title} {abstract}"
    has_abstract = bool(abstract.strip())

    if not PRODUCT.search(text):
        return "exclude", "E7 not a cement/concrete product"
    if not INTERVENTION.search(text) and has_abstract:
        return "exclude", "E8 no carbonation/CO2-utilisation intervention"
    if not has_abstract:
        return "full-text", "no abstract in index - cannot screen on title alone"
    if not OUTCOME.search(text):
        return "exclude", "E4 no quantitative environmental outcome"
    if DURABILITY.search(text) and not LCA_TERM.search(text):
        return "exclude", "E1 natural carbonation / durability focus"
    if GEOLOGICAL.search(text) and not CURED_PRODUCT.search(text):
        return "exclude", "E2 geological CCS without concrete product"

    return "full-text", "meets intervention + product + outcome criteria"


def flatten_abstract(inverted):
    if not inverted:
        return ""
    position = {p: word for word, spots in inverted.items() for p in spots}
    return " ".join(position[k] for k in sorted(position))


def row_for(work):
    abstract = work.get("abstract") or flatten_abstract(
        work.get("abstract_inverted_index"))
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    decision, reason = screen(work.get("title") or "", abstract)
    decided_by = "rule"

    if doi in MANUAL_DECISIONS:
        decision = "exclude"
        reason = MANUAL_DECISIONS[doi][0]
        decided_by = "rater"

    location = (work.get("primary_location") or {}).get("source") or {}
    return {
        "openalex_id": work["id"],
        "doi": doi,
        "year": work.get("publication_year"),
        "title": work.get("title"),
        "source": location.get("display_name", ""),
        "has_abstract": bool(abstract),
        "decision": decision,
        "reason": reason,
        "decided_by": decided_by,
    }


def main():
    with open(os.path.join(SEARCH, "openalex_records.json")) as fh:
        records = json.load(fh)["records"]

    rows = [row_for(w) for w in records]

    out = os.path.join(SEARCH, "screening_log_regenerated.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    to_full_text = sum(r["decision"] == "full-text" for r in rows)
    by_rater = sum(r["decided_by"] == "rater" for r in rows)
    print(f"screened {len(rows)} | to full text {to_full_text} "
          f"| excluded {len(rows) - to_full_text}")
    print(f"  {len(rows) - by_rater} decided by the coded rules, "
          f"{by_rater} by recorded rater decision (see MANUAL_DECISIONS)")


if __name__ == "__main__":
    main()
