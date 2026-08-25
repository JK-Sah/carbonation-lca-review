# Systematic search — protocol and results

**Run:** 23 August 2026. **Database:** OpenAlex (REST API, `title_and_abstract.search`).
**Filters:** publication date >= 2000-01-01; type = article.
**Reproducibility:** `openalex_raw.json` holds every retrieved record with the query set that
produced it. `screening_log.csv` holds a decision and coded reason for all 713 records.

This replaces the search described in the submitted manuscript (WoS n=214, Scopus n=198,
Google Scholar n=148, hand-search n=23, total 583). Those counts came from records that could
not be substantiated and are not carried forward.

## Why OpenAlex

WoS and Scopus require institutional interactive sessions and do not permit automated export
under RIT's licence. OpenAlex indexes both corpora's underlying records, exposes a documented
API, and makes the search reproducible by a third party without a subscription — which matters
for a review whose contribution is transparency. A confirmatory WoS/Scopus search should be run
before submission and any additional records folded in; that is a limitation until done.

## Query set (8 queries)

| ID | Focus | Retrieved |
|---|---|---|
| Q1 | carbonation curing / CO2-cured x LCA-GWP-footprint | 136 |
| Q2 | CO2 / mineral carbonation x cement-concrete x LCA | 52 |
| Q3 | accelerated carbonation x concrete-block-precast x life-cycle | 128 |
| Q4 | CO2 injection / utilization x ready-mixed concrete x LCA | 10 |
| Q5 | CO2 utilization / CCU x concrete x climate-benefit / net-CO2 | 113 |
| Q6 | carbonated recycled concrete / blocks / paste x LCA | 148 |
| Q7 | CO2 sequestration / uptake x concrete x LCA | 266 |
| Q8 | carbon capture / flue gas x concrete-precast x LCA | 81 |

Verbatim query strings are in `openalex_raw.json` under `queries`.

**Total retrieved 934; unique after DOI/ID deduplication 713.**

## Known-item validation

Q1-Q4 alone retrieved only 3 of 6 studies already known to be eligible or relevant. The query
set was broadened (Q5-Q8) and re-validated. All 6 are now retrieved:

Ravikumar 2021 · Tanzer 2021 · Huang 2019 · Monkman & MacDonald 2017 · Skocek 2020 · Mao 2026

Recording this iteration is deliberate: the first query set would have missed half the known
literature, which is itself evidence for how inconsistently this field is indexed.

## Stage-1 screening (title/abstract)

Abstracts are present in the index for 437 of 713 records (61%). **A missing abstract is never
grounds for exclusion** — such records go to full text on the title alone. An earlier version
of this screen violated that rule and wrongly excluded Monkman & MacDonald 2017, which has no
indexed abstract and no LCA term in its title. The rule was corrected and the screen re-run.

| Outcome | n |
|---|---|
| To full text | **391** |
| Excluded | **322** |

Exclusion reasons: E8 no carbonation/CO2-utilisation intervention (221); E7 not a
cement/concrete product (68); E1 natural carbonation / durability focus (21); E4 no
quantitative environmental outcome (7); E2 geological CCS without concrete product (5).

## Full-text stage — status

391 records await full-text assessment. Within them, **128** carry explicit life-cycle
language together with a carbonation-curing or mineralisation intervention and form the
priority pool (`priority_fulltext.csv`); **208** have no indexed abstract and must be checked
directly.

Five studies have been read in full so far (`../sources/EXTRACTION_RECORDS.md`). Of those,
four are eligible and one (Skocek 2020) is excluded at full text as a CO2 balance rather than
an LCA — the paper states its headline figure "disregarding any indirect emissions".

**The full-text stage is not complete and no synthesis should be written until it is.**

## Growth of the field

The priority pool is heavily weighted to recent years: 2 records before 2016, 36 in 2026
alone, 93 of 128 from 2023 onward. Any review of this literature is reviewing a field that has
roughly tripled in output since the submitted manuscript's evidence base was assembled.
