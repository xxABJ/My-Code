# Analysis Report 2

Date: 2026-06-28

## Summary of Latest Findings

## 1. Breakpoint Location
- First break occurs at `p = 4`.
- For `p <= 3`:

$$
\frac{f3}{(abc)^p} = 1
$$

- For `p >= 4`:

$$
\frac{f3}{(abc)^p} = \frac{10p}{p!(p+2)}
$$

## 2. Invariants Confirmed Exactly (else-only `R_`, unchanged `Fi_`)
- For all `p >= 0`:

$$
\mathrm{inv\_b2} = \frac{B2_{total}}{FS} = \frac{p(p+2)(p+3)}{40}
$$

- For `p > 0`:

$$
\mathrm{inv\_r} = \frac{R}{Q3\cdot S6\cdot I1} = \frac{p}{2}
$$

(`inv_r` is undefined at `p = 0`.)

## 3. `Fi` Causality Test
- A/B tests with three `Fi` modes:
  - original
  - `abs(Ti)`
  - `abs(Ti) * AN`
- All produced the same breakpoint and invariant sequence.
- Conclusion: `Fi` is likely not the primary cause in the current else-only `R_` path.

## 4. Structural Diagnosis
- Main issue is factorial under-scaling in the FS plus normalization chain:

`indsum -> B2_total -> S6 -> R -> f3`

- `K` behaves like a compensator for this structural regime change, not random noise.

## 5. Non-Circular Proof Principle
- Do not inject direct reconstruction of `(abc)^p`.
- Avoid post-hoc correction if the goal is a true internal proof.
- Prefer deriving a transition law from native invariants.

## 6. Next Recommended Research Step
- Run parameter sweeps over `(a, b, c, AN)` to separate universal laws from parameter-dependent behavior.

## Related Files
- `ANALYSIS_REPORT.md`
- `invariant_research.py`
- `wtesting2.py`
