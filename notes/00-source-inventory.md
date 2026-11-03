# Source inventory and mining method

Date: 2026-10-25.

Reviewed: 2026-11-03 (P1.2). All 22 public source URLs in this note return HTTP
200. The carried counts were re-derived from the current pages: 493 IRSS
publication records, 47 Silva21 project pages, 12 hubs, 65 DOI-linked scientific
publications, and 62 registry candidates. The Silva21 extension-note count was
corrected from 14 to 16 notes across 15 volumes, because Volume 6 has two numbered
issues. No candidate evidence or score changed.

## Scope

The mine covers two public bodies of work:

1. **UBC Integrated Remote Sensing Studio (IRSS)** — research themes, project
   narratives, and the publications list at <https://irsslab.forestry.ubc.ca>.
2. **Silva21** — a five-year, NSERC-funded research programme led by Alexis
   Achim (Université Laval) with Nicholas Coops (UBC IRSS) as a principal
   collaborator, at <https://www.silva21.com>.

The target is the FRESH forest modelling ecosystem: `femic`, `ws3`, `ws4`,
`fhops`, and `nemora`.

## What was fetched

| Page or source | URL | What it contributed |
| --- | --- | --- |
| IRSS home and research index | <https://irsslab.forestry.ubc.ca/research/> | The 11 research themes and the lab's framing |
| NTEMS | <https://irsslab.forestry.ubc.ca/research/ntems-national-terrestrial-ecosystem-monitoring-system/> | National Landsat change, attribution, recovery |
| BioSpace | <https://irsslab.forestry.ubc.ca/research/biospace/> | Biodiversity modules and indicators |
| Biodiversity | <https://irsslab.forestry.ubc.ca/research/biodiversity/> | Avian SDMs, Dynamic Habitat Indices, conservation regionalization |
| Disturbance and habitat change | <https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/> | Anthropogenic disturbance regimes, grizzly food landscapes, LANDIS-II/TACA-GEM |
| Carbon and forest dynamics | <https://irsslab.forestry.ubc.ca/research/carbon/> | Disturbance-carbon links, Landsat attributes, GPP |
| Data fusion | <https://irsslab.forestry.ubc.ca/research/data-fusion/> | Hyperspectral + LiDAR + Landsat fusion for composition and structure |
| Mountain pine beetle | <https://irsslab.forestry.ubc.ca/research/mountain-pine-beetle/> | Landscape pattern and beetle infestation |
| LiDAR | <https://irsslab.forestry.ubc.ca/research/lidar/> | Structure, GPP, canopy-depth effects |
| Urban | <https://irsslab.forestry.ubc.ca/research/urban/> | Urban energy and vegetation (screened out) |
| Mobile remote sensing | <https://irsslab.forestry.ubc.ca/research/mobile-remote-sensing/> | Smartphone fuels app and volunteered data |
| Water resources | <https://irsslab.forestry.ubc.ca/research/remote-sensing-and-hydrology/> | Snow and hydrology (screened out for now) |
| IRSS publications | <https://irsslab.forestry.ubc.ca/publications/> | 493 publication records, 2004-2023 as rendered |
| Silva21 home | <https://www.silva21.com/?lang=en> | Programme scope: 38 projects, $5.5M, 5 universities, 50 collaborators, 2021-2026 |
| Silva21 projects | <https://www.silva21.com/projects> | 47 project pages across AD, AN, and OB |
| Silva21 publications | <https://www.silva21.com/publicationsscientifique?lang=en> | 50+ papers, 2022-2026, with DOIs |
| Silva21 climate data | <https://www.silva21.com/climatedata?lang=en> | ClimateNA/SilvR21, hub climate reports, GCM ensemble |
| Silva21 extension notes | <https://www.silva21.com/extensionnotes?lang=en> | 14 practitioner notes, 2023-2026 |
| Silva21 data portal | <https://www.silva21.com/dataportal?lang=en> | Globus-hosted LiDAR, climate, and spatial data; access by request |
| Silva21 research sites | <https://www.silva21.com/sitesderecherche?lang=en> | The hub network |

The 47 Silva21 project pages are mapped one by one in
[`07-silva21-project-map.md`](07-silva21-project-map.md).

## Counts

- IRSS research themes: 11.
- IRSS publication records parsed: 493 (2004-2023).
- Silva21 funded projects: 38, represented by 47 project pages.
- Silva21 scientific publications listed: 65 DOI-linked records (2022-2026; the carried
  "50+" summary remains true).
- Silva21 extension notes: 16, across 15 volumes (Volume 6 has two issues).
- Silva21 hubs: 12.
- Candidate integrations in this register: 62, in nine workstreams.

## Method

1. Fetch the public pages and preserve the rendered text locally for analysis.
2. Parse the publication list into year and title records to find recurring
   methods, sensors, and problem domains.
3. Read the Silva21 project pages for objectives, outcomes, partners, and
   linked publications.
4. Cluster the material into nine workstreams that match FRESH insertion
   points, not academic disciplines.
5. For each candidate, record the public source, the FRESH gap, the first
   integration step, and a risk note.
6. Score impact, readiness, effort, and risk on a 1-5 scale; compute a
   screening score; assign a wave using dependencies and strategic sequencing,
   not the score alone.

## What this mine is not

- It is **not** a full-text systematic review. The 493 IRSS records were mined
  at title, year, journal, and DOI level. Only the Silva21 project pages and a
  small number of key papers were read in more depth.
- It is **not** an author consultation. No IRSS or Silva21 researcher was
  interviewed. Readiness and risk are the planner's judgement.
- It is **not** a data-access agreement. The Silva21 portal is access-controlled;
  the register treats access as a dependency, not an assumption.
- It is **not** a publication-quality bibliometric analysis. Duplicate records,
  missing years, and inconsistent journal formatting exist in the source page.
- It is **not** a substitute for the target repos' own roadmaps. Accepted
  candidates must become issues in those repos.

## 2026-11-03 review (P1.2)

- Re-fetched every URL in the "What was fetched" table: 22 of 22 returned HTTP 200.
- Re-counted the IRSS publications page: 493 lines carry a 2004-2023 year, matching the
  carried figure. The page still stops at 2023.
- Re-counted the Silva21 project page: 47 "See the project" entries, matching the carried
  47 project pages. The 12-hub claim is confirmed by the research-sites page.
- Re-counted the Silva21 scientific-publications page: 65 unique DOI links, so the carried
  "50+" summary is conservative rather than stale.
- Corrected the extension-note count: the page lists volumes 1-14, and Volume 6 appears as
  two issues, so the current total is 16 notes across 15 volumes. The earlier "14" counted
  volume numbers, not notes.
- Re-counted the registry: 62 candidates in nine workstreams.
- No source was re-mined, no candidate evidence was changed, and no readiness or risk score
  was revised. Dynamic source pages can change after this date; re-check them before a
  future registry change.

## Known source limitations

- The IRSS publications page appears to stop at 2023, while Silva21's list
  covers 2024-2026. The mine uses both and does not claim a complete IRSS
  bibliography after 2023.
- Some Silva21 project pages are recruiting or have no named lead; the project
  map marks these `n/a`.
- The Silva21 project list has paired projects under the same code (for example,
  two `OB 7` projects). The register uses titles, not codes, to disambiguate.
- DOI links were taken from the public pages. A few records have formatting
  errors in the source; the register cites the public page as well as the DOI
  where the DOI is clear.

## Reproducing the mine

The source pages are public and stable enough to re-fetch. A future refresh
should:

1. Re-fetch the IRSS publications page and compare the record count.
2. Re-fetch the Silva21 projects and publications pages.
3. Add new records to the evidence table before changing a candidate.
4. Re-run `python scripts/check_registry.py` and `python -m pytest`.
5. Re-render `docs/candidates.md`.
