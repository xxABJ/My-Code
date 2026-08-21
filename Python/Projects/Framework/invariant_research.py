from fractions import Fraction
from math import factorial


def FS_(a, b, c, p):
    fs = Fraction(1, 1)
    for k in range(p, 0, -1):
        fs *= Fraction(a * b * c, k)
    return fs


def Q3_(fs):
    return fs


def Fi_(ta, ti, an):
    if ti > 0:
        return ti * an
    return abs(ti)


def indsum_(fi, an, ta, p):
    # Mirrors the current model behavior while keeping exact arithmetic.
    numerator = Fraction(ta, fi * an)
    denominator = numerator * p + numerator
    if numerator == 0 or denominator == 0:
        return Fraction(0, 1)
    return numerator / denominator


def I1_(p):
    return sum((p + 1) - k for k in range(0, p + 1))


def BNS_(p):
    return [Fraction(k, 10) for k in range(1, p + 2)]


def B2_(fs, bns, indsum, i1_minus_1):
    return [fs * indsum * i1_minus_1 * bn for bn in bns]


def S6_(q3, b2_total):
    if b2_total == 0:
        return Fraction(0, 1)
    return q3 / b2_total


def PF_(s6, an):
    if s6 == 0:
        return Fraction(0, 1)
    if s6 == 1:
        return Fraction(s6, 10) * an
    if s6 > 1:
        return Fraction(s6, 10) - Fraction(s6, 100)
    return Fraction(1, 1)


def SPF_(p):
    if p == 0:
        return Fraction(0, 1)
    return Fraction(p, 2)


def R_(q3, s6, i1, spf, an):
    # Else-only form, as requested in current research path.
    return q3 * s6 * i1 * spf


def C1_(i1, i1_minus_1):
    if i1 == 0 or i1_minus_1 == 0:
        return Fraction(0, 1)
    return Fraction(i1 * i1, i1_minus_1)


def run_model(p, a, b, c, an):
    fs = FS_(a, b, c, p)
    q3 = Q3_(fs)

    ta = an * p
    i = a * b
    ti = ta - i

    fi = Fi_(ta, ti, an)
    indsum = indsum_(fi, an, ta, p)

    i1 = I1_(p)
    i1_minus_1 = i1 - 1

    b2_total = sum(B2_(fs, BNS_(p), indsum, i1_minus_1), Fraction(0, 1))
    s6 = S6_(q3, b2_total)

    pf = PF_(s6, an)
    spf = SPF_(p)
    r = R_(q3, s6, i1, spf, an)
    c1 = C1_(i1, i1_minus_1)

    f0 = r * pf - c1
    f1 = Fraction(0, 1) if i1 == 0 else f0 / i1
    f2 = f1 * i1_minus_1
    f3 = f2 + i1

    expected = Fraction((a * b * c) ** p, 1)

    inv_f3 = f3 / expected if expected != 0 else Fraction(0, 1)
    inv_b2 = b2_total / fs if fs != 0 else Fraction(0, 1)

    denom_r = q3 * s6 * i1
    inv_r = None if denom_r == 0 else r / denom_r

    return {
        "p": p,
        "ti": ti,
        "fi": fi,
        "spf": spf,
        "indsum": indsum,
        "s6": s6,
        "f3": f3,
        "expected": expected,
        "inv_f3": inv_f3,
        "inv_b2": inv_b2,
        "inv_r": inv_r,
    }


def fmt(frac):
    if frac is None:
        return "nan"
    if isinstance(frac, Fraction):
        return f"{frac.numerator}/{frac.denominator} ({float(frac):.12g})"
    return str(frac)


def main():
    a, b, c, an = 3, 5, 6, 4
    rows = [run_model(p, a, b, c, an) for p in range(0, 31)]

    print("Invariant scan for p=0..30")
    print("Columns: p, Ti, Fi, inv_f3=f3/(abc)^p, inv_b2=B2_total/FS, inv_r=R/(Q3*S6*I1)")
    print()

    for row in rows:
        print(
            f"p={row['p']:2d} | Ti={row['ti']:3d} | Fi={row['fi']:3d} | "
            f"inv_f3={fmt(row['inv_f3'])} | inv_b2={fmt(row['inv_b2'])} | inv_r={fmt(row['inv_r'])}"
        )

    first_break = next((row["p"] for row in rows if row["inv_f3"] != 1), None)

    print("\nBreakpoint findings")
    print(f"first p where inv_f3 != 1: {first_break}")

    # Candidate exact laws from observed structure.
    law_inv_b2_ok = all(
        row["inv_b2"] == Fraction(row["p"] * (row["p"] + 2) * (row["p"] + 3), 40)
        for row in rows
    )

    law_inv_r_ok = all(
        (row["p"] == 0 and row["inv_r"] is None) or
        (row["p"] > 0 and row["inv_r"] == Fraction(row["p"], 2))
        for row in rows
    )

    law_inv_f3_piecewise_ok = all(
        (row["p"] <= 3 and row["inv_f3"] == 1) or
        (row["p"] >= 4 and row["inv_f3"] == Fraction(10 * row["p"], factorial(row["p"]) * (row["p"] + 2)))
        for row in rows
    )

    print("\nExact-law checks")
    print(f"inv_b2 == p(p+2)(p+3)/40 for all p: {law_inv_b2_ok}")
    print(f"inv_r == p/2 for p>0 (undefined at p=0): {law_inv_r_ok}")
    print(f"inv_f3 piecewise law holds exactly: {law_inv_f3_piecewise_ok}")


if __name__ == "__main__":
    main()
