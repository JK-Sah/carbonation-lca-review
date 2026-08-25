# Extraction records — from actual full text

One block per study. Every value here was read from the paper's own text, with the location
recorded. Values are transcribed as the paper states them, in the paper's own units and
against the paper's own comparator. No conversion, normalisation, or imputation happens in
this file — that belongs downstream and must be shown separately.

Full text held in `sources/fulltext/`.

Status legend: EXTRACTED = read from full text | ABSTRACT-ONLY = not yet full text |
PENDING = not yet obtained

---

## Ravikumar et al. 2021 — Nat. Commun. 12:855

- **Status:** EXTRACTED (open access, Europe PMC PMC7870952)
- **DOI:** 10.1038/s41467-021-21148-w
- **Full citation:** D. Ravikumar, D. Zhang, G. Keoleian, S. Miller, V. Sick, V. Li, Carbon
  dioxide utilization in concrete curing or mixing might not produce a net climate benefit,
  Nat. Commun. 12 (2021) 855.
- **Local full text:** `sources/fulltext/Ravikumar2021_NatCommun_PMC7870952.txt`

**Functional unit** (Methods, "Functional Unit"): "concrete with 1 MPa compressive strength
and 1 m3 of volume and Ep kWh of electricity". Strength-normalised, and it carries an
electricity term for the capture energy penalty. It is *not* a plain 1 m3.

**Comparator** (Methods): conventional (non-CCU) concrete produced from the same source
dataset. Not "Standard CMU".

**What the paper actually reports.** Not a percentage GWP reduction. The outcome is the
"net CO2 benefit" — TOT(conventional) minus TOT(CCU) — computed stochastically over 10,000
Monte Carlo runs *per dataset*, for 99 datasets from 19 publications. Results are reported
as counts of datasets by sign of benefit:

| quantity | value | location |
|---|---|---|
| datasets with negative net CO2 benefit, coal-plant capture, baseline | 56 of 99 | Results, Figs 3–5 |
| datasets with negative net benefit, range across SE/MA/EA allocation | 56 to 63 of 99 | Results, Fig 6 |
| datasets with negative net benefit, NGCC capture (SE/MA/EA) | 61, 65, 68 of 99 | SI Section 10 |
| headline range across CO2 source and allocation | **negative in 56–68 of 99** | Abstract; Results |
| datasets with *positive* net benefit | 36 (EA) to 43 (SE) of 99 | Results, Fig 6 |
| datasets negative when CO2 captured at a cement plant | 44 of 99 | SI Section 11, Supp. Fig. S4 |

Worked single-dataset example (dataset 1, Results): CCU concrete OPC 24.8 kg/MPa vs
conventional 22.6 kg/MPa; at 0.948 kg CO2/kg OPC (Supp. Table 2) that is 23.5 vs
21.4 kg CO2/MPa, a difference of 2.1 kg CO2/MPa against 1.1 kg CO2/MPa of CO2 utilised.
Likelihood of positive net benefit for dataset 1: **0%**.

**Absolute baseline GWP:** not reported as a single figure. Baseline emissions are built
per-dataset from inventory; the OPC intensity used is 0.948 kg CO2/kg OPC (Supp. Table 2).

**Uncertainty:** Monte Carlo distributions per dataset (10,000 runs); reported as likelihood
of positive benefit, not as a CI on a percentage.

**Cradle-to-gate LCA of a carbonation-cured product?** Cradle-to-gate CO2 assessment, yes —
13 processes, ecoinvent factors. But it is a *reanalysis across 99 literature datasets*, not
a single-product LCA.

> **Against the manuscript.** Table 2 / S6 record **6.5% reduction, 95% CI [3.5, 9.5]**,
> functional unit 1 m3, comparator "Standard CMU", region USA. The paper contains no 6.5%
> and no such interval, uses a strength-normalised FU with an electricity term, and its
> central result runs the other way. Nothing in Table 2's row for this study is recoverable
> from the paper.
>
> **Eligibility:** questionable as a single meta-analysis data point. One effect size cannot
> represent 99 datasets whose signs disagree. If used at all it is a *source of datasets*,
> not a study-level observation — and 19 of its underlying publications may themselves be
> candidates for screening.

---

## Skocek et al. 2020 — Sci. Rep. 10:5614

- **Status:** EXTRACTED (open access, Europe PMC PMC7101415)
- **DOI:** 10.1038/s41598-020-62503-z
- **Full citation:** J. Skocek, M. Zajac, M. Ben Haha, Carbon capture and utilization by
  mineralization of cement pastes derived from recycled concrete, Sci. Rep. 10 (2020) 5614.
- **Local full text:** `sources/fulltext/Skocek2020_SciRep_PMC7101415.txt`

**Functional unit:** none declared. Quantities are per 100 g of clinker replaced / per 100 g
of paste. This is a materials-chemistry study, not an LCA with a declared FU.

**Comparator:** clinker replacement by limestone — i.e. the savings from carbonated fines are
compared against the savings from a *different SCM strategy*, not against an OPC baseline.

| quantity | value | location |
|---|---|---|
| CO2 bound by carbonated paste | 42 g CO2 / 100 g initial cement | "Re-carbonated paste as cement constituent" |
| equivalently | 28 g CO2 / 100 g carbonated paste | same |
| clinker emission factor used | 86.5 g CO2 / 100 g clinker (ref. 51) | same |
| **overall CO2 saving** | **114.5 g CO2 per 100 g clinker replaced** | same; repeated in Conclusions |
| relative to limestone replacement | "more than 30% higher" | Abstract; Conclusions |

Explicit scope caveat in the same sentence as the headline number: the 114.5 g figure is
stated **"disregarding any indirect emissions"**.

**Uncertainty:** none reported. No interval, no range, no sensitivity analysis on the saving.

**Cradle-to-gate LCA?** **No.** A stoichiometric/TG-based CO2 balance that explicitly excludes
indirect emissions. There is no life-cycle inventory, no system boundary, no impact assessment.

> **Against the manuscript.** Table 2 / S6 record **37.0% reduction vs an OPC baseline,
> CI [17, 57]**, functional unit 1 kg. The paper reports no percentage GWP reduction, no
> interval, and no OPC comparator. The ">30%" in the abstract is a *ratio between two SCM
> strategies' savings*, not a GWP reduction.
>
> **Eligibility: fails.** The manuscript's stated inclusion criterion is a cradle-to-gate LCA
> of a carbonation-cured cement product. This is not one, by the authors' own framing.

---

---

## Huang et al. 2019 — J. Clean. Prod. 241:118359   **INCLUDE (I1-I6 met)**

- **Status:** EXTRACTED from full text (accepted manuscript, 37 pp, CC BY-NC-ND)
- **DOI:** 10.1016/j.jclepro.2019.118359
- **Full citation:** H. Huang, T. Wang, B. Kolosz, J. Andresen, S. Garcia, M. Fang,
  M.M. Maroto-Valer, Life-cycle assessment of emerging CO2 mineral carbonation-cured concrete
  blocks, J. Clean. Prod. 241 (2019) 118359.
- **Local full text:** `sources/fulltext/Huang2019_JCLP.txt` (PDF alongside it)
- **Full title (the manuscript cites a truncated form):** "Life-cycle assessment of emerging
  CO2 mineral carbonation-cured concrete blocks: **Comparative analysis of CO2 reduction
  potential and optimization of environmental impacts**"

| field | value | location |
|---|---|---|
| functional unit | 1 m3 non-hollow concrete block with MC curing | Sec 2.2 |
| baseline / comparator | conventional **steam-cured**, non-MC OPC block | Abstract; Conclusions |
| **absolute baseline GWP** | **419 kg CO2-eq/m3** | Abstract; Conclusions; Fig. (OPC-Steam bar) |
| **GWP of CO2-cured blocks** | **292-454 kg CO2-eq/m3** (a range, stated twice) | Abstract; Conclusions |
| headline claim | "Up to 30 % of CO2 emission avoidance could be achieved when replacing steam curing by MC curing **and adjusting the binder types**" | Abstract |

**Effect implied by the paper's own numbers.** The product range straddles the baseline:

- best case (292 vs 419): **+30.3% reduction** — consistent with the "up to 30%" claim
- worst case (454 vs 419): **-8.4%, i.e. an increase in emissions**

So the paper's own span is roughly **-8.4% to +30.3%**. Note also that the 30% is conditional on
*changing the binder as well as the curing*, so it is not attributable to carbonation alone.

> **Against the manuscript.** This is a real cradle-to-gate LCA of a carbonation-cured product
> and does meet the inclusion criterion. But the citation and the number both differ from what
> is recorded:
>
> - Cited as "H. Huang, **R. Guo**, T. Wang, et al. ... J. Clean. Prod. **238** (2019) **117823**".
>   R. Guo is not an author; the volume and article number are wrong.
> - Table 2 records **15.0%, CI [0.0, 30.0]**. The paper reports "up to 30%" — a ceiling, not a
>   central estimate. The recorded 15.0 is the midpoint of [0, 30], i.e. constructed from the
>   ceiling rather than extracted from a reported effect size.
> - S6 records baseline "Portland cement"; the paper's comparator is **steam-cured** OPC blocks.
> - S6 records region "China"; the group is Heriot-Watt (UK) with a Zhejiang co-author.
>
> **First real absolute baseline recovered: 419 kg CO2-eq/m3.** This is one of the twelve values
> Reviewer 2 asked for at comment 2.1.
>
> **Slot resolvable.** The citation can be fully corrected (authors, title, volume, article
> number, DOI). The effect size cannot be carried over: there is no single reported percentage,
> and the honest summary is a range spanning zero.

---

## Pan et al. 2017 — Sci. Rep. 7:17227  (proposed for slot [37])

- **Status:** ABSTRACT VERIFIED (open access, PMC5722910) — not a match for the slot
- **DOI:** 10.1038/s41598-017-17648-9
- **Authors:** S.-Y. Pan, T.-C. Chung, C.-C. Ho, C.-J. Hou, Y.-H. Chen, P.-C. Chiang
  (not "Pan, Chen, Dong" as cited).
- **What it reports:** flue-gas CO2 mineralized with electric-arc-furnace slag, the carbonated
  slag then used as an SCM in blended cement mortar. Headline quantity is a **global** CO2
  reduction potential of **~138 million t/yr** from iron and steel slags.
- **No product-level GWP reduction against an OPC baseline is reported.**

> **Against the manuscript.** Slot [37] records Pan et al. **2022**, "Industrial demonstration
> of CO2 mineral curing", *J. CO2 Util.* 56:101818, post-cast low-Ca, **Belgium**, **41.0%
> [31.0, 51.0]**. This paper is 2017, *Sci. Rep.*, Taiwan, steel slag, and reports no such
> quantity. It is not the cited paper and cannot supply the recorded effect size.

---

## Monkman & MacDonald 2017 — J. Clean. Prod. 167:365-375   **INCLUDE (I1-I6 met)**

- **Status:** EXTRACTED from full text (ScienceDirect via RIT EZproxy)
- **DOI:** 10.1016/j.jclepro.2017.08.194
- **Full citation:** S. Monkman, M. MacDonald, On carbon dioxide utilization as a means to
  improve the sustainability of ready-mixed concrete, J. Clean. Prod. 167 (2017) 365-375.
- **Local full text:** `sources/fulltext/Monkman2017_JCLP_sciencedirect.txt`

| field | value | location |
|---|---|---|
| functional unit | 1 m3 of concrete | Table 6 title; Sec 4.2 |
| baseline / comparator | reference control mix, same producer | Sec 3, Table 1-2 |
| binder loading reduction | **5-8%** (Conclusions say 7-8%) | Highlights; Abstract; Conclusions |
| **carbon footprint reduction** | **4.6%** | Abstract; Conclusions ("a generic case suggests that a 4.6% reduction in the carbon footprint is feasible") |
| cement emission factor used | 915 kg CO2/t cement (supplier-communicated) | Sec 3 |
| model-case plant year | 24 t CO2 used; ~897 t CO2 absorbed and avoided | Abstract |

Table 6 reports the plant-year model case, not a per-m3 baseline: CO2 absorbed -289.1 kg,
avoided cement emissions -17,584.8 kg, total produced 64.7 kg, net reduction -17,932.7 kg.

> **Against the manuscript.** Table 2 records **7.5%, CI [5.0, 10.0]**, FU 1 m3.
>
> - The paper's reported carbon-footprint reduction is **4.6%** — **below the lower bound of
>   the recorded interval**. The recorded CI excludes the value the paper actually reports.
> - The 5-8% figure in the recorded interval is the **binder loading** reduction, a different
>   quantity. Cement removal and carbon-footprint reduction have been conflated.
> - The citation is also wrong: cited as vol. **125** (2016) 232-240; actual vol. **167**
>   (2017) 365-375.
>
> **Slot resolvable.** Citation fully correctable, and unusually the effect size is too —
> a single, clearly reported **4.6%** against a 1 m3 functional unit.

---

## Tanzer et al. 2021 — Faraday Discuss. 230:271-291   **INCLUDE (I1-I6 met)**

- **Status:** EXTRACTED from full text (RSC via RIT EZproxy)
- **DOI:** 10.1039/d0fd00139b
- **Local full text:** `sources/fulltext/Tanzer2021_FaradayDiscuss_rsc.txt`
- **Real title:** "Curing time: a temporally explicit life cycle **CO2 accounting of
  mineralization, bioenergy, and CCS** in the concrete sector"
  (the manuscript cites "...life cycle assessment of mineralization in the concrete sector")

**Scope.** Temporally explicit life-cycle CO2 accounting for 30 MPa OPC concrete, combining
bioenergy + CCS at the kiln with accelerated carbonation of fresh concrete and natural
carbonation of demolition waste. Accelerated carbonation is one lever among several, not the
subject of the whole study.

**Functional unit:** 1 m3 of 30 MPa ordinary Portland concrete.

**Benchmark net CO2: 280 kg CO2/m3** (life cycle net, after natural-carbonation credits;
production and upstream emissions are 380 kg CO2/m3 before those credits).

**Table 3 — effect of accelerated carbonation, as change from the benchmark case:**

| scenario | change in net CO2 | implied effect vs 280 kg/m3 |
|---|---|---|
| 0.3% CO2 injection, 5% strength gain | **-9 kg/m3** | **+3.2% reduction** |
| 10% CO2 curing, no strength gain | **+42 kg/m3** | **-15.0% — an increase** |
| 10% CO2 curing, 10% strength gain | **+19 kg/m3** | **-6.8% — an increase** |

The paper states it directly: "The injection of 0.3% CO2 during concrete mixing was the only
case that resulted in a decrease". And in the abstract: "accelerated carbonation was, by
itself, an inefficient CO2 storage mechanism, due to the penalty of energy use and injection
losses."

> **Against the manuscript.** Table 2 records **8.0%, CI [2.0, 14.0]**, FU 1 t, CO2 source
> "Biogenic", region Netherlands.
>
> - The paper's only reduction scenario gives **3.2%**, near the bottom of the recorded
>   interval. Its other two accelerated-carbonation scenarios are **net increases**.
> - Nothing in the paper supports a central estimate of 8.0% or an upper bound of 14.0%.
> - The functional unit is **1 m3**, not 1 t.
> - The title in the reference list is not the paper's title.
>
> **Eligibility: doubtful.** The study's subject is BECCS-plus-carbonation system accounting,
> not a cradle-to-gate LCA of a carbonation-cured product. Accelerated carbonation appears as
> a sensitivity lever, and by itself it is reported as counterproductive.

---

## Mao et al. 2026 — J. Clean. Prod. 556:148215   **INCLUDE (I1-I6 met)**

- **Status:** EXTRACTED from full text (ScienceDirect via RIT)
- **DOI:** 10.1016/j.jclepro.2026.148215
- **Full citation:** Y. Mao, X. Wang, S. Drissi, W. Chen, S. Guo, X. Hu, C. Shi, Life cycle
  assessment of carbonated recycled concrete fine products, J. Clean. Prod. 556 (2026) 148215.
- Identified by Reviewer 2 (comments 2.12 and 2.17) and retrieved independently by the
  23 Aug 2026 search.

| field | value | location |
|---|---|---|
| functional unit | **1 t of concrete blocks** | Sec 2.1 |
| system boundary | cradle-to-gate: raw material production + transport, block preparation + transport | Sec 2.1, Fig. 1 |
| comparator | A-Ref: cast block, 100% Portland cement binder, autoclave cured | Table 1 |
| **absolute baseline GWP** | **200.97 kg CO2/t** | Sec 3.1, Fig. 3 |

**Results (Sec 3.1, Fig. 3), all kg CO2/t block:**

| scenario | total CO2 | vs A-Ref |
|---|---|---|
| A-Ref (reference, cast, autoclave) | 200.97 | baseline |
| A-Wet RCF (30% wet-carbonated RCF) | 145.35 | **-27.7%** |
| A-Dry RCF (30% dry-carbonated RCF) | 141.37 | **-29.7%** |
| B-Ref-Steam (compacted reference) | 201.96 | +0.5% |
| B-Ref-CO2 (compacted reference, CO2 cured) | 159.50 | **-20.6%** |
| B-RCF-CO2 (**100% RCF**, CO2 cured) | **-1.51** | **-100.75%, net-negative** |

Abstract range: CO2 emissions -27.68% to -100.75%; energy -19.61% to -67.38%; cost -8.95% to
-30.47%.

**Three findings that bear directly on the net-benefit framework.**

1. **The benefit tracks clinker elimination.** Cement carries an emission factor of
   167.2 kg CO2/t and contributes 83-87% of total emissions (Sec 3.1). The only net-negative
   case is the one containing **no cement at all** (100% RCF). Partial replacement at 30%
   yields ~28-30%; full replacement yields net-negative. This is the A term dominating.

2. **The net-negative result is conditional on a near-zero CO2 supply chain.** The paper is
   explicit: net-negativity arises "mainly resulting from the use of on-site exhaust gas,
   which did not involve additional emissions associated with CO2 capture, purification, or
   transport" (Sec 3.1). That is s ~ 0 in the framework's terms.

3. **With commercially supplied CO2 the economics and energy invert, and the paper quantifies
   it.** Energy consumption rises almost linearly with carbonation degree under commercial CO2,
   steepest for B-RCF-CO2; and "the cost associated with the CO2 curing stage in B-RCF-CO2
   **exceeded the total production cost of B-Ref-Steam**" (Sec 4.1). Subtle and worth
   reporting precisely: the CO2 *source* has a **negligible** effect on net CO2 at the
   carbonation stage — the balance is governed by uptake — but a **large** effect on energy
   and cost. A framework that treats s as purely a GWP term would miss this.

4. **Extreme sensitivity of the net-negative case.** A 5% change in the CO2-curing stage moves
   B-RCF-CO2's total CO2 by **118.53%** (Table 8) — the net-negative result sits on a knife
   edge, because it is a small difference between large opposing flows.

> **Value to this review.** A 2026 cradle-to-gate LCA with a declared functional unit, a stated
> comparator, six scenarios, absolute values for every arm, and an explicit CO2-source
> sensitivity. It is the strongest single piece of evidence retrieved so far, and it
> independently supports the mechanism the net-benefit condition describes.

---

## Wang et al. 2024 — J. Clean. Prod. 470:143553   **EXCLUDE — X6**

- **DOI:** 10.1016/j.jclepro.2024.143553
- "Assessing Carbon Capture and Carbonation in Recycled Concrete Aggregates: A Holistic Life
  Cycle Assessment Perspective with Simulation at Industrial Scale"
- Cradle-to-gate, functional unit **per tonne of carbonated RCA output**. Reports a **net
  carbon abatement of 21.42 kg CO2 eq**; NGCC flue gas captured by aqueous ammonia, then
  mineralised onto RCA.

> **Excluded under X6 — no non-carbonated comparator.** The study quantifies the net abatement
> of a capture-and-mineralisation *process*; it does not report the GWP of an uncarbonated RCA
> arm, so no relative effect against a conventional product can be formed. The only
> carbonated-vs-conventional comparisons in the text are citations to other studies.
> Borderline against I3/I5 as a process rather than product assessment; recorded here so the
> decision is auditable and can be contested.

---

## Shang et al. 2023 — Constr. Build. Mater. 404:133207   **INCLUDE (I1-I6 met)**

- **Status:** EXTRACTED from full text (ScienceDirect via RIT)
- **DOI:** 10.1016/j.conbuildmat.2023.133207
- **Full citation:** Shang, Chen, Qi, Chang, Yang, Qu, Comparative life cycle environmental
  assessment of recycled aggregates concrete blocks using accelerated carbonation curing and
  traditional methods, Constr. Build. Mater. 404 (2023) 133207.

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of recycled aggregate concrete block (RACB)** | Sec 2.2 (a dedicated "Functional unit" section) |
| system boundary | "cradle to the door" (cradle-to-gate) | Abstract; Sec 2 |
| comparator | standard (traditional) curing | Abstract |
| **absolute baseline GWP** | **539.5 kg CO2-eq/m3** (standard curing) | Results |

| curing scenario | GWP | vs standard curing |
|---|---|---|
| standard curing (baseline) | 539.5 kg CO2-eq/m3 | — |
| pressurized carbonation curing | ~359.8 kg CO2-eq/m3 | **-33.3%** |
| wet carbonation curing | **254.7 kg CO2-eq/m3** | **-52.8%** |

CO2 absorption: -73.0 kg CO2-eq (pressurized) and -99.3 kg CO2-eq (wet).

> ### This paper corrects something I reported earlier
>
> Reference **[38]** in the manuscript cites "P. Shen, H. Zheng, S. Liu, Y. Sun, Comparative
> life-cycle assessment of recycled concrete aggregate blocks with accelerated carbonation,
> Constr. Build. Mater. **409** (2023) **133884**" and records **52.8%**, FU 1 m3.
>
> I previously reported that [38] resolved to "different authors entirely" and treated the
> value as unsupported. The authors and the volume/article number are indeed wrong. **But the
> effect size is not invented — 52.8% is exactly what this real paper reports** for wet
> carbonation curing against standard curing, at the same functional unit of 1 m3.
>
> So [38] is a **garbled citation to a real paper whose headline number was transcribed
> correctly**, not a fabricated data point. That is a materially different finding from the
> others and I was wrong to group it with them.
>
> What remains wrong in that row: the author list, volume and article number; the 95% CI
> [46.8, 58.8] is still a constructed +/-6 with no basis in the paper; and the S6 metadata
> records the CO2 source as "DAC" and the binder as "Slag/FA", neither of which matches a
> wet-carbonation-cured recycled aggregate block.

---

## Merino-Lechuga et al. 2025 — Constr. Build. Mater. 142286   **EXCLUDE — I2**

- **DOI:** 10.1016/j.conbuildmat.2025.142286 (open access)
- "Technical and environmental assessment of CO2-cured alkali-activated pervious paving blocks
  incorporating recycled aggregates"
- Functional unit **1 m3 of pervious paving blocks**, SimaPro 9.6.0.1, ecoinvent v3.10,
  EN 15804+A2. Headline: "Alkali-activated blocks with reduced CO2 emissions by **49 %** vs.
  Portland cement blocks."

> **Excluded under I2 — the boundary is gate-to-gate, not cradle-to-gate.** The paper states it
> "followed a 'gate-to-gate' approach, considering only the stages of the alkali-activated
> pervious paving blocks, excluding transportation, use, maintenance, and end-of-life phases",
> and that the fly ash and mine tailings inputs "were considered burden-free in terms of
> production".
>
> **A second MRS exhibit.** A highlight bullet reads "reduced CO2 emissions by 49 % vs.
> Portland cement blocks" with no indication that the binder inputs carry zero production
> burden. A practitioner reading the highlight has no way to know. MRS field 2 —
> system boundary — is exactly what makes this visible.

---

## Also screened and excluded (J. CO2 Util. / Constr. Build. Mater., 2023-2026)

| Study | DOI | Reason |
|---|---|---|
| Julcour et al. 2025, CO2 mineralization of bottom ash and decarbonation of waste-to-energy plants, J. CO2 Util. | 10.1016/j.jcou.2025.103169 | **X3** — feedstock characterisation and CO2-uptake kinetics; no functional unit, no life-cycle boundary |
| Rawat et al. 2024, Corrosion resistance and LCA of lightweight geopolymer concrete, Constr. Build. Mater. | 10.1016/j.conbuildmat.2024.138370 | No carbonation-curing intervention — carbonation appears as a durability attribute of a geopolymer |
| Carbon dioxide sequestration in cementitious materials: a review, J. CO2 Util. 2024 | 10.1016/j.jcou.2024.102812 | **X5** — review |
| Carbon sequestration and storage in concrete: state-of-the-art review, J. CO2 Util. 2023 | 10.1016/j.jcou.2023.102443 | **X5** — review |

---

## Fu et al. 2024 — Commun. Mater. 5:109 — "Storing CO2 while strengthening concrete by carbonating its cement in suspension"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1038/s43246-024-00546-9 (open access)
- **Local full text:** `sources/fulltext/10.1038_s43246-024-00546-9.txt`

| field | value | location |
|---|---|---|
| functional unit | **1 tonne of cement** | Carbon footprint section |
| system boundary | **cradle-to-gate** | same |
| comparator | classical cement manufacturing | same |
| **absolute baseline GWP** | **519 kg CO2-eq/t** (311.4 fuel + 207.6 calcination) | same |
| carbonated cement | **500.3 kg CO2-eq/t** | same |
| **effect** | **-18.7 kg CO2-eq/t = -3.6%** | same |

The paper also states that "the proportion of carbonated cement for a functional unit is set
at 1/4", i.e. the 3.6% corresponds to carbonating one quarter of the cement.

> **Why this study matters to the argument.** The title promises storing CO2 *and* strengthening
> concrete, and the paper scales its result to "82.28 million tons of CO2" globally. The
> cradle-to-gate figure for the product itself is **3.6%**. Both statements are in the same
> paragraph. This is the clearest single illustration of why a review must read the LCA rather
> than the framing — and of why the MRS asks for the functional unit and the absolute baseline
> next to any percentage.

---

## Sapata et al. 2026 — Front. Built Environ. 12:1888433   **INCLUDE (I1-I6 met)**

- **DOI:** 10.3389/fbuil.2026.1888433 (open access)
- **Local full text:** `sources/fulltext/10.3389_fbuil.2026.1888433.txt`
- Carbonated fine and coarse recycled concrete aggregates in 3D printable concrete.

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of 3D printable concrete** | LCA section |
| system boundary | cradle-to-gate (raw material production + mixing) | same |
| design | **7 mixtures**: 1 reference with natural aggregate, 3 with non-carbonated RCA, 3 with carbonated RCA (CRCA) | same |
| **absolute baseline GWP** | **REF = 485.88 kg CO2-eq/m3** | Table 4 |
| non-carbonated RCA mixes | 472.77 - 439.44 kg CO2-eq/m3 | Table 4 |
| carbonated RCA mixes | 477.52 - 442.21 kg CO2-eq/m3 | Table 4 |

**This is the most informative design retrieved so far, because it isolates carbonation from
aggregate substitution.**

1. The reductions relative to REF "are attributed to the replacement of NA with RCA" — the
   aggregate swap, not the carbonation.
2. At matched composition the **carbonated mixes are marginally worse than the non-carbonated
   ones** (477.52 vs 472.77 at the top of each range).
3. Decisively: including the carbonation electricity burden **"reversed the environmental
   outcome of the CRCA mix"**. Net GWP **increased by 3.1%, 6.3% and 11.3%** for the three
   CRCA mixes relative to their own baselines. The implied electricity burdens — **22.75,
   45.48 and 85.51 kg CO2-eq/m3** — were "larger than the combined benefits from avoided
   burdens and CO2 uptake".

> **Direct support for the net-benefit condition.** The sign of the effect is set by process
> energy, not by uptake. This is the s term dominating U*eta, measured rather than modelled,
> and it is exactly the mechanism Reviewer 2 pointed to at comment 2.12.

---

## Pending verification

**Sci. Rep. 2025, 10.1038/s41598-025-31481-5** — CO2 mineralization applied to concrete poles.
Reports CO2 emissions falling from **36.353 to 30.353 kg per pole** (-16.5%) with 6.0 kg CO2
mineralised, using Ecoinvent 3.0 and defined system boundaries. Functional unit is stated per
concrete pole. Comparator wording needs confirming before inclusion.

---

## Results in Engineering 2026 — "Development of CO2 Mineralised concrete for carbon sequestration: thermogravimetric analysis and life cycle assessment"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.rineng.2026.110120
- Read in full via ScienceDirect (RIT).

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of concrete at 30 MPa, 28 d** | Sec 2, LCA methodology |
| system boundary | cradle-to-gate (extraction, processing, transport to batching plant, mixing); use and end-of-life excluded | same |
| intervention | **dry ice (solid CO2) added during mixing** at 5, 10, 15% by cement mass | Sec 2, Table 2 |
| comparator | **DI-0, an otherwise identical mix with no dry ice** | Table 2 |
| **absolute baseline GWP** | **345.8 kg CO2-eq/m3** | Table 7 |

**Table 7 — total embodied carbon:**

| mix | kg CO2-eq/m3 | absolute reduction | relative reduction | 28-d strength |
|---|---|---|---|---|
| DI-0 (control) | **345.8** | — | — | 32.8 MPa |
| DI-5 | 338.7 | 7.1 | **2.1%** | 36.5 MPa |
| DI-10 | 334.5 | 11.3 | **3.3%** | 39.8 MPa |
| DI-15 | ~332.6 | 13.2 | **3.8%** | — |

CO2 uptake: 28.9, 32.8, 39.4, 46.3 kg CO2/m3 across the series; net additional sequestration
attributable to the dry ice is **3.9 to 17.4 kg CO2/m3**, which the paper describes as about a
**5.9% offset of cement emissions** (~297 kg CO2/m3). Cement is ~86% of total embodied carbon
across all four mixes.

> **Why this study matters.** It is a clean matched comparison — same mix design, only the
> carbonation input varies — and the answer is **2.1 to 3.8%**. Table 8 reports the
> corresponding cost increases: **15.6%, 30.8% and 45.9%**. A 3.8% carbon reduction for a 46%
> cost increase is the sharpest cost-per-tonne statement in the retrieved set.
>
> **One reporting observation worth recording.** Table 6 assigns dry ice a production emission
> factor of **-3.195 kg CO2-eq/kg** — a negative factor crediting the captured CO2 as avoided
> emissions. That allocation choice is disclosed, which is exactly what the MRS asks for, but a
> reader who did not open Table 6 would not know the result depends on it.

---

## Developments in the Built Environment 2026 — "Low-carbon ternary binder bio-composites via accelerated carbonation for circular construction"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.dibe.2026.100874
- Read in full via ScienceDirect (RIT).

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of bio-composite** for non-load-bearing applications, at functional equivalence (>=7 MPa at 28 d) | LCA section |
| system boundary | **cradle-to-gate**, ISO 14040/44 and EN 15804+A2, Ecoinvent v3.8, ReCiPe 2016; no Module D credits | same |
| intervention | **accelerated carbonation curing (ACC)** of a shale-ash / steel-slag ternary binder | same |
| comparator | **OPC-based system** | same |
| absolute baseline GWP | **not reported**; the result is given as a ratio | — |
| **outcome** | bio-composite generates **34.6% of OPC's climate-change impact**, i.e. a **65.4% reduction** | Results, Fig. 13 |

Net CO2 uptake is **0.42-0.55% of specimen mass**, credited within the cradle-to-gate GWP
following EN 15804+A2.

> **This is the clearest single attribution in the retrieved set.** The authors state the
> reduction is "primarily due to the elimination of clinker which is a high-temperature,
> high-emission component from its formulation." The carbonation contribution is half a percent
> of specimen mass; the 65.4% comes from removing Portland clinker.
>
> **Caveat to record.** The comparison is bio-composite-with-ACC against OPC, so binder
> substitution and carbonation are confounded. The study qualifies under I4 and I5 — the
> product is carbonation-cured and the comparator is non-carbonated — but the effect cannot be
> attributed to carbonation, and the authors do not attempt to.

---

## Carbon Capture Sci. Technol. 2025 — "Carbonation behavior of reactivated recycled concrete fines"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.ccst.2025.100557

| field | value | location |
|---|---|---|
| functional unit | **1 tonne of cured cementitious paste** | Sec 4.6 |
| system boundary | cradle-to-gate; Ecoinvent v3.9 in SimaPro | same |
| comparator | **conventionally water-cured OPC** | same |
| **absolute baseline GWP** | **591 kg CO2 eq/t** | Sec 4.6, Fig. (c) |

| formulation | GWP | reduction |
|---|---|---|
| C-800-0 | **99 kg CO2 eq/t** | **83%** |
| C-1000-0 | **155 kg CO2 eq/t** | **74%** |
| C-1000-20 | **231 kg CO2 eq/t** | **61%** |

The paper attributes the reductions to two mechanisms, the first being substitution of limestone
with recycled concrete fines — clinker displacement again.

---

## Cleaner Waste Systems 2026 — "Synergistic carbonation pretreatment for performance enhancement and CO2 uptake in limestone-blended cement"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.clwas.2026.100480

| field | value | location |
|---|---|---|
| functional unit | **1 kg of cementitious material** | LCA section |
| system boundary | cradle-to-gate (raw material extraction, carbonation pretreatment, cement manufacture, carbonation curing); ISO 14040/14044; openLCA v2.4; ReCiPe 2016 (H); ELCD v3.2 | same |
| comparator | control mixture (OPC) | Sec 7 |
| **outcome** | **21% GWP reduction** at 25% replacement with highly carbonated limestone powder | Sec 7, Fig. 15 |

> The authors attribute the reduction to "both the lower clinker content in the mixture and the
> CO2 sequestration potential of the carbonated limestone" — the two contributions are not
> separated, and clinker is named first.

---

## Case Studies in Construction Materials 2026 — "GGBS-biochar concrete for low-carbon construction"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.cscm.2026.e06336

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of concrete** | Fig. 28, LCA section |
| system boundary | **cradle-to-gate** | Fig. 28 |
| comparator | conventional concrete control (five mixes assessed) | same |
| intervention | **accelerated carbonation curing (ACC)** | Abstract |
| **outcome** | **~14% GWP reduction** for S20-BC5 | Highlights; LCA section |

CO2 uptake rose from 3.90% to 6.09% of mass (TGA); under ACC, S20-BC5 gained 13.2% compressive
strength over its water-cured counterpart.

> **Confound to record.** The 14% is for a mix containing 20% GGBS and 5% biochar assessed
> against conventional concrete, so binder substitution and carbonation are not separated. The
> study qualifies under I4 and I5 but the effect is not attributable to carbonation alone.

---

## Also screened and excluded

| Study | DOI | Reason |
|---|---|---|
| Optimizing carbon sequestration in a sustainable gypsum-based material, *Mater. Today Sustain.* 2025 | 10.1016/j.mtsust.2025.101296 | **I3 and I5** — gypsum-based, not a cement-based product; and the comparator is an *EC-cured cement block*, i.e. itself carbonated, so no non-carbonated arm exists |
| A digital workflow for assessing lifespan, carbonation, and embodied carbon of reusing concrete in buildings, *J. Build. Eng.* 2024 | 10.1016/j.jobe.2024.110536 | **X1 and X7** — building-scale assessment of *service-life* carbonation during reuse, not accelerated curing. Reports CO2 uptake over service life at under 6% of embodied carbon and states "the climate benefits of reuse greatly exceeded those of carbonation" — useful for the Discussion, not eligible |
| Application of total carbon analysis for CO2 fixation in cementitious materials, *Case Stud. Constr. Mater.* 2024 | 10.1016/j.cscm.2024.e03880 | **X3** — a measurement-method study; no functional unit, no system boundary, no life-cycle accounting |

---

## Applied Sciences 2024, 14:7442 — "Life Cycle Carbon Assessment of Mortars with Carbonated and Non-Carbonated Recycled Aggregates"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.3390/app14177442 (open access)

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of industrially formulated powder-state mortar** | Sec 2.1 |
| system boundary | **cradle-to-gate** (product stage) | Sec 2.1 |
| design | **three arms**: reference mortar with natural aggregate; mortars with non-carbonated recycled aggregate; mortars with the same aggregate after forced carbonation | Sec 2, Sec 4 |
| **effect of aggregate substitution alone** | **3.3-7.5% reduction** vs the natural-aggregate reference (3.3-3.8% at 50% replacement; 6.3-7.5% at 100%) | Sec 4, Table 8, Fig. 2 |
| **effect with carbonated aggregate** | **up to 37% reduction** | Sec 4 |

> **This study runs against the pattern in Section 4.5 and must be reported as such.** It is a
> properly matched three-arm design — the same aggregates, with and without forced carbonation —
> and here carbonation adds a large benefit rather than subtracting one: from at most 7.5% to
> as much as 37%.

---

## iScience 2022, 25:104261 — "An industrial demonstration study on CO2 mineralization curing for concrete"   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.isci.2022.104261 (open access)

| field | value | location |
|---|---|---|
| functional unit | **1 m3 of product** | LCA section; STAR Methods |
| system boundary | **cradle-to-gate**, ISO 14040/14044, ecoinvent 3.7 | LCA section, Fig. 11 |
| comparator | **autoclaved curing** of the same block | same |
| **effect** | CO2 mineralization curing (CMC) emits **182 kg CO2-Eq/m3 less** than autoclaved curing | Abstract; Fig. 12 |
| **absolute outcome** | CO2 curing gives **GWP of -120 kg CO2-Eq/m3** — net-negative | Fig. 12 |
| attribution | **direct CO2 sequestration accounts for ~65% of the reduction** | Abstract |

Process: >98% CO2 conversion ratio with carbonation exotherm recycling; operational cost
30.93 USD/m3.

> **A genuine counter-example, and the clearest one in the set.** In every other study the
> benefit tracks avoided clinker and sequestration is a minor term. Here the authors attribute
> ~65% of a 182 kg/m3 reduction to direct sequestration.
>
> Two qualifications belong with it rather than against it. The comparator is **autoclaved
> curing**, which is itself energy-intensive, so part of the remaining ~35% is avoided autoclave
> energy rather than clinker displacement. And the process is unusually optimised: a >98%
> conversion ratio with exotherm recycling is not representative of the laboratory
> configurations in most of the retrieved set. It demonstrates what carbonation can achieve
> when the process is engineered for it, which is a different claim from what it typically
> achieves.

---

## Ostovari et al. 2021 — Environ. Sci. Technol. 55:5212-5223   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1021/acs.est.0c07599
- "From unavoidable CO2 source to CO2 sink? A cement industry based on CO2 mineralization"
- Read in full via ACS (RIT).

| field | value | location |
|---|---|---|
| functional unit | **1 tonne of cement, or 1 tonne of blended cement of equivalent performance** | Sec 2.4 |
| system boundary | cradle-to-gate | Sec 2.1, Fig. 1 |
| comparator | conventional Portland cement production | Sec 2.1 |
| intervention | CO2 mineralisation of slag, the silicate product blended into cement | Sec 2.2-2.3 |
| **outcome** | carbon footprint as low as **-0.16 t CO2e/t cement**, or **-0.53 t CO2e/t** at the maximum theoretical blended fraction of 55 wt% | Abstract; Sec 3.2 |

**The most direct quantification of the clinker mechanism in the set.** The paper reports that
increasing the blended fraction by 1% reduces the carbon footprint by **5 kg CO2e/t cement up to
a 32 wt% blend, and by 8 kg CO2e/t above it**. The benefit is close to linear in the quantity of
clinker displaced, and the authors describe the configuration as combining carbon capture and
storage with "reducing clinker usage".

> Note for the record: J. Skocek is a co-author here and also of the 2020 *Sci. Rep.* paper
> excluded under X3. The same group produced one study that meets every criterion and one that
> declares no functional unit — further evidence that the gap is conventional rather than a
> matter of capability.

---

## Also screened

| Study | DOI | Outcome |
|---|---|---|
| Quality-Matched Life Cycle Assessment of CCU Supply Chains for SMR Tail Gas CO2, *Sustainability* 2026 | 10.3390/su18105063 | **EXCLUDE — I3.** Cradle-to-gate, but the functional unit is *1 kg of CO2 treated and utilised* and the object is a capture-to-utilisation pathway, not a cement product. Useful for the Discussion: it puts concrete curing near break-even at **0.010 kg CO2-eq per kg CO2 utilised**, falling to 0.005 when capture purity is matched to demand |
| Dynamic carbon footprint trade-off between carbonation curing, mineral carbonation and natural carbonation, *Environ. Res. Lett.* 2026 | 10.1088/1748-9326/ae9968 | **Not assessed — X8.** The publisher platform returns a bot-detection challenge; the full text could not be retrieved by any available route. Flagged for manual retrieval |

---

## Li et al. 2023 — J. Clean. Prod. 383:135501   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.jclepro.2022.135501
- "Carbonation curing of mortars produced with reactivated cementitious materials for CO2 sequestration"
- Retrieved by the Web of Science confirmatory search; present in the OpenAlex set but not yet screened.

| field | value | location |
|---|---|---|
| functional unit | **1 tonne** | Sec 3.7 |
| system boundary | **cradle-to-gate** production of the mortar | Sec 3.7, Fig. 2 |
| method | IPCC 2021 GWP100 and cumulative energy demand | Sec 3.7 |
| comparator | **Portland cement mortar** (w/c 0.4, sand/cement 1.5) | Sec 3.7 |
| **baseline GWP** | **378 kg CO2 eq** | Sec 3.7, Fig. 11 |
| **carbonation-cured RCM mortar** | **93.6 kg CO2 eq** | same |
| **effect** | **-75.2%** | same |

Attribution given by the authors: saving in raw materials and the recycled calcium source
(165 kg lower from those alone), with a further 152 kg from sequestered CO2.

> Units are printed in the source as "kg CO2 eq/kg" while the stated functional unit is 1 tonne;
> transcribed here as reported, with the discrepancy noted. This is itself a minor instance of
> the reporting problem the review documents.

---

## Di Maria et al. 2020 — Int. J. Greenh. Gas Control 93:102882   **INCLUDE (I1-I6 met)**

- **DOI:** 10.1016/j.ijggc.2019.102882
- "Environmental assessment of CO2 mineralisation for sustainable construction materials"

| field | value | location |
|---|---|---|
| functional unit | **0.08 m3 of wall block, matched on compressive strength** — 92 kg carbonated block against 94.4 kg PC-based concrete | Sec 2.2.1, Table 1 |
| system boundary | cradle-to-gate; goal-and-scope, LCI, LCIA, interpretation | Sec 2.2 |
| comparator | **PC-based concrete blocks of similar properties** | Sec 2.2.1 |
| product | stainless steel slag + sand + water, compacted, cured at 5 bar in >90% CO2 — **contains no Portland cement** | Sec 2.1 |

**Climate change reduction versus PC-based concrete:**

| CO2 recovery route | reduction |
|---|---|
| S1 cryogenic | **68%** |
| S2 membrane | **77%** |
| S3 chemical absorption | **71%** |

> **The cleanest isolation of the CO2-supply term in the whole set.** One product, one functional
> unit, one comparator, three CO2 recovery processes — and a nine-point spread in the result that
> is attributable to nothing but how the CO2 was obtained. The electricity demand of the recovery
> route differs by a factor of eighteen across the three scenarios (5.3, 0.3 and 3.4 kWh), and
> that is what moves the answer.
>
> The magnitude of the reduction, meanwhile, follows the usual pattern: the product contains no
> Portland cement.

---

## Chen et al. 2022 — Cem. Concr. Compos. 134:104764   **EXCLUDE — I2**

- **DOI:** 10.1016/j.cemconcomp.2022.104764
- "Modification of carbonation-cured cement mortar using biochar and its environmental evaluation"

> Defines a functional unit (Table 6, "Mix design of the functional unit") and reports an
> environmental evaluation of carbonation-cured mortar, but declares **no system boundary** and
> cites no LCA standard, software or inventory database; the paper's outline contains no
> life-cycle methodology section. **This is the seventh paper in the retrieved set reporting an
> environmental result for a carbonation-treated cement product without the disclosures needed
> to interpret it.**

---

## Summary

See `Revision/SOURCE_PDF_LINKS.md`. Paywalled items (Elsevier, RSC, ASCE) need RIT access.


| slot | study | recorded in Table 2 | what the paper reports | verdict |
|---|---|---|---|---|
| [34] | Monkman & MacDonald 2017 | 7.5% [5.0, 10.0] | **4.6%** carbon-footprint reduction | below the recorded CI; 5-8% is binder loading, a different quantity |
| [35] | Tanzer et al. 2021 | 8.0% [2.0, 14.0] | **+3.2%** in the only reducing scenario; **-15.0%** and **-6.8%** in the other two | no basis for 8.0% or for 14.0% |
| [36] | Huang et al. 2019 | 15.0% [0.0, 30.0] | **292-454 vs 419 kg CO2-eq/m3**, i.e. **-8.4% to +30.3%** | interval truncates the net-emitting tail |
| [17] | Ravikumar et al. 2021 | 6.5% [3.5, 9.5] | no percentage; net benefit **negative in 56-68 of 99** datasets | sign reversed |
| [39] | Skocek et al. 2020 | 37.0% [17.0, 57.0] | 114.5 g CO2 per 100 g clinker replaced, vs a limestone comparator | not an LCA; fails the inclusion criterion |
| [10] [18] [33] [37] [38] [40] [41] | seven slots | 14.0 / 108.0 / 97.0 / 41.0 / 52.8 / 32.5 / 51.0 | no such papers exist | unresolvable |

**Five of five checkable studies fail to support the value recorded against them.**

One substantive observation, separate from the provenance question. Three of the five --
Ravikumar, Tanzer and Huang -- explicitly report that accelerated carbonation can *increase*
life-cycle emissions: Tanzer's +42 kg/m3 without strength gain, Huang's 454 kg/m3 case,
Ravikumar's 56-68 of 99. Two of them attribute the benefit, where it exists, to cement
displacement rather than to CO2 uptake -- Monkman's 4.6% comes from binder reduction, Huang's
30% requires "adjusting the binder types".

That is the manuscript's own thesis: Section 5's condition framework, and the Sobol result
that clinker displacement drives ~89% of the variance in r. The real literature supports the
paper's argument. What it does not support is a pooled 31.8% reduction.
