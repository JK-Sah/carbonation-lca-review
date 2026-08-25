# Confirmatory search — Web of Science Core Collection

**Run:** 24 August 2026, via RIT institutional access. **Interface:** Advanced Search, Topic field.

## Query

```
("carbonation curing" OR "CO2 curing" OR "carbonation-cured" OR "CO2-cured" OR
 "accelerated carbonation" OR "mineral carbonation" OR "CO2 mineralization" OR
 "CO2 mineralisation")
AND (concrete OR cement OR cementitious OR mortar OR masonry OR precast OR
     aggregate* OR binder*)
AND ("life cycle assessment" OR "life-cycle assessment" OR LCA OR
     "global warming potential" OR GWP OR "carbon footprint" OR "embodied carbon")
```

**Result: 379 records** in Web of Science Core Collection, against **713 unique records** from
the eight-query OpenAlex search. The OpenAlex set is larger because it also carried CCU,
CO2-uptake and carbon-capture term groups (Q5–Q8) that this single WoS query does not.

## Overlap test

The sixteen highest-relevance WoS records were checked against the OpenAlex record set by
normalised title match.

| | n |
|---|---|
| Already present in the OpenAlex set | **14** |
| Not retrieved by the OpenAlex search | **2** |

The two missed:

- *Environmental impacts of low-temperature CO2 sequestration* — to be assessed
- *Environmental benefit assessment of steel slag utilization and carbonation: a systematic
  review*, Sci. Total Environ. 806 (2022) — a review, and therefore **X5** regardless

**Interpretation.** The primary search recovers 14 of the 16 records Web of Science ranks most
relevant, and the single substantive miss is a review that the eligibility criteria exclude on
other grounds. This does not prove completeness, but it materially weakens the concern that a
single-database search systematically missed the eligible literature. The limitation in
Section 7.5 should be softened accordingly rather than removed: one confirmatory database is
not two, and Scopus remains outstanding.

## Unexpected secondary benefit — a screening priority order

Web of Science's relevance ranking identified records that are in the 713 but had not yet been
assessed at full text. These are now the highest-priority remaining candidates:

| Study | Journal / year |
|---|---|
| Carbonation curing of mortars produced with reactivated cementitious materials for CO2 sequestration | *J. Clean. Prod.* 383 (2023) |
| Modification of carbonation-cured cement mortar using biochar and its environmental evaluation | *Cem. Concr. Compos.* 134 (2022) |
| Environmental assessment of CO2 mineralisation for sustainable construction materials | *Int. J. Greenh. Gas Control* 93 (2020) |
| Green and durable engineered cementitious composites (GD-ECC) … and life-cycle analysis | *Constr. Build. Mater.* 414 (2024) |
| CO2 mineralization curing steel slag–fly ash–Portland cement ternary paste: … life cycle assessment | *J. Cent. South Univ.* 32(7) (2025) |
| Accelerated carbonation curing of cement mortars containing cement kiln dust: … carbon footprint reduction | *J. Clean. Prod.* 192 (2018) |
| CO2-curing of carbon-reducing slag-based masonry bricks at elevated … | — |

Each carries explicit life-cycle language together with a carbonation-curing intervention. The
relevance ranking of an independent database is a more reliable prioritisation signal than the
keyword heuristic used to build the internal priority pool, and these should be assessed before
the remaining lower-ranked records.

## Scopus — attempted, not available

The same query could not be run. Scopus was reached by three routes on 24 August 2026 — through
the RIT EZproxy stanza, through Scopus's own institutional access check (which correctly
identified Rochester Institute of Technology), and after a personal sign-in — and the platform
remained in **Scopus Preview** mode in every case, with the banner "You might be entitled to
access the full version of Scopus through your institution" and no subscribing institution
shown.

Stated accurately: **full Scopus access was not available through any institutional route
tested.** Whether the institution holds a licence at all should be confirmed with the library
before this is described in the manuscript; the observable fact is that access could not be
obtained.

This does not leave the search unconfirmed. It leaves it confirmed against one independent
database rather than two, which is what Section 7.5 should say.

## What Section 7.5 should now state

Not "the search draws on a single bibliographic database; a confirmatory search is
outstanding", but: the search was confirmed against Web of Science Core Collection, which
returned 379 records for an equivalent query and whose sixteen highest-relevance records were
already present in the retrieved set in fourteen cases, the exceptions being one record still
to assess and one systematic review excluded on other grounds. Scopus could not be accessed.
The search should still be treated as incomplete, but the specific worry that a single-database
strategy missed the eligible literature is not supported by the check that was possible.
