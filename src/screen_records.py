"""
Title-and-abstract screen — applies the coded eligibility rules and writes screening_log_regenerated.csv.

RELATIONSHIP TO THE RELEASED LOG. Run over the released record set this script reproduces
search/screening_log.csv exactly: the same decision and the same coded reason for all 713
records, giving 391 to full text and 322 excluded (E8 221, E7 68, E1 21, E4 7, E2 5), the
counts reported in manuscript Section 4.1 and Figure 1.

It reaches them two ways, and the distinction matters. 699 records are decided by the coded
rules in screen(). The remaining 14 are recorded rater decisions, listed individually in
MANUAL_DECISIONS above with the reason logged against each: screening was single-rater, and
those fourteen were excluded by the author on reading them rather than by any rule. They are
written out explicitly, not folded into the regular expressions, because no function of title
and abstract reproduces them -- see the note on MANUAL_DECISIONS. Anyone auditing the screen
can therefore see exactly which exclusions are mechanical and which are judgment.

KNOWN DISCREPANCY. One of the 17 included studies, Di Maria et al. 2020 (10.1016/j.ijggc.2019
.102882), is recorded in the log as excluded here under E7. It has no indexed abstract and its
title -- "Environmental assessment of CO2 mineralisation for sustainable construction
materials" -- carries no term the PRODUCT pattern matches, so the product criterion fires on
the title alone. This is the same failure mode as the Monkman and MacDonald case described
below: the study was recovered by hand-search and is included on its full text. Both cases are
disclosed in manuscript Section 3.4. The log is reproduced here as released; the discrepancy is
recorded rather than silently corrected, because correcting it would change the reported counts.

RULE THAT MATTERS: a missing abstract is never grounds for exclusion beyond the
product criterion. Records without an indexed abstract proceed to full-text assessment
on the title alone. An earlier version of this screen violated that rule and wrongly
excluded an eligible study (Monkman & MacDonald 2017) that has no indexed abstract and
no life-cycle term in its title.
"""
import csv, json, re
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEARCH = os.path.join(ROOT, "search")

INTERV = re.compile(r"carbonation curing|carbonation-cured|co2 curing|co2-cured|carbon dioxide curing|"
                    r"accelerated carbonation|forced carbonation|wet carbonation|co2 injection|"
                    r"carbon dioxide injection|co2 mineraliz|mineral carbonation|carbon mineraliz|"
                    r"co2 utiliz|carbon dioxide utiliz|co2 sequestrat|co2 uptake|"
                    r"carbonated (recycled|concrete|cement|aggregate|paste|fines)", re.I)
QUANT = re.compile(r"life ?cycle assessment|life-cycle assessment|\blca\b|global warming potential|\bgwp\b|"
                   r"carbon footprint|embodied carbon|co2 emission|carbon emission|emission reduction|"
                   r"net co2|climate benefit|kg co2|sustainab", re.I)
PRODUCT = re.compile(r"concrete|cement|cementitious|mortar|masonry|block|precast|paver|binder|clinker|aggregate", re.I)
DURABILITY = re.compile(r"durabilit|corrosion|carbonation depth|service life prediction|"
                        r"reinforcement corrosion|chloride", re.I)
GEOLOGICAL = re.compile(r"geological storage|saline aquifer|enhanced oil recovery|subsurface|"
                        r"flue gas desulfuriz", re.I)
LCA_STRICT = re.compile(r"life ?cycle assessment|life-cycle assessment|\blca\b|global warming potential|"
                        r"\bgwp\b|carbon footprint|embodied carbon", re.I)


# ---------------------------------------------------------------------------
# RECORDED RATER DECISIONS (not rules).
#
# Screening was single-rater. These fourteen records were excluded at title and
# abstract by the author on reading them, and the coded rules below do not derive
# those exclusions -- the rules would pass all fourteen through to full text.
# They are listed explicitly, with the reason recorded in the screening log and a
# note on what the record actually is, so that every departure from the automated
# pass is visible and auditable rather than hidden inside a regular expression.
#
# WHY THESE ARE NOT ENCODED AS RULES. There is no function of title and abstract
# that reproduces them. The log excludes "Accelerated carbonation curing as a CCUS
# strategy: a bibliometric and technical review" at this stage while sending
# "Review on carbonation curing of cement-based materials" to full text; a rule
# excluding reviews here would also exclude 45 records the log sends forward, and
# would change the screen rather than reproduce it. Reviews are, by design, mostly
# carried to full text and excluded there under X5.
#
# CAVEAT ON THE RECORDED REASONS. The codes below are transcribed verbatim from
# the screening log. For most of these records the code is a poor description of
# the ground actually taken -- nine are literature reviews or bibliometric
# analyses (X5), four are sectoral or geological CO2 storage assessments (X2/X4),
# and one is a materials study with no life-cycle accounting (X3). The verbatim
# codes are kept so that this script reproduces the released log exactly; the
# "basis" note records what the record is.
# ---------------------------------------------------------------------------
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
    """Return (decision, coded_reason) for one record."""
    text = f"{title} {abstract}"
    has_abstract = bool(abstract.strip())
    if not PRODUCT.search(text):
        return "exclude", "E7 not a cement/concrete product"
    if not INTERV.search(text) and has_abstract:
        return "exclude", "E8 no carbonation/CO2-utilisation intervention"
    if not has_abstract:
        return "full-text", "no abstract in index - cannot screen on title alone"
    if not QUANT.search(text):
        return "exclude", "E4 no quantitative environmental outcome"
    if DURABILITY.search(text) and not LCA_STRICT.search(text):
        return "exclude", "E1 natural carbonation / durability focus"
    if GEOLOGICAL.search(text) and not re.search(PRODUCT.pattern + r".{0,60}(cured|curing|mineraliz)", text, re.I):
        return "exclude", "E2 geological CCS without concrete product"
    return "full-text", "meets intervention + product + outcome criteria"


def inverted_to_text(inv):
    if not inv:
        return ""
    pos = {p: w for w, ps in inv.items() for p in ps}
    return " ".join(pos[k] for k in sorted(pos))


def main():
    data = json.load(open(os.path.join(SEARCH, "openalex_records.json")))
    rows = []
    for w in data["records"]:
        abstract = w.get("abstract") or inverted_to_text(w.get("abstract_inverted_index"))
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        decision, reason = screen(w.get("title") or "", abstract)
        source_of_decision = "rule"
        if doi in MANUAL_DECISIONS:
            # a recorded rater decision overrides the automated pass
            decision, reason = "exclude", MANUAL_DECISIONS[doi][0]
            source_of_decision = "rater"
        rows.append({"openalex_id": w["id"],
                     "doi": doi,
                     "year": w.get("publication_year"), "title": w.get("title"),
                     "source": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
                     "has_abstract": bool(abstract), "decision": decision, "reason": reason,
                     "decided_by": source_of_decision})
    with open(os.path.join(SEARCH, "screening_log_regenerated.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    n_ft = sum(r["decision"] == "full-text" for r in rows)
    n_rater = sum(r["decided_by"] == "rater" for r in rows)
    print(f"screened {len(rows)} | to full text {n_ft} | excluded {len(rows) - n_ft}")
    print(f"  {len(rows) - n_rater} decided by the coded rules, "
          f"{n_rater} by recorded rater decision (see MANUAL_DECISIONS)")


if __name__ == "__main__":
    main()
