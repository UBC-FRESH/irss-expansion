# P6 first maintenance review

Date: 2026-11-03
Phase: P6 Operate and maintain
Parent issue: #35
Tasks: P6.1, P6.2
Plan: [`25-p6-maintenance-plan.md`](25-p6-maintenance-plan.md)
Schedule: [`../registry/maintenance.yaml`](../registry/maintenance.yaml)

## Scope and method

This is the baseline review that starts the recurring cycle. It covers the whole
registry at the status-group level, checks the active target records against
GitHub, and refreshes every unique public source URL.

Evidence was read on 2026-11-03 with:

```bash
python scripts/check_maintenance.py --due
python scripts/check_issue_drift.py --json
python scripts/refresh_sources.py --json
gh issue view <number> --repo UBC-FRESH/<repo> --json state,title
gh pr view <number> --repo UBC-FRESH/<repo> --json state,mergedAt
git ls-remote https://github.com/UBC-FRESH/<repo>.git refs/heads/main
```

The audit is read-only. No target issue, branch, pull request, setting, tag, or
release was created or changed. No source URL was edited.

## 1. Schedule and consistency

- `registry/maintenance.yaml` records 90-day registry reviews, a 180-day source
  refresh, and a 30-day issue/registry drift check. The next dates are
  2027-02-01, 2027-05-02, and 2026-12-03.
- `python scripts/check_maintenance.py --due` reports no errors: the schedule
  arithmetic, the generated register, the resolution fields, and the active
  records agree.
- The dashboard runs the deterministic check on every commit. The calendar
  check stays manual so a clean checkout does not turn red on a date alone.

## 2. Source refresh

`python scripts/refresh_sources.py --json` checked 84 unique URLs from 62
candidates.

| Outcome | Count | Meaning |
| --- | ---: | --- |
| `ok` | 63 | HTTP 2xx; reachable on 2026-11-03 |
| `blocked` | 21 | HTTP 403 from the publisher; the page may exist but refuses an automated client |
| `broken` | 0 | No network, redirect, 404, or other failure |

The 21 blocked URLs are DOI links that resolve to publisher pages:

| Publisher host | Blocked |
| --- | ---: |
| `academic.oup.com` | 7 |
| `cdnsciencepub.com` | 6 |
| `www.tandfonline.com` | 3 |
| `pubs.cif-ifc.org` | 2 |
| `zslpublications.onlinelibrary.wiley.com` | 1 |
| `onlinelibrary.wiley.com` | 1 |
| `www.mdpi.com` | 1 |

The check proves reachability, not content. A blocked DOI is recorded as blocked,
not as verified. The 63 `ok` responses include the IRSS, Silva21, GitHub, and
USDA pages plus the DOI links whose publishers allow the client.

## 3. Issue and registry drift

The active set is the one queued candidate and the two adopted candidates. The
live state matched every recorded expectation.

| Candidate | Status | Target record | Expected | Live on 2026-11-03 |
| --- | --- | --- | --- | --- |
| `GRO-06` | `queued` | `femic` [#376](https://github.com/UBC-FRESH/femic/issues/376) | open | open |
| `CARB-01` | `adopted` | `femic` [#361](https://github.com/UBC-FRESH/femic/issues/361) | closed | closed |
| `CARB-01` | `adopted` | `ws4` [#357](https://github.com/UBC-FRESH/ws4/issues/357) | closed | closed |
| `CARB-03` | `adopted` | `fhops` [#381](https://github.com/UBC-FRESH/fhops/issues/381) | open | open |
| `CARB-03` | `adopted` | `fhops` pull [#383](https://github.com/UBC-FRESH/fhops/pull/383) | open | open, CI success, not merged |

The live `main` heads moved since the P4 reconciliation in `ws4` (`a86f884` to
`26402dd`) and `fhops` (`296e2cf` to `440a30e`). `femic` (`faf00af`), `ws3`
(`b84a0ae`), `nemora` (`060c688`), and `fresh-road` (`df8ad2d`) are unchanged.
The movement does not add candidate-specific evidence and does not change a
score.

## 4. Re-score and status decisions

| Status group | Count | Decision | Reason |
| --- | ---: | --- | --- |
| `complete` | 17 | No change | P4 reconciled every row against a closed target record and merged evidence; no later candidate-specific evidence was found |
| `adopted` | 2 | No change | `CARB-01` is merged; `CARB-03` is still live and unmerged, so `adopted` still means "taken up" |
| `queued` | 1 | No change | `GRO-06` is still open under `femic` P117.2 (#376) and waits on a separate target-repository approval |
| `shortlisted` | 14 | No change | No new source or target evidence changes the screening scores; they stay in the reviewed queue |
| `candidate` | 23 | No change | The evidence is still metadata and abstract level; no candidate meets a retirement trigger |
| `deferred` | 4 | No change | `DIS-02` and `DIS-03` failed their readiness tests; `PLAN-06` and `CARB-04` remain held with their revisit triggers |
| `rejected` | 1 | No change | `INV-04` remains out of scope as a new general ALS site-index model |

Score changes: none. Status changes: none. Retirements: none. No candidate
failed contact with the live record or the public sources in this cycle.

The active scores remain:

| Candidate | Effort | Impact | Readiness | Risk | Score | Revisit |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `GRO-06` | M | 5 | 4 | 2 | 5.00 | When `femic` P117.2 starts or closes |
| `CARB-01` | M | 5 | 4 | 2 | 5.00 | If either adopted target record disappears |
| `CARB-03` | S | 3 | 4 | 2 | 6.00 | If FHOPS pull #383 merges, closes unmerged, or idles for a cycle |

## 5. Registry metadata

`meta.last_audited` stays `2026-11-03`, and `meta.audit_note` names this review
alongside the P2, P3, and P4 audits. The generated register is regenerated from
the registry after the metadata change. No candidate field, source, score, or
status changed.

## 6. Limits

- The review checked source reachability and live target state, not the content
  behind a blocked DOI or a target test suite.
- The 17 `complete` rows rely on the P4 reconciliation and its dated evidence;
  this review did not re-read every merged diff.
- The live target state is a 2026-11-03 snapshot. The next drift check is due
  2026-12-03, and the next full review is due 2027-02-01.
- The 21 blocked DOI rows are not evidence that the article changed or vanished.
  They are a publisher policy boundary.
