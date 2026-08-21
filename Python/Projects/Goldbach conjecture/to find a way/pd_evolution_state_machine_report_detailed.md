# State-Machine Investigation Report

Prepared: 21 August 2026

## 1. Executive Summary

This report documents the structure, behavior, and observed failure mode of the original evolution rule in [pd_evolution.py](pd_evolution.py).

The purpose is not to claim a theorem or a finished prime-generation method, but to describe the mechanism as it actually behaves under observation. The main finding is that the process is internally coherent, strongly state-dependent, and recursive, but it is not a valid prime extractor in its present form because composite values are able to survive inside the stored state and then influence future candidate generation.

The conclusion is therefore clear:

- the machine is interesting and structured,
- the state updates are meaningful,
- the reproduction of primes is partially successful,
- but the acceptance rule is not strict enough to preserve a certified prime list.

The reason there is no 100% sieve is that the code never preserves a global invariant of the form

$$
\forall x \in PD,\; x \text{ is prime}.
$$

It performs local checks and partial repairs, but it never enforces a final certificate before insertion. The result is a partial and conditional sieve, not a complete one.

---

## 2. Scope and Context

The file under consideration is the original evolution script. The analysis concerns the mechanism by which it updates a running list $PD$, the current iteration value $ien$, the derived ending number $\_en$, and the generated split values $np1$ and $np2$.

The central question is not whether the script occasionally produces primes. It is whether the system maintains a valid invariant such as:

$$
\forall x \in PD,\; x \text{ is prime.}
$$

The observed behavior through 110 shows that this invariant does not hold.

---

## 3. Core State Variables

The evolution can be modeled as a state machine:

$$
S_k = (PD_k, \mathrm{ien}_k, \mathrm{pairs}_k, \mathrm{pair}_k).
$$

Where:
- $PD_k$ is the current stored list of candidate values,
- $\mathrm{ien}_k$ is the current iteration value,
- $\mathrm{pairs}_k$ records whether a pair branch is active,
- $\mathrm{pair}_k$ holds the pair value when that branch is used.

Additional variables used by the algorithm are:
- $EN = 2$
- $\_bPD_k = \max(PD_k)$ after sorting
- $\_en_k$, the ending-number value derived from $\mathrm{ien}_k$
- $f_k$, the active multiplier/state value
- $np1_k$ and $np2_k$, the split candidates produced from the current state

---

## 4. Mechanism of the Original Update Rule

The broad flow is:

$$
\mathrm{ien}_k \rightarrow \_en_k \rightarrow f_k \rightarrow (np1_k, np2_k) \rightarrow PD_{k+1}.
$$

This is not a standard primality test. It is a recursive, branch-driven arithmetic update that mixes:
- additive split generation,
- divisibility checks against the current $PD$,
- a special 7-branch correction,
- feedback-based rewriting of candidate values,
- and insertion into the same evolving list.

The key structural feature is that the system is state-driven rather than externally certified. It generates candidates from the current state and then tries to repair them adaptively. That is interesting, but it is not the same as proving primeness.

---

## 5. The Most Important Driver: $f$

A central observation is that the value $f$ is state-dependent and not fixed.

In principle, the code uses the current maximum stored value and the active pair state to write:

$$
_bPD_k = \max(PD_k)
$$

and then

$$
 f_k =
\begin{cases}
\mathrm{pair}_k \cdot EN, & \text{if } \mathrm{pairs}_k = \mathrm{True}, \\
\_bPD_k \cdot EN, & \text{if } \mathrm{pairs}_k = \mathrm{False}.
\end{cases}
$$

Since $EN = 2$, this means the machine usually uses twice the strongest value presently in $PD$ as its main driver, unless the pair branch overrides it.

This matters because $f_k$ is not passive. It is the main feedback term that determines the next split, and then that split determines the next accepted values.

---

## 6. The Pair and Correction Branches

The pair branch is not decorative. It can override the usual maximum-based rule and redirect the evolution along a different path. The branch changes the source of $f$, which in turn changes both $np1$ and $np2$.

The machine also contains a special 7-based correction rule. When one side of the generated split reaches a form that matches a 7-pattern, the algorithm modifies the pair by a computed increment. That makes the rule look less like a theorem and more like an internal repair mechanism.

Together, these branches create a system that is flexible, but also difficult to certify formally.

---

## 7. The Divisibility Feedback Loop

The generated split is not accepted automatically. Instead, the code checks whether either part is divisible by an existing value in $PD$.

If one part is composite relative to that list, it is rewritten by a divisor-based correction. In practical terms, this means:

- the machine keeps trying to make its candidate fit the current state,
- it does not only reject invalid values,
- it actively reshapes them and re-inserts them.

This is a very strong sign that the algorithm is using state repair, not a strict primality certificate.

---

## 8. Result Through 110

Running the same logic through 110 yields the final stored list:

$$
PD = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61, 63, 65, 69, 75, 79, 83, 85, 95, 101, 107].
$$

The values that survived into the list are:

| Value | Status | Observation |
|---|---|---|
| 61 | prime | accepted |
| 63 | composite | survived |
| 65 | composite | survived |
| 69 | composite | survived |
| 75 | composite | survived |
| 79 | prime | accepted |
| 83 | prime | accepted |
| 85 | composite | survived |
| 95 | composite | survived |
| 101 | prime | accepted |
| 107 | prime | accepted |

This is the basic failure. The machine can generate primes, but it does not maintain the invariant that every stored member is prime.

At larger cutoffs, the final PD does not become prime-only. The observed survivors include values such as 51, 111, 123, 125, 129, 135, 145, 161, 165, 171, and 187, and the composite rate remains around 24 percent in the runs that were checked.

---

## 9. Why It Fails

The original mechanism fails for three connected reasons.

### 9.1 The correction is local, not global

The divisibility feedback repairs the current split, but it does not impose a permanent exclusion rule over all future evolution. A composite can be rewritten once and then still affect later states because it remains in a structurally active position inside $PD$.

### 9.2 The list $PD$ is not protected by a certificate

A candidate can be inserted before the system has established that it is genuinely prime. Once inside the list, it becomes part of the next state and therefore influences later outputs.

### 9.3 The update rule preserves balance, not primality

The machine is tuned to maintain internal arithmetic coherence, not to guarantee prime membership. Balance is therefore not the same as correctness.

This is why the output remains only partially sieved: some values are correctly filtered, but many survive in the state, and the composite fraction stays nonzero.

### 9.4 The invariant is missing

There is no maintained rule that says every stored value must be prime. Without that invariant, the process cannot become a full sieve, no matter how many local divisibility checks are added.

---

## 10. Do the Surviving Composites Change Future Candidate Generation?

Yes — absolutely.

This is the most important consequence of the failure.

The update logic does the following:

1. sorts the current list,
2. sets $\_bPD = PD[-1]$,
3. computes $f = \_bPD \cdot EN$ or uses the pair branch,
4. generates $np1$ and $np2$ from that driver.

So if a composite remains in the list and becomes the largest value in $PD$, then it changes the next value of $\_bPD$, and therefore changes the next value of $f$ and the next split.

In other words, the surviving composite is not merely a harmless extra value. It is a causal input to later candidate construction.

### Concrete example

At the point where the run reaches a branch with $np1 = 5$ and $np2 = 63$, the value $63$ is not rejected as a permanent error. It remains part of the active state and becomes the driver that informs subsequent updates.

That means the machine is feeding its own future state with a non-prime value. Once that happens, the evolution is no longer a clean prime-producing rule; it is a self-referential arithmetic process that can drift away from primality.

---

## 11. What This Means in Practice

The file is not “wrong” in the sense of being totally random. It is structurally meaningful and recognizably state-based. But it is not a reliable prime generator because it does not maintain the invariant that every accepted value is prime.

In practical terms, the script behaves like a custom arithmetic evolution with local repair steps rather than a certificate-checked prime theorem.

---

## 12. Suggestions and Future Directions

### 12.1 Most important fix

If the goal is to keep the same style but guarantee correctness, then the accepted element must be checked before being inserted into $PD$.

A good rule would be:

$$
\text{insert } x \text{ into } PD \quad \Longleftrightarrow \quad \mathrm{isPrime}(x) = \mathrm{True}.
$$

This should be enforced as a final gate, not just as a side repair after the fact.

The failed broad-divisibility experiment confirms why this matters: the machine is feeding contaminated state back into itself, so a gate that is too broad can either leave composites behind or suppress the evolution entirely. That is why the fix must be a genuine certificate check rather than a loose rejection rule.

### 12.2 Separate state evolution from certification

The current scheme mixes two roles at once:
- generating candidates from the evolving state,
- and deciding whether those candidates are legitimate primes.

These should be separated.

A cleaner structure would be:

1. generate candidate,
2. test candidate against a primality certificate,
3. only then update $PD$.

### 12.3 Keep a rejected buffer

Instead of letting a failed candidate influence the main state, it could be placed into a secondary rejected list. That would prevent the main list from being polluted by values that are not valid primes.

### 12.4 Preserve the recursive structure, but tighten the invariant

The dynamic behavior is worth keeping. The real issue is not the recursion itself. The issue is that the recursion is not constrained by a hard proof condition. A better version would preserve the state-driven style while enforcing primality as an invariant.

### 12.5 Future mathematical direction

If the goal is to push this further, the next step should be to define an explicit certificate function:

$$
C(x, PD) = \text{True if } x \text{ is accepted as prime given the current certified state}.
$$

Then the update rule becomes:

$$
PD_{k+1} = PD_k \cup \{x_k\} \quad \text{only if} \quad C(x_k, PD_k).
$$

This would preserve the spirit of the state machine while making the process mathematically defensible.

---

## 13. Final Assessment

The original mechanism is interesting and structurally rich, but it is not a valid prime extractor as currently written.

Its strengths are:
- recursive state updates,
- nontrivial pair logic,
- a meaningful dependence on the previous maximum state,
- and a clear, formula-driven evolution structure.

Its weakness is more important:
- the accepted state is not protected by a strict primality certificate,
- composite values can survive and feed later updates,
- therefore the future candidate generation is causally affected by non-prime entries.

The practical conclusion is simple:

The current system behaves like a custom arithmetic evolution with repair rules, not a guaranteed prime-producing theorem.

If the goal is to keep the style but make it valid, then the next version must separate evolution from certification and enforce a strict prime gate before anything is inserted into $PD$.

In the clearest form, the lesson is this: the machine is interesting, but it is not prime-safe because it mixes candidate generation with state mutation. A broad divisibility gate is not enough on its own; it either misses composites or over-restricts the loop. The correct remedy is to certify each candidate before insertion.

In short: this is a partial sieve with local repair, not a complete sieve with a preserved prime invariant.
