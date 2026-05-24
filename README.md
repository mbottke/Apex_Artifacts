# Apex-Artifacts — Claude Project package

Drop-in package for setting up a Claude.ai Project that produces apex-quality artifacts (React components, SVGs, Mermaid diagrams, long-form docs, data visualizations).

Built from `claude/prepare-apex-artifacts-BZAJZ` at Phase 6 close (Waves 7–13). 221 files; ~5.3 MB.

---

## What's in this folder

```
apex-artifacts-project/
├── README.md                  ← you are here
├── CLAUDE-projects.md         ← paste into Project's Custom Instructions
└── knowledge/                 ← upload contents to Project Knowledge
    ├── references/            ← REQUIRED — 121 files in 4 sub-trees
    │   ├── (22 top-level)     ←   manifesto, pre-delivery-checklist, etc.
    │   ├── libraries/         ←   16 platters (color, type, viz, medical, etc.)
    │   ├── medium-playbooks/  ←   50 playbooks + cross-cluster/ (9)
    │   └── tear-downs/        ←   45 deconstructed exemplars
    ├── templates/             ← RECOMMENDED — 71 concrete starters
    └── tokens/                ← OPTIONAL — 6 design-token CSS sets + tokens.json
```

---

## Setup (Claude.ai Project) — 3 steps

### 1. Create the Project

1. Open <https://claude.ai/projects>
2. Click **Create project**, name it (e.g. "Apex Artifacts")
3. Add a short description

### 2. Paste the custom instructions

Open `CLAUDE-projects.md` (16 KB / 223 lines), copy its entire contents, paste into the Project's **Custom instructions** field, save.

This is the trimmed version: prime directives, philosophy, non-negotiables, calibration cards, decision tree, operating loop. The detailed file index and Claude-Code-only sections are removed — the Knowledge browser is the file index when you're in a Project.

### 3. Upload the knowledge

In the Project's **Knowledge** panel, upload the contents of `knowledge/`. Three approaches, in order of preference:

- **Drag-and-drop the `knowledge/` folder contents** — Claude.ai Projects preserve directory structure on upload. Drag `references/`, `templates/`, and `tokens/` in.
- **Upload `references/` only first**, then add `templates/` and `tokens/` later as you find you want concrete starters or palette CSS.
- **Selective upload**: at minimum, upload the entire `references/` tree. The Project will work without `templates/` (Claude reconstructs from playbooks) and without `tokens/` (Claude uses the descriptions in `references/design-tokens.md`), but quality is higher with all three.

Claude Projects support ~200 MB of knowledge; this package is ~5.3 MB.

---

## Verification — one prompt

Open a new conversation in the Project and ask:

> "Build me a small interactive React artifact that explains how a Bloom filter works."

A correctly-configured Project will:

- Identify the medium (React) and load `references/medium-playbooks/claude-react-artifact.md`
- Roll for cross-pollination from `references/libraries/inspiration-atlas.md`
- Pick a signature move from `references/wow-taxonomy.md` and declare it before building
- Apply one of the 6 design-token sets (not default Tailwind)
- Follow the Prime → Show → Explain → Invite → Check sequence from `references/educational-scaffold.md`
- Run the pre-delivery checklist and emit the required YAML block before delivery
- Self-rate against the 5-tier ladder in `references/taste-calibration.md`

If those things are absent, the Custom Instructions paste didn't take — re-check Step 2.

---

## Coverage (Phase 6 totals)

| Category | Count |
|---|---|
| Medium playbooks | 50 (covers React, SVG, Mermaid, long-form, slides, notebooks, email, dashboards, forms, print/PDF, technical docs, infographic, scrollytelling, explorable explanations, mnemonic medium + 8 cross-cluster forms + 4 sci/med education + 4 sci/med creative + 6 medical Wave-10 + 6 Wave-11 per-persona + 4 Wave-12 multi-persona + 10 Wave-13 specialty depth) |
| Templates | 71 (React + SVG + Mermaid + markdown + Quarto qmd; with body-of-work continuity across waves) |
| Tear-downs | 44 (Ciechanowski, Case, Minard, Tufte, Linear, Pudding, NYT, Stripe, plus 12 medical incl. I-PASS, NIH R01 Aims, AO Surgery, Hoppenfeld, WHO Surgical Safety, ACC/AHA HF 2022, SCAT6, UpToDate algorithm box) |
| Libraries | 16 (color, type, viz grammar, composition, motion, reader models, rhetorical atlas, pedagogy, iconography, inspiration atlas, dataset corpus, snippet cookbook, utilities, medical, scientific, romantic) |
| Editorial voice registers | 6 (Editorial / Technical / Warm-familiar / Editorial-wonder / Literary / Critical-collegial) |
| Named failure modes | 70 across voice / structure / visual / argument / process / teaching / science |
| Named signature moves | 89 (54 original + 5 Wave-4 A.x + 20 Wave-9 + 5 B.x body-of-work + 5 Wave-13 additions) |
| Reader-models personas | ~80 (40 clinical-stakeholder personas added Wave 10) |
| Named clinical-teaching micro-skills | 14 (OMP, SNAPPS, RIME, Aunt Minnie, Calgary-Cambridge, SPIKES, NURSE, Ask-Tell-Ask, Pendleton, Advocacy-Inquiry, ALOBA, R2C2, GAS-PEARLS-3D, AAR) |
| Design-token sets | 6 substitutable (ft-salmon, quanta-cobalt, penguin-classic, ukiyo-e, scandi-fog, default-cool) |

---

## Maintaining this Project

When the standards or libraries evolve in the source repo, re-run the build to refresh this package, then re-upload to the Project Knowledge (Claude doesn't hot-reload Project files).

Build command from repo root:

```bash
./tools/pack-for-project.sh
```

(Or follow the manual steps in `SETUP.md` Path A in the source repo.)

---

## What's NOT in this package

Intentionally excluded — not relevant to Claude.ai Project context:

- `.claude/skills/` — Claude Code / Agent SDK skills (Projects don't invoke skills)
- `tools/artifact-lint/` — CLI linter (no shell access in Projects)
- `references/user/` — per-user overrides (SETUP.md guidance: don't auto-upload)
- The full untrimmed `CLAUDE.md` — too large for Custom Instructions; the trimmed `CLAUDE-projects.md` is the paste-ready version
