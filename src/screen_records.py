"""
Title-and-abstract screen — applies the coded eligibility rules and writes screening_log_regenerated.csv.

RELATIONSHIP TO THE RELEASED LOG. search/screening_log.csv is the authoritative record of
the author's screening decisions (single-rater, as stated in the manuscript). This script
implements the automated pass that supported that screen; it is a reproduction aid, not the
screen itself. Run over the released record set it agrees with the log on 699 of 713 records
(98.0%). The 14 differences are all in one direction: records the author excluded on reading
the title -- literature reviews, bibliometric analyses, and sectoral or geological CCS
assessments -- that these regex rules pass through to full text. The script therefore reports
405 to full text where the log records 391. Cite the log, not this script's output, for the
counts in Section 4.1.

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
        decision, reason = screen(w.get("title") or "", abstract)
        rows.append({"openalex_id": w["id"],
                     "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                     "year": w.get("publication_year"), "title": w.get("title"),
                     "source": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
                     "has_abstract": bool(abstract), "decision": decision, "reason": reason})
    with open(os.path.join(SEARCH, "screening_log_regenerated.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    n_ft = sum(r["decision"] == "full-text" for r in rows)
    print(f"screened {len(rows)} | to full text {n_ft} | excluded {len(rows) - n_ft}")


if __name__ == "__main__":
    main()
