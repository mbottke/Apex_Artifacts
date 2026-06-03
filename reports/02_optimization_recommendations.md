# 2026–2027 Resident Call Schedule — Optimization, Recommendations & Alternatives

Companion to the *Flagged-Dates Report*. This document covers the two delivered schedule versions,
the recommendations behind them, and the alternative options considered.

---

## A. Two delivered versions

| | **Version 1 — Minimal Repair** | **Version 2 — Full Rebuild** |
|---|---|---|
| Goal | Fix only the rule violations, change nothing else | Re-derive the whole year for maximum fairness within the rules |
| Method | 1-for-1 same-day-of-week swaps | CP-SAT constraint optimization |
| Disruption | 20 swaps; everything else identical to your draft | Most assignments re-derived |
| Totals & day-mix | **Identical** to preliminary | Re-balanced to be near-equal within each class |
| Best for | Adopting now with minimal review | A fresh, provably-balanced calendar |

Both pass the same hard-rule QA: **0 rotation conflicts, 0 PTO conflicts, 0 double-bookings.**

---

## B. Version 1 — Minimal Repair (change log)

Each fix is a 1-for-1 swap with an eligible partner on the **same day of the week**, so both
residents keep their exact call total and day-of-week distribution — only the dates move.

| # | Fixed conflict | Reason | Swap made |
|---|---|---|---|
| 1 | 7/17 Bower | on NICU | Patel ↔ Bower (Bower → 7/24) |
| 2 | 10/30 Mautino | on Away | Lux ↔ Mautino (Mautino → 12/4) |
| 3 | 11/13 Mautino | on Away | Lux ↔ Mautino (Mautino → 12/18) |
| 4 | 4/14 Sublette | on Peds ER | Bower ↔ Sublette (Sublette → 4/7) |
| 5 | 5/17 Bottke | on Peds ER | Beutel ↔ Bottke (Bottke → 5/24) |
| 6 | 9/10 Patel | Nexplanon (do-not-schedule) | Sublette ↔ Patel (Patel → 9/3) |
| 7 | 3/15 Schutt | PTO | Oehm ↔ Schutt (Schutt → 3/8) |
| 8 | 5/18 Wohlgemuth | PTO | Strand ↔ Wohlgemuth (Wohlgemuth → 5/25) |
| 9 | 8/25 Bottke | Cardiology-Tue | Sublette ↔ Bottke (Bottke → 10/27) |
| 10 | 1/12 Beutel | Cardiology-Tue | Bower ↔ Beutel (Beutel → 12/29) |
| 11 | 3/9 Gaspar | Cardiology-Tue | Bottke ↔ Gaspar (Gaspar → 4/27) |
| 12 | 9/6 Sublette | GYN/CM-Sun | Patel ↔ Sublette (Sublette → 11/1) |
| 13 | 9/27 Patel | GYN/CM-Sun | Gaspar ↔ Patel (Patel → 12/13) |
| 14 | 2/28 Kendrick | GYN/CM-Sun | Bower ↔ Kendrick (Kendrick → 2/21) |
| 15 | 3/17 Kendrick | GYN/CM-Wed | Patel ↔ Kendrick (Kendrick → 2/24) |
| 16 | 5/30 Bower | GYN/CM-Sun | (3-way) → Gaspar; Bower → 5/16 |
| 17 | 11/4 Beutel | Ultrasound-Wed | Sublette ↔ Beutel (Beutel → 11/11) |
| 18 | 11/11 Sublette | Ultrasound-Wed | (paired with #17) |
| 19 | 4/18 Kendrick | Ultrasound-Sun | Bower ↔ Kendrick (Kendrick → 4/25) |
| 20 | 6/6 Gaspar | Ultrasound-Sun | Patel ↔ Gaspar (Gaspar → 5/30) |
| 21 | 2/22 Mudondo | Dermatology-Mon | Lux ↔ Mudondo (Mudondo → 3/8) |
| 22 | 3/8 Lux | Dermatology-Mon | (paired with #21) |

*QA: counts and day-of-week distribution identical to the preliminary for all 17 residents; no new
soft conflicts or back-to-back call introduced.*

---

## C. Version 2 — Full Rebuild

### C.1 Rules enforced as hard constraints
- No resident on call during a **no-call rotation** (Away, NICU, Peds Inpatient, Peds ED, Leave).
- **Rotation day-restrictions:** GYN/CM no Sun/Mon/Wed; Ultrasound no Sun/Wed; Cardiology no Tue;
  Dermatology no Mon; FM-Ambulatory (2nd half) no Sun/Mon/Wed; R2-Pediatrics no Thu.
- **No CBP or R3-Orthopedics call at all** (the rebuild eliminates even the "limited/soft" uses).
- **PTO** windows and the **9/10 Nexplanon** date fully respected.
- **Night-float** weeknights fixed by the rotation grid (unchanged).
- **Post-call day:** no back-to-back call for anyone (except within a night-float block).
- **R3 take no Sunday senior call** (single Lux-style exception permitted).
- **R2 carry 7–8 Sunday calls** and **14–16 weekend (Fri+Sat+Sun) calls** each.
- **Holidays:** each senior works at most one major *or* two minor; the four "mix-up" holidays
  (July 4, Labor Day, Easter, Memorial Day) land on four different interns; interns cover
  Thanksgiving, Christmas, and New Year's.
- **Coverage:** one intern + one senior every call day, including the 12/20–1/2 winter block
  (interns now included, correcting the preliminary's senior-only winter coverage).

### C.2 Fairness objective
Within each class, the solver minimizes the inequality of every weekday's load and of the total
weighted-inconvenience load (Wed/Thu = 1, Mon/Tue = 2, Fri/Sun = 3, Sat = 4) — i.e. the schedule
is made as even as the rules allow.

### C.3 Result — balance before vs after

Lower spread = fairer. "Δ" is the gap between the most- and least-burdened resident in the class.

| Metric | Preliminary | **Rebuild (V2)** |
|---|---|---|
| Hard rotation conflicts | 19 | **0** |
| PTO / Nexplanon conflicts | 3 | **0** |
| CBP / R3-Ortho ("soft") call | 11 | **0** |
| Back-to-back call (no post-call) | 4 | **0** |
| Interns covering Christmas / NYE / NYD | none | **all three (3 different interns)** |
| "Mix-up" holidays on distinct interns | no (Oehm ×2) | **yes — 4 distinct** |
| R2 weighted-load spread (excl. Patel) | 74–80 (Δ6) | **75–75 (Δ0)** |
| R2 Saturdays (excl. Patel) | 4–7 (Δ3) | **4–5 (Δ1)** |
| R3 weighted-load spread | 71–80 (Δ9) | **75–75 (Δ0)** |
| R3 Saturdays | 4–6 (Δ2) | **5–5 (Δ0)** |
| Intern totals | 55–58 (Δ3) | **59–59 (Δ0)** |
| R3 Sunday calls (rule) | Lux 1 | **0** |
| Patel (preserved outlier) | 35 | **36 (12 backup days)** |
| Senior holiday weight cap respected | no (Beutel 3 minor) | **yes (≤ one major / two minor each)** |

In the rebuild the six non-Patel R2s share a near-identical mix (32–33 calls, **weighted load 75 each**)
and the four R3s are **identical** (34 calls, weighted load 75 each) — so R2 and R3 now carry the *same*
weighted load, with per-call inconvenience averages of 2.27–2.34 (R2) and 2.21 (R3). Patel is the single
intentional outlier (36 calls, his 12 preserved backup days). No R3 works a Sunday at all (the rule's
ideal), and the heaviest-loaded R3 (Mautino, formerly 9 Fridays + 6 Saturdays) is now level with peers.

### C.4 Deliberate structural decisions
1. **Winter intern coverage (12/20–1/2).** Interns are added to the holiday block so Christmas / New
   Year's have intern call, per the rule "interns schedule Thanksgiving, Christmas and New Years" and
   your note that interns work that period. (Preliminary had seniors covering solo.)
2. **Patel's extra days are PRESERVED.** Patel keeps his 12 early-year "second-senior" backup days and
   his elevated total (35–36 vs the class's 33), reflecting his off-cycle volume. Ten of the twelve
   original dates are kept exactly; the two that were themselves rule violations — **9/10 (Nexplanon
   "do-not-schedule")** and **9/27 (GYN/CM Sunday)** — are relocated to two other Patel-eligible
   July–September weekdays. Every other senior remains at the standard one-senior-per-day, so Patel is
   the single intentional outlier; the partner on each of his backup days is rotated across the class.
3. **8/20 night-float intern restored.** The preliminary's missing intern on 8/20 (Hanna Hard's NF
   block) is filled.

---

## D. Recommendations (independent of which version you adopt)

1. **Fix the five no-call-rotation errors first** (Bower 7/17, Mautino 10/30 & 11/13, Sublette 4/14,
   Bottke 5/17). These are the highest-risk — a resident physically unavailable for call.
2. **Add intern coverage to the winter holidays** (Christmas, New Year's) — currently senior-only.
3. **Even out holidays:** Stanek (3) and Beutel (3 minor) are over; Hard, Strand, Bower, Sublette are
   under. Put the four "mix-up" holidays on four different interns.
4. **Relieve Mautino:** in the preliminary he carries the heaviest senior load (9 Fri + 6 Sat).
5. **Respect post-call** on the four back-to-back pairs (esp. the two holiday-weekend ones).
6. **Block-boundary check:** several conflicts occur on the first/last days of a 2-week rotation
   block (e.g., 9/27, 2/28) — worth a standing check when a rotation changes mid-weekend.

---

## E. Alternative options considered

- **Pure fairness (rejected per your instruction).** Letting R3s share Sundays makes every senior's
  day-mix identical (tightest possible balance), but it breaks the R3-no-Sunday rule, so it was not used.
- **Preserve the R2-Sunday / R3-Friday split (adopted).** Slightly less uniform across classes but
  faithful to program structure; this is the Version 2 you have.
- **Minimal vs full.** Version 1 if you want the smallest change that is rule-clean; Version 2 if you
  want the fairest calendar.

---

## F. Workbook tracking tables (both Excel versions)

Both workbooks keep the program's original **live formulas** — the monthly per-resident `COUNTIF`
totals (cols AH–AO), the **"Day of Weeks Tracking"** tables (M/T · W/TH · F · Sun · Sat) on every
month tab, and the **YTD** tab's cross-month `SUM` rollups. None of these were replaced with static
numbers; the formulas are intact and will recompute if you edit any cell.

Because the schedule cells changed, every formula's cached result was **recomputed and written back**,
so the tables show correct numbers immediately (no "open and recalc" needed). The recomputed values
were then **verified cell-by-cell against the solved schedule**: all 17 residents' YTD totals and all
five day-of-week groups match exactly, on every month tab and on the YTD tab. (The workbook is also
flagged to fully recalculate on open, so Excel will confirm the same numbers.)
