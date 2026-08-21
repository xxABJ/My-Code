from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def level(n):
    if n < 0:
        return 0
    start = 0
    L = 1
    pattern = [6, 4]
    i = 0
    while True:
        block = pattern[i % len(pattern)]
        end = start + block - 1
        if start <= n <= end:
            return L
        start = end + 1
        L += 1
        i += 1


def pick_expression_for_level(n, target_level):
    """Pick one prime-additive expression with exactly target_level terms whenever possible.
    This matches your intended rule: level == number of prime addends in the representation.
    """
    if n < 0:
        return None
    if n == 0:
        return "0"
    if target_level == 1:
        if is_prime(n):
            return str(n)
        if n == 4:
            return "2 + 2"
        return None

    # Try to find a sum of exactly target_level primes.
    # Repetition is allowed, because the model is additive and reusable.
    # Generate the prime pool up to n so the table works all the way to 120.
    primes = [candidate for candidate in range(2, n + 1) if is_prime(candidate)]

    def build(target, remaining_terms, start_index=0, current=None):
        if current is None:
            current = []
        if remaining_terms == 1:
            if target in primes and target >= 2:
                return current + [target]
            return None
        for p in primes[start_index:]:
            if p > target:
                break
            if p < 2:
                continue
            rest = target - p
            if rest < 0:
                continue
            if rest == 0 and remaining_terms > 1:
                continue
            result = build(rest, remaining_terms - 1, start_index, current + [p])
            if result is not None:
                return result
        return None

    result = build(n, target_level)
    if result is not None:
        return " + ".join(map(str, result))

    return None


print("Level-matched prime-additive table, up to 120")
print("=" * 80)
print("Number | Level | Expression")
print("-------|-------|-----------")
for n in range(0, 121):
    L = level(n)
    expr = pick_expression_for_level(n, L)
    print(f"{n:>6} | {L:>5} | {expr if expr is not None else 'no match'}")
