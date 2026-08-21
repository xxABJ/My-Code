# Fixed Analysis of Latest 7_NEW.py with Bug Fix

import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def latest_formula_fixed(m, d):
    """
    Latest 7_NEW.py formula - FIXED VERSION
    The bug: (d/7) % 2 fails when d is not divisible by 7
    """
    if d % 2 == 1:  # d is odd
        # Check parity of d/7 (whether d/7 is odd or even integer)
        d_div_7_parity = int(d) % 7  # Get remainder when d is divided by 7
        d_is_div_7_odd = (d // 7) % 2 == 1 if d % 7 == 0 else (int(d/7)) % 2 == 1
        
        if m % 7 == 0 and d_is_div_7_odd:
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm
        elif m % 7 == 0 and not d_is_div_7_odd:
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm
        elif m % 7 != 0 and d_is_div_7_odd:
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm
        elif m % 7 != 0 and not d_is_div_7_odd:
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm
    else:  # d is even
        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

def original_formula(m, d):
    """Original formula"""
    if d % 2 == 1:
        cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
    else:
        cm = ((2 / 10) * m) - (d * 2 / 10)
    return cm

def calculate_d_precise(m):
    """Calculate d"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

print("\n" + "⚠️ "*50)
print("CRITICAL ISSUE FOUND IN LATEST 7_NEW.py")
print("⚠️ "*50 + "\n")

print("="*100)
print("THE BUG")
print("="*100 + "\n")

print("""
The formula uses: (d / 7) % 2

This has a FATAL FLAW:
- When d is divisible by 7:  d/7 is an integer, (d/7) % 2 works fine
- When d is NOT divisible by 7:  d/7 is a decimal, (d/7) % 2 gives WRONG results

Example:
  d = 21 → d/7 = 3.0 → (3.0) % 2 ≈ 1.0 ✓ (works, but unreliable)
  d = 5  → d/7 = 0.714... → (0.714) % 2 ≈ 0.714 ✗ (meaningless)
  d = 43 → d/7 = 6.14... → (6.14) % 2 ≈ 0.14 ✗ (meaningless)

Result: The formula returns None or produces wrong values for most inputs!
""")

# Test a few values to show the problem
print("="*100)
print("DEMONSTRATING THE BUG")
print("="*100 + "\n")

print(f"{'m':<8} {'d':<8} {'d divisible by 7?':<20} {'d/7 value':<15} {'(d/7)%2 result':<15} {'Problem?':<15}")
print("-" * 90)

test_values = [7, 14, 21, 28, 35, 42, 49, 147, 154, 161]

for m in test_values:
    d = calculate_d_precise(m)
    is_div = "YES" if d % 7 == 0 else "NO"
    d_div_7 = d / 7
    d_div_7_mod = (d / 7) % 2
    
    problem = "✗ WRONG" if d % 7 != 0 else "✓ OK"
    
    print(f"{m:<8} {d:<8} {is_div:<20} {d_div_7:<15.4f} {d_div_7_mod:<15.4f} {problem:<15}")

print("\n" + "="*100)
print("WHAT THE FORMULA PROBABLY INTENDED")
print("="*100 + "\n")

print("""
The formula probably meant to check:
  (d // 7) % 2  instead of  (d / 7) % 2

This would check whether d/7 is odd or even WHEN d IS divisible by 7.
But this creates a new problem: what happens when d is NOT divisible by 7?

The formula is incomplete!
""")

print("\n" + "="*100)
print("QUESTIONS FOR YOU")
print("="*100 + "\n")

print("""
1. Did you intend to check (d // 7) % 2 instead of (d / 7) % 2?
   
2. Should the formula handle cases where d is NOT divisible by 7?
   
3. What should happen when d is odd but not divisible by 7?
   - Use (d×2-2) formula?
   - Use (d×2+2) formula?
   - Something else?

4. Is this a work-in-progress or a finished formula?
""")

print("\n" + "="*100)
print("RECOMMENDATION")
print("="*100 + "\n")

print("""
Before testing anomalies, you need to:

1. Clarify the logic for when d is NOT divisible by 7
2. Use integer division: (d // 7) % 2 instead of (d / 7) % 2
3. Add an else clause for the case when d is odd but d%7!=0
4. Test with specific examples to verify the intended behavior

Would you like me to:
a) Fix the formula based on best guess?
b) Wait for your clarification on the intended logic?
c) Test multiple interpretations?
""")
