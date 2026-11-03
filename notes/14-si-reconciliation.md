# SI reconciliation pilot (TSA46)

Status: first implementation merged in `UBC-FRESH/femic` #396 (`2a02fac`);
follow-ups in #399.

## Why this exists

The P117 attempt to derive a new ALS site-index layer was rejected as
research-scale modelling. Site index is already a provincial product:

- VRI carries `SITE_INDEX` and `EST_SITE_INDEX` per polygon;
- VDYP carries primary-layer `ESTIMATED_SITE_INDEX` where populated; and
- SIBEC provides BEC-unit/site-series/species means, plot counts, and standard
  errors.

The useful software task is therefore provenance and reconciliation, not a new
model.

## What was run

```bash
python -m femic.site_index \
  --vri external/femic-tsa46-instance/data/vri_vclr1p_checkpoint8.feather \
  --vdyp external/femic-tsa46-instance/data/vdyp_lyr-tsa46.feather \
  --sibec $WORKDIR/sibec/sibec2013approx_final.xlsx \
  --out-csv $WORKDIR/si-reconcile/tsa46_si_reconciliation.csv \
  --out-json $WORKDIR/si-reconcile/tsa46_si_summary.json \
  --delta-threshold 2.0
```

## Result

| Item | Value |
| --- | ---: |
| VRI features | 171,826 |
| VRI `SITE_INDEX` present | 171,826 |
| VRI `EST_SITE_INDEX` present | 5,966 |
| VDYP primary-layer SI present | 3,384 |
| SIBEC match for VRI species | 136,807 |
| Complete VRI + VDYP + SIBEC triple | 2,285 |
| Conflicts at 2.0 m | 25,643 |
| Partial | 143,898 |
| Species mismatch (VRI vs VDYP) | 531 |

Top conflict BEC units: `CWHvh2` (11,259), `CWHms2` (3,436), `CWHvm2`
(2,537), `CWHvm1` (2,522), `CWHws2` (1,515).

Most conflicts are VRI values outside the BEC-unit/species SIBEC range, not
VRI-versus-VDYP disagreements. VDYP primary-layer SI is too sparse for a
complete three-way comparison.

## Interpretation

- SIBEC is aggregated to BEC unit + species because VRI has no site series. The
  range is a screening envelope, not a polygon point estimate.
- A conflict is a review flag, not a verdict that VRI or VDYP is wrong.
- The VDYP value is retained as the current curve input. The reference value
  does not change a curve, AAC, THLB, or schedule.
- The SIBEC 2014 addendum is not merged. AU-level TSA SI is a separate grain and
  is not forced into the polygon table.

## Follow-up

`femic` #399 (P119.2): merge the SIBEC addendum and reconcile AU-level
`03_input` SI separately. The contract is
`femic/docs/reference/contracts/site-index-reconciliation.rst`.
