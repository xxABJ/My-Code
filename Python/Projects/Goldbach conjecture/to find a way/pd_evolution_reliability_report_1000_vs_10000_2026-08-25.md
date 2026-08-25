# PD Evolution Reliability Report

Prepared: 2026-08-25
File analyzed: pd_evolution.py

## 1. Executive summary

This report brings together the test results from the original state machine across multiple run lengths, including the strong evidence that the machine depends on the chosen range. The most striking fact is not just that the machine makes slips; it is that the location of those slips changes with the run horizon.

The main findings are:

- The machine can produce a surprisingly long exact prime prefix.
- It is not globally reliable as a prime generator.
- The first composite slip, the first missed prime, and the measured precision/recall all change depending on how long the machine runs.
- This is exactly what one expects from a path-dependent recursive state machine that uses its own evolving state as input, without a hard invariant protecting the stored list.

This makes the system look like a finite-window prime-like generator, not a mathematically stable infinite prime engine.

---

## 2. The core question

The important question is not simply: "Does the machine produce primes?"

The important question is: "Does it preserve the invariant that every stored value is prime and that every prime up to the current range is included?"

The answer, from the evidence, is no.

The machine behaves like a state evolution with local repairs instead of a strict certified prime process.

---

## 3. Testing method

The testing used a trusted primality oracle based on trial division up to sqrt(n). For each run, the final PD list was compared against the true prime set up to the maximum value observed in PD.

The metrics computed were:

- Maximum value in PD
- PD count
- True prime count
a- First false positive (first composite in PD)
- First false negative (first true prime missing from PD)
- False positive count
- False negative count
- Precision = true positives / total PD values
- Recall = true positives / true primes up to max
- Perfect prefix: the largest N such that PD and true primes agree exactly on [2..N]

This is the cleanest direct test of reliability for the state machine.

---

## 4. Verified results: 1000, 10000, and 100000 runs

### 4.1 1000-run summary

- Max value in PD: 991
- PD count: 180
- True primes up to max: 167
- Perfect prefix through: 154
- First false positive: 155
- First false negative: 503
- FP count: 56
- FN count: 43
- Precision: 0.6889
- Recall: 0.7425

### 4.2 10000-run summary

- Max value in PD: 9993
- PD count: 1535
- True primes up to max: 1229
- Perfect prefix through: 390
- First false positive: 391
- First false negative: 5003
- FP count: 680
- FN count: 374
- Precision: 0.5570
- Recall: 0.6957

### 4.3 100000-run summary

- Max value in PD: 99993
- PD count: 14094
- True primes up to max: 9592
- Perfect prefix through: 1926
- First false positive: 1927
- First false negative: 50023
- FP count: 7491
- FN count: 2989
- Precision: 0.4685
- Recall: 0.6884

---

## 5. The most interesting result: the values depend on the run range

This is the most fascinating fact in the whole investigation.

The same machine, under the same logic, produces different first-slip values when the run limit changes:

- 1000 run: first slip at 155
- 10000 run: first slip at 391
- 100000 run: first slip at 1927

Likewise, the first missing prime changes:

- 1000 run: first missed prime at 503
- 10000 run: first missed prime at 5003
- 100000 run: first missed prime at 50023

This is not a small numerical fluctuation. It is a strong sign that the machine is path-dependent.

It means the output is not simply a function of the range endpoint N. It is a function of the entire historical trajectory of PD as the machine evolves.

That is exactly what one expects from a recursive state system with feedback.

---

## 6. Checkpoint table for the 10000 run

| N | PD <= N | True primes <= N | FP | FN | Precision | Recall | First FP <= N | First FN <= N |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 97 | 95 | 2 | 0 | 0.9794 | 1.0000 | 391 | - |
| 1000 | 174 | 168 | 6 | 0 | 0.9655 | 1.0000 | 391 | - |
| 2000 | 325 | 303 | 22 | 0 | 0.9323 | 1.0000 | 391 | - |
| 3000 | 461 | 430 | 31 | 0 | 0.9328 | 1.0000 | 391 | - |
| 4000 | 581 | 550 | 31 | 0 | 0.9466 | 1.0000 | 391 | - |
| 5000 | 700 | 669 | 31 | 0 | 0.9557 | 1.0000 | 391 | - |
| 6000 | 872 | 783 | 160 | 71 | 0.8165 | 0.9093 | 391 | 5003 |
| 7000 | 1057 | 900 | 293 | 136 | 0.7228 | 0.8489 | 391 | 5003 |
| 8000 | 1225 | 1007 | 429 | 211 | 0.6498 | 0.7905 | 391 | 5003 |
| 9000 | 1384 | 1117 | 552 | 285 | 0.6012 | 0.7449 | 391 | 5003 |
| 9993 | 1535 | 1229 | 680 | 374 | 0.5570 | 0.6957 | 391 | 5003 |

This table provides a strong phase picture:

- Stage I: exact agreement for a while
- Stage II: composites begin to appear, but recall still remains 1.0
- Stage III: true primes begin to be skipped and the error rate accelerates rapidly

---

## 7. Checkpoint table for the 100000 run

| N | PD <= N | True primes <= N | FP | FN | Precision | Recall | First FP <= N | First FN <= N |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 500 | 95 | 95 | 0 | 0 | 1.0000 | 1.0000 | - | - |
| 1000 | 168 | 168 | 0 | 0 | 1.0000 | 1.0000 | - | - |
| 2000 | 304 | 303 | 1 | 0 | 0.9967 | 1.0000 | 1927 | - |
| 3000 | 439 | 430 | 9 | 0 | 0.9795 | 1.0000 | 1927 | - |
| 4000 | 583 | 550 | 33 | 0 | 0.9434 | 1.0000 | 1927 | - |
| 5000 | 715 | 669 | 46 | 0 | 0.9357 | 1.0000 | 1927 | - |
| 6000 | 842 | 783 | 59 | 0 | 0.9299 | 1.0000 | 1927 | - |
| 7000 | 983 | 900 | 83 | 0 | 0.9156 | 1.0000 | 1927 | - |
| 8000 | 1118 | 1007 | 111 | 0 | 0.9007 | 1.0000 | 1927 | - |
| 9000 | 1254 | 1117 | 137 | 0 | 0.8907 | 1.0000 | 1927 | - |
| 10000 | 1378 | 1229 | 149 | 0 | 0.8919 | 1.0000 | 1927 | - |
| 20000 | 2542 | 2262 | 280 | 0 | 0.8899 | 1.0000 | 1927 | - |
| 30000 | 3611 | 3245 | 366 | 0 | 0.8986 | 1.0000 | 1927 | - |
| 40000 | 4582 | 4203 | 379 | 0 | 0.9173 | 1.0000 | 1927 | - |
| 50000 | 5512 | 5133 | 379 | 0 | 0.9312 | 1.0000 | 1927 | - |
| 60000 | 7331 | 6057 | 1879 | 605 | 0.7437 | 0.9001 | 1927 | 50023 |
| 70000 | 9149 | 6935 | 3377 | 1163 | 0.6309 | 0.8323 | 1927 | 50023 |
| 80000 | 10898 | 7837 | 4829 | 1768 | 0.5569 | 0.7744 | 1927 | 50023 |
| 90000 | 12553 | 8713 | 6198 | 2358 | 0.5063 | 0.7294 | 1927 | 50023 |
| 99993 | 14094 | 9592 | 7491 | 2989 | 0.4685 | 0.6884 | 1927 | 50023 |

This is very revealing:

- the first false positive appears at 1927,
- but the first missed prime does not appear until 50023,
- recall remains 1.0000 all the way up to that threshold,
- then both forms of failure accelerate together.

This suggests a specific ordering:

1. contamination begins,
2. the state continues to cover all primes for a while,
3. then the feedback loop becomes strong enough to suppress some true primes.

---

## 8. Why the range matters so much

This is the heart of the discovery.

The machine is not simply producing numbers from a fixed rule. It is producing numbers from a state trajectory that depends on the entire history of earlier values.

The key structural drivers are:

- PD is sorted and used as the current state
- the largest current value is used as the feedback term
- the next values are derived from that driver
- candidates are inserted before a strict certification step
- then some local repair logic attempts to compensate for divisibility failures

This means the system is path-dependent. The machine is not evaluating each number in isolation. It is evolving as a dynamical system.

The result is that different run lengths can lead to different failure points, because the trajectory is not the same.

That is the real reason the slip location changes with N.

---

## 9. Exact code-level reasoning

The behavior follows directly from the structure in pd_evolution.py.

### 9.1 The candidate is appended before certification

- Insertion happens first: [pd_evolution.py](pd_evolution.py#L238-L240)
- divisibility testing happens afterward: [pd_evolution.py](pd_evolution.py#L242-L258)

This is extremely important, because it means PD can be polluted before the machine makes a corrected decision.

### 9.2 The driver is always the current tail of PD

- _bPD = PD[-1]: [pd_evolution.py](pd_evolution.py#L265)
- f = _bPD * EN: [pd_evolution.py](pd_evolution.py#L277-L280)

This makes the machine sensitive to the current maximum value in PD, which itself may be composite.

### 9.3 Repair logic is local, not invariant-preserving

Examples:

- division rewrite: [pd_evolution.py](pd_evolution.py#L382-L392)
- alternate rewrite based on f - np2: [pd_evolution.py](pd_evolution.py#L395-L416)
- insertion of rewritten outputs back into PD: [pd_evolution.py](pd_evolution.py#L421-L425)

This means the machine is chasing arithmetic continuity rather than protecting the invariant that PD should stay prime-only.

### 9.4 The machine is state-driven, not theorem-driven

There is no strict proof that every accepted value is prime before it affects later evolution.

Without that proof, the state can steadily drift away from the correct prime set.

---

## 10. Why the errors appear late and then accelerate

The data suggests a three-phase pattern:

1. Early stable phase
   - The state remains close to the true prime set.
   - The machine behaves impressively for a long while.

2. Contamination phase
   - A composite enters the list.
   - It is then used as driver input for later generation.

3. Drift phase
   - False positives begin growing quickly.
   - Eventually false negatives appear.
   - Precision and recall both decline sharply.

This is exactly what a self-referential state machine does when the primary list is not protected by a hard invariant.

---

## 11. The strongest conclusion

The strongest honest conclusion is:

- The machine is not globally reliable as a prime generator.
- It is a path-dependent arithmetic process that can produce a long prime-like run.
- The exact failure point depends on the run history, not just the chosen limit.
- Therefore, the machine is not a stable prime theorem; it is a finite-window heuristic with strong initial behavior and eventual drift.

This does not mean the mechanism is worthless. It means it behaves like an unstable but interesting dynamical system rather than a certified prime-producing law.

---

## 12. What is the most plausible interpretation?

The most likely interpretation is that the machine is exploiting a transient attractor in the state-space of PD.

For a while it stays in a regime that almost perfectly matches the prime set, but eventually that regime is destabilized by contamination entering the state and then feeding back into the next generation of candidates.

The behavior is therefore not random, but neither is it mathematically permanent.

---

## 13. Hypothetical idea: range-by-range reseeding

Although the current machine is not globally reliable, the observation still raises an important possibility:

- run the machine on a trusted finite window,
- keep the verified reliable portion,
- reinsert it as the seed,
- then continue on a new short range,
- then repeat.

This would create a bounded reliable method instead of a free-running state machine.

In other words, instead of letting the machine run indefinitely from its own contaminated state, one could do:

1. trust a finite prefix,
2. run only a short window,
3. revalidate the new output,
4. re-seed with the trusted prefix,
5. repeat.

This is a real engineering pattern. It is not pure self-generation, but it can be far more stable than letting the machine evolve freely.

The cost is that it requires an external correctness boundary: some form of trusted validation or certified seed.

Without that boundary, the same drift is expected to return.

---

## 14. Final opinion

The machine is remarkable because it can look like a prime generator for a surprisingly long time, and it is impressive that the reliable window can be quite large before failure.

But the tests across 1000, 10000, and 100000 show that the reliability is finite and range-sensitive.

So the most honest conclusion is:

- It is not yet a trustworthy infinite prime generator.
- It is a fascinating finite-window prime-like evolution machine.
- It may be exploitable with controlled reseeding, but only as a bounded method, not as a pure self-sustaining proof.

That is the strongest and most accurate way to describe it.

---

## 15. Final short statement

If I had to summarize it in one sentence:

The state machine behaves like a highly promising finite-window prime generator whose apparent reliability is due to a transient state regime, but whose long-term correctness fails because the machine feeds its own contaminated state back into future generation.

That is the real reason the slip point moves with the range.

---

## 16. Suggested next step

The most useful next step would be:

- vary the initial seed or initial trusted prefix,
- test whether a different certified starting point changes the length of the reliable window,
- then test the reseeding model on a short range basis.

This would directly answer whether the apparent “reliable prime generation” can be preserved under controlled boundaries, or whether the system is fundamentally unstable beyond its transient regime.

That would be the most honest way to understand whether the machine has a real working principle or only a very long finite illusion.