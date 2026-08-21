# Display results from 7_NEW.py in table format
import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def next_formula(m, d):
    """Enhanced formula with divisibility-by-7 condition"""
    if d % 2 == 1:  # d is odd
        if m % 7 == 0:  # m is multiple of 7
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm
        else:  # m is NOT multiple of 7
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm
    else:  # d is even
        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

def calculate_d_precise(m):
    """Calculate d using Decimal for high precision"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

# Display table
print("7_NEW.py - Enhanced Formula Results\n")
print(f"{'Multiple':<12} {'d (decimal places)':<20} {'cm (result)':<15}")
print("-" * 50)

for m in range(7, 1001, 7):
    d = calculate_d_precise(m)
    cm = next_formula(m, d)
    print(f"{m:<12} {d:<20} {cm:<15.4f}")

print("\n... continuing to 5000 (showing every 7th multiple)\n")
print(f"{'Multiple':<12} {'d (decimal places)':<20} {'cm (result)':<15}")
print("-" * 50)

for m in range(1001, 5001, 7*10):  # Every 70 to avoid spam
    d = calculate_d_precise(m)
    cm = next_formula(m, d)
    print(f"{m:<12} {d:<20} {cm:<15.4f}")
