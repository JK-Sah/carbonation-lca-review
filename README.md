# Carbonation-cured cement-based products — systematic review, net-benefit framework, and reporting set

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22089287.svg)](https://doi.org/10.5281/zenodo.22089287)

Data, search records and analysis code for:

> J.K. Sah, *When is carbonation-cured concrete actually cleaner? A systematic review, a
> net-benefit condition framework, and a proposed minimum reporting set for CO₂
> mineralization in cement-based products.* Submitted to *Journal of Cleaner Production*
> (JCLEPRO-D-26-25739).

---

## ⚠️ Relationship to the earlier repository and archive

This repository **replaces**
[`JK-Sah/carbonation-lca-meta-analysis`](https://github.com/JK-Sah/carbonation-lca-meta-analysis)
and its Zenodo archive [10.5281/zenodo.22061901](https://doi.org/10.5281/zenodo.22061901).

Those artifacts support an **earlier version** of the manuscript that pooled effect sizes
across studies in a quantitative meta-analysis. **The effect-size dataset in that release was
not verified against its cited sources and must not be used or cited.** A correction notice
to that effect is published on the Zenodo record, and the earlier repository is archived
read-only.

The work has since been rebuilt from a reproducible search. **No effect sizes are pooled.**
Every quantitative value released here is transcribed from a primary source in that source's
own units, against that source's own comparator, with the page, table or section in which it
appears recorded in [`extraction/extraction_records.md`](extraction/extraction_records.md).
Nothing from the earlier dataset is carried forward.

---

## What the review found

A PRISMA 2020 search (OpenAlex, 8 queries, 23 August 2026) returned 934 records, 713 unique.
Title-and-abstract screening excluded 322; 391 were sought for full text; 57 have been
assessed, of which **17** met criteria requiring a declared functional unit, a boundary of at
least cradle-to-gate, a stated non-carbonated comparator, and a locatable number.
Full-text assessment is **incomplete and reported as such** — 334 records remain, and a coded
decision is released for every one of the 713.

1. **The reported outcomes cannot be placed on a common axis.** The 17 studies use five
   functional-unit bases, 17 different comparators, and baselines spanning 280–540
   kg CO₂-eq/m³. Pooling them would be a category error, so none is performed.
2. **Magnitude tracks avoided Portland clinker, not mineralized CO₂.** Every reduction above
   10% in the set involves substituting or eliminating clinker; the only net-negative product
   contains no Portland cement at all.
3. **The isolated effect of carbonation spans both signs.** In comparisons holding composition
   constant, charging the energy of the carbonation step reverses the sign in some studies.

Of 25 papers reporting a quantified GWP reduction for a carbonation-treated cement product,
**8 do not declare both a functional unit and a system boundary** — the finding that motivates
the proposed Minimum Reporting Set.

## Contents

```
docs/
  index.html                 interactive net-benefit calculator (served via GitHub Pages)
search/
  search_queries.json        verbatim strings, all 8 primary queries + confirmatory search
  openalex_records.json      full record set returned by the search (713 unique)
  screening_log.csv          coded decision for every one of the 713 records
  fulltext_exclusions.csv    the 40 full-text exclusions with the criterion each failed
  fulltext_exclusions.md     the same, with the reasoning for each
  search_protocol.md         protocol, including known-item validation of the query set
  inclusion_criteria.md      criteria I1–I6 and exclusion codes X1–X8
  confirmatory_search.md     Web of Science cross-check (Scopus was not accessible)
extraction/
  extraction_table.csv       the 17 included studies as extracted
  extraction_records.md      per-study record: FU, boundary, comparator, baseline,
                             outcome, and the page/table/section of every value
src/
  search_openalex.py         re-executes the 8 queries; reproduces 934 / 713
  screen_records.py          automated screening pass (agrees with the log on 699/713)
  figure1_prisma.py          Figure 1 (PRISMA flow diagram)
  net_benefit_model.py       the net-benefit condition model; reproduces Table 4
  probabilistic_sensitivity.py   Monte Carlo (n=200,000) and Sobol indices
  sobol_robustness.py        re-tests the Sobol result under four prior specifications
```

## Interactive tool

An interactive implementation of the net-benefit condition model, in which the parameters can
be varied and the net benefit read against a chosen baseline, is served from `docs/`:

**https://jk-sah.github.io/carbonation-lca-review/**

It is a single self-contained HTML file with no external dependencies, and implements the same
model as `src/net_benefit_model.py`. It does not depend on any study-level dataset.

## Reproducing

Python 3.11, with `numpy`, `scipy` and `matplotlib`. The search needs network access but
**no API key and no institutional subscription**.

```bash
pip install numpy scipy matplotlib
```

The search and screening scripts resolve their own paths and can be run from anywhere. The
analysis scripts import `net_benefit_model`, so run them from `src/`:

```bash
python3 src/search_openalex.py          # → search/openalex_records.json  (934 → 713 unique)
python3 src/screen_records.py           # → search/screening_log_regenerated.csv (see note)
python3 src/figure1_prisma.py           # → Figure1_PRISMA_FlowDiagram.png/.tif

cd src
python3 net_benefit_model.py            # → Table 4 (r = 76.7 / 33.0 / 7.3; s* = 4.90 / 2.22 / 1.47)
python3 probabilistic_sensitivity.py    # → Tables 5–6; results/probabilistic_results.json
python3 sobol_robustness.py             # → Sobol indices under four prior specifications
```

OpenAlex is a moving index: re-running the search after 23 August 2026 will return more
records. `search/openalex_records.json` is the frozen set the manuscript reports.

**On `screen_records.py`.** Screening was single-rater and performed by the author;
`search/screening_log.csv` is the authoritative record of those decisions and is the source of
the 322 excluded / 391 sought counts in the manuscript. The script implements the automated
pass that supported that screen and is provided so the rules are inspectable — it is not the
screen itself. It agrees with the log on **699 of 713 records (98.0%)**. All 14 differences run
one way: literature reviews, bibliometric analyses and sectoral or geological CCS assessments
that the author excluded on reading the title, and that the regex rules pass through. Running
the script therefore reports 405 to full text against the log's 391. It writes to
`search/screening_log_regenerated.csv` and never overwrites the released log.

## Scope and limitations

Stated plainly, because they bound what these files support: the protocol was not
prospectively registered; screening was **single-rater**; the primary search draws on a
**single bibliographic database**, cross-checked against Web of Science (Scopus could not be
accessed through any available institutional route); and **full-text assessment is
incomplete**. Five records could not be retrieved and one is pending; all are listed in
`search/fulltext_exclusions.md` rather than silently dropped.

## Citation

Cite the manuscript for the findings and this archive for the data and code:

> Sah, J. K. (2026). *Carbonation-cured cement-based products: systematic review, net-benefit
> framework, and reporting set — data and code* (v2.0.0). Zenodo.
> https://doi.org/10.5281/zenodo.22089287

`10.5281/zenodo.22089287` is the concept DOI and always resolves to the latest version;
`10.5281/zenodo.22089288` is this specific release. If you use the released records, please
also cite OpenAlex as the source of the bibliographic data.

## License

MIT — see [LICENSE](LICENSE). Bibliographic metadata in `search/` derives from OpenAlex and is
CC0.
