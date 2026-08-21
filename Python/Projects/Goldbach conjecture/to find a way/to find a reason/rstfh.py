import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def calculate_d_precise(m):
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

# PURE LINEAR SENSOR: cm = m / 7
def build_table(start=7, end=5000, step=7):
    rows = []
    for m in range(start, end+1, step):
        d = calculate_d_precise(m)   # keep d for display
        cm = m / 7                   # PURE LINEAR SENSOR
        rows.append({"m": m, "d": d, "cm": cm})
    return rows

def print_table(rows):
    print(f"{'m':<8} {'d':<8} {'cm':<12} {'Δ':<8}")
    print("-"*40)
    prev_cm = None
    for r in rows:
        m, d, cm = r["m"], r["d"], r["cm"]
        if prev_cm is None:
            delta = ""
        else:
            delta = f"{cm - prev_cm:.1f}"   # always 1.0
        print(f"{m:<8} {d:<8} {cm:<12.4f} {delta:<8}")
        prev_cm = cm

rows = build_table()
print_table(rows)
