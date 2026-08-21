import math
from decimal import Decimal, getcontext

getcontext().prec = 500


def calculate_d_precise(m):
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d


def original_formula(m, d):
    if d % 2 == 1:
        return ((2 / 10) * m) - ((d * 2 + 2) / 10)
    return ((2 / 10) * m) - (d * 2 / 10)


def next_formula(m, d):
    """
    Intended rule:
    d in 1..7 -> minus
    d in 8..14 -> plus
    d in 15..21 -> minus
    d in 22..28 -> plus
    etc.

    That is exactly the parity of floor(d / 7):
        if (d // 7) % 2 == 0 -> use minus
        else -> use plus
    """
    if d % 2 == 1:
        band = d // 7
        if band % 2 == 0:
            return ((2 / 10) * m) - ((d * 2 - 2) / 10)
        return ((2 / 10) * m) - ((d * 2 + 2) / 10)
    return ((2 / 10) * m) - (d * 2 / 10)


def compare_multiples(start=7, end=5000, step=7):
    orig_anomalies = []
    new_anomalies = []
    prev_orig = prev_new = None

    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        orig = original_formula(m, d)
        new = next_formula(m, d)

        if prev_orig is not None:
            if abs((orig - prev_orig) - 0.6) < 1e-9:
                orig_anomalies.append(m)
            if abs((new - prev_new) - 0.6) < 1e-9:
                new_anomalies.append(m)

        prev_orig = orig
        prev_new = new

    print(f"Original anomalies: {len(orig_anomalies)}")
    print(orig_anomalies[:20])
    print(f"Band-based anomalies: {len(new_anomalies)}")
    print(new_anomalies[:20])
    print(f"Overlap: {len(set(orig_anomalies) & set(new_anomalies))}")

    diff_points = []
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        if abs(original_formula(m, d) - next_formula(m, d)) > 1e-9:
            diff_points.append(m)
    print(f"Different value count: {len(diff_points)}")
    print(diff_points[:20])


if __name__ == "__main__":
    m = 42
    d = calculate_d_precise(m)
    print(f"m={m}, d={d}")
    print(f"original: {original_formula(m, d)}")
    print(f"banded:   {next_formula(m, d)}")
    compare_multiples()