# 2026–2027 Resident Call Schedule — Flagged-Dates Report

**Scope:** Review of the *preliminary* on-call schedule (all 12 month tabs) against the program's
written rules (Rules tab), each resident's rotation assignments (Rotations Master Schedule),
PTO requests, holiday rules, and the day-of-week inconvenience weighting.

**Method & confidence:** Both workbooks were parsed into a structured model. As a correctness
check, the reconstructed per-resident call counts and day-of-week distributions **match the
schedule's own YTD tab exactly** (706 total shifts across 17 residents), so the findings below
are reliable rather than parsing artifacts. Each flag was additionally cross-checked against the
scheduler's own monthly "Call Variances" notes.

**Roster.** Interns/R1: Hard, Oehm, Schutt, Stanek, Strand, Wohlgemuth. R2: Beutel, Bottke, Bower,
Gaspar, Kendrick, Patel, Sublette. R3: Johnson, Lux, Mautino, Mudondo.

---

## 1. Hard rotation conflicts — 19 dates (must fix)

These are dates where a resident was assigned call while on a rotation that the rules prohibit
for that day.

### 1a. On a NO-CALL rotation (most severe — the resident cannot take any call) — 5

| Date | Day | Resident | Rotation | Note |
|---|---|---|---|---|
| 2026-07-17 | Fri | Bower (R2) | **NICU** | NICU = no call shifts |
| 2026-10-30 | Fri | Mautino (R3) | **Away** | Away 10/25–11/21; not caught in Oct variance box |
| 2026-11-13 | Fri | Mautino (R3) | **Away** | same Away block |
| 2027-04-14 | Wed | Sublette (R2) | **Peds ER** | Peds ED = no call shifts |
| 2027-05-17 | Mon | Bottke (R2) | **Peds ER** | Peds ED 5/9–5/22; **not flagged in May variance box** |

### 1b. Day-restricted rotation violations — 14

| Rule | Dates (resident) |
|---|---|
| **GYN/CM** — no Sun/Mon/Wed (must cover La Clinica & GYN) | 9/6 Sublette (Sun), 9/27 Patel (Sun)\*, 2/28 Kendrick (Sun), 3/17 Kendrick (Wed), 5/30 Bower (Sun) |
| **Ultrasound** — no Sun/Wed (on-site Mon & Thu only) | 11/4 Beutel (Wed), 11/11 Sublette (Wed), 4/18 Kendrick (Sun), 6/6 Gaspar (Sun) |
| **Cardiology** — no Tuesday (Wednesday personal clinic all day) | 8/25 Bottke, 1/12 Beutel, 3/9 Gaspar |
| **Dermatology** — no Monday (Tuesday Derm clinic) | 2/22 Mudondo, 3/8 Lux |

\* The 9/27 cell already shows Patel partly swapped to Kendrick (a transitional block-boundary cell).

---

## 2. PTO / explicit-instruction conflicts — 3 dates

| Date | Day | Resident | Issue |
|---|---|---|---|
| 2026-09-10 | Thu | Patel | YTD says **"Bottke & Patel Nexplanon training 9/10 evening — DO NOT schedule call 9/10."** Patel was scheduled. |
| 2027-03-15 | Mon | Schutt | Inside Schutt's PTO window (3/15–3/19). |
| 2027-05-18 | Tue | Wohlgemuth | Inside Wohlgemuth's PTO window (5/17–5/21). The scheduler had already marked this cell `**` as a known problem. |

All other PTO windows were correctly respected in the preliminary.

---

## 3. Soft / "limited" conflicts — 11 dates (rule-permitted but worth noting)

These appear in the scheduler's variance boxes and are allowed by the rules ("limited call" /
"can be done if absolutely necessary"), but each is a candidate for relief.

| Rule | Dates (resident) |
|---|---|
| **R3 Orthopedics** — limited call only | 7/13 Lux, 7/16 Lux, 10/7 Johnson |
| **Community Based Practice** — avoid call during the 2 weeks away | 8/12 Lux, 8/24 Lux, 11/5 Mudondo, 11/18 Mudondo, 3/11 Mautino, 3/23 Mautino, 6/3 Johnson, 6/17 Johnson |

---

## 4. Coverage gaps & structural anomalies

| Item | Detail |
|---|---|
| **Winter holidays have no intern** | 12/20/26–1/2/27 is covered by a senior only (no intern). Christmas (12/25), New Year's Eve (12/31), and New Year's Day (1/1) therefore have **no intern on call**, which conflicts with the rule "Interns schedule Thanksgiving, Christmas, and New Years" (and with interns working that period). |
| **Missing night-float intern (8/20/26)** | Hard is on the Night Float rotation 8/16–8/29 but is absent from the 8/20 cell; the day shows two seniors and no intern — a likely omission. |
| **Patel double-booked as 2nd senior on 12 days** | 7/15–9/27, Patel appears as an extra second senior (explains his year total of 35 vs the other R2s' 33). Likely reflects his off-cycle/transition status; flagged for confirmation. |

---

## 5. Spacing — call on consecutive days (no post-call day) — 4

The rule is "24-hour call **with post-call day**," so back-to-back call is undesirable.

| Resident | Dates | Context |
|---|---|---|
| Mautino (R3) | 10/12 → 10/13 | Mon→Tue |
| Patel (R2) | 2/2 → 2/3 | Tue→Wed |
| Stanek (R1) | 2/14 → 2/15 | Sun → Presidents Day Mon |
| Oehm (R1) | 5/9 → 5/10 | Mother's Day Sun → Mon |

---

## 6. Fairness & holiday-equity observations

**Day-of-week inconvenience** (weighting: Wed/Thu = best, Mon/Tue = average, Fri/Sun = bad, Sat = worst):

- **R3s are the most uneven.** Mautino carries the heaviest load (9 Fridays + 6 Saturdays, 0 Sundays →
  avg inconvenience 2.42) while Lux is lightest (2.15) — a within-cohort spread of 0.27.
- **R2 Saturdays are uneven:** Beutel has 7 Saturdays (the worst day) vs 4 for several peers.
- Interns are already tightly balanced (8/8/8 Fri/Sat/Sun each).

**Holiday distribution:**

- **Intern Stanek works 3 holidays** (Labor Day + Thanksgiving + Presidents) while **Hard and Strand
  work none.**
- **Beutel (R2) works 3 minor holidays** (July 4 + Presidents + Mother's Day) — exceeds the "two minor
  holidays" cap; **Bower and Sublette** carry essentially none of the tiered holidays.
- The **four "mix-up" holidays** (July 4, Labor Day, Easter, Memorial Day) are **not** on four distinct
  interns — Oehm has both July 4 **and** Easter.

---

## 7. Summary counts

| Category | Count |
|---|---|
| Hard rotation conflicts | **19** |
| PTO / explicit-instruction conflicts | **3** |
| Soft / "limited" conflicts | 11 |
| Consecutive-day (no post-call) pairs | 4 |
| Coverage gaps / structural anomalies | 3 |

The **22 hard + PTO conflicts** are the must-fix items; they are fully resolved in **Version 1
(Minimal Repair)**. The soft conflicts, spacing, coverage gaps, and fairness/holiday imbalances are
addressed in **Version 2 (Full Rebuild)**. See the companion *Optimization & Recommendations Report*.
