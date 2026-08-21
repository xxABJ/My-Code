# Detailed Analysis of the Latest 7_NEW.py
# This version uses DUAL divisibility checks: m%7 AND d%7

import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def latest_formula(m, d):
    """
    Latest 7_NEW.py formula with dual divisibility checks
    
    Checks BOTH: m % 7 (original number) AND (d/7) % 2 (parity of d/7)
    """
    if d % 2 == 1:  # d is odd
        if m % 7 == 0 and (d / 7) % 2 == 1:
            # m is M7 AND d/7 is odd
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm
        
        elif m % 7 == 0 and (d / 7) % 2 == 0:
            # m is M7 AND d/7 is even
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm
        
        elif m % 7 != 0 and (d / 7) % 2 == 1:
            # m is NOT M7 AND d/7 is odd
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm
        
        elif m % 7 != 0 and (d / 7) % 2 == 0:
            # m is NOT M7 AND d/7 is even
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm
    
    else:  # d is even
        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

def original_formula(m, d):
    """Original formula for comparison"""
    if d % 2 == 1:
        cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
    else:
        cm = ((2 / 10) * m) - (d * 2 / 10)
    return cm

def calculate_d_precise(m):
    """Calculate d using Decimal"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

print("\n" + "🔍 "*50)
print("DETAILED ANALYSIS: Latest 7_NEW.py Formula")
print("🔍 "*50 + "\n")

# Test 1: Show the formula logic
print("="*100)
print("FORMULA LOGIC BREAKDOWN")
print("="*100 + "\n")

print("When d is ODD, the formula has 4 branches based on TWO conditions:")
print("  Condition 1: Is m divisible by 7? (m % 7 == 0)")
print("  Condition 2: Is (d/7) odd or even? ((d/7) % 2)")
print("\nThis creates a 2×2 matrix:\n")

print(f"{'Condition':<35} {'Formula Used':<35}")
print("-" * 75)
print(f"{'m%7==0 AND (d/7)%2==1 (ODD)':<35} {'(d×2-2) formula':<35}")
print(f"{'m%7==0 AND (d/7)%2==0 (EVEN)':<35} {'(d×2+2) formula':<35}")
print(f"{'m%7!=0 AND (d/7)%2==1 (ODD)':<35} {'(d×2-2) formula':<35}")
print(f"{'m%7!=0 AND (d/7)%2==0 (EVEN)':<35} {'(d×2+2) formula':<35}")

# Test 2: Comparison table
print("\n" + "="*100)
print("DETAILED COMPARISON: Original vs Latest Formula")
print("="*100 + "\n")

print(f"{'m':<8} {'d':<8} {'m%7':<6} {'d/7':<6} {'(d/7)%2':<10} {'Original':<12} {'Latest':<12} {'Diff':<12} {'Branch':<20}")
print("-" * 110)

differences = []

for m in range(7, 351, 7):
    d = calculate_d_precise(m)
    
    orig = original_formula(m, d)
    latest = latest_formula(m, d)
    diff = latest - orig
    
    m_mod_7 = "M7" if m % 7 == 0 else "!M7"
    d_div_7 = d / 7 if d % 7 == 0 else "N/A"
    d_div_7_parity = "ODD" if (d / 7) % 2 == 1 else "EVEN"
    
    # Determine branch
    if d % 2 == 1:
        if m % 7 == 0 and (d / 7) % 2 == 1:
            branch = "M7 + d/7 odd"
        elif m % 7 == 0 and (d / 7) % 2 == 0:
            branch = "M7 + d/7 even"
        elif m % 7 != 0 and (d / 7) % 2 == 1:
            branch = "!M7 + d/7 odd"
        else:
            branch = "!M7 + d/7 even"
    else:
        branch = "d is even"
    
    print(f"{m:<8} {d:<8} {m_mod_7:<6} {d_div_7 if isinstance(d_div_7, str) else f'{d_div_7:.1f}':<6} {d_div_7_parity:<10} {orig:<12.4f} {latest:<12.4f} {diff:+.4f}         {branch:<20}")
    
    if abs(diff) > 0.001:
        differences.append((m, d, orig, latest, diff))

print("\n" + "-"*110)
print(f"Total differences found: {len(differences)}")

if differences:
    print("\nPoints where formulas differ:")
    for m, d, orig, latest, diff in differences[:10]:
        print(f"  m={m:<6} d={d:<6} orig={orig:.4f} latest={latest:.4f} diff={diff:+.4f}")
    if len(differences) > 10:
        print(f"  ... and {len(differences)-10} more")

# Test 3: Anomaly detection
print("\n" + "="*100)
print("ANOMALY DETECTION IN LATEST FORMULA")
print("="*100 + "\n")

anomalies_latest = []
prev_cm = None

print(f"{'m':<8} {'d':<8} {'cm':<12} {'Increment':<12} {'Status':<20}")
print("-" * 60)

for m in range(7, 1001, 7):
    d = calculate_d_precise(m)
    cm = latest_formula(m, d)
    
    if prev_cm is not None:
        increment = cm - prev_cm
        
        status = ""
        if abs(increment - 1.0) < 0.01:
            status = "Normal ✓"
        elif abs(increment - 0.6) < 0.01:
            status = "0.6 drop ⚠"
            anomalies_latest.append((m, d, cm, increment))
        else:
            status = f"Unusual ({increment:.1f})"
            if abs(increment - 1.0) > 0.05:
                anomalies_latest.append((m, d, cm, increment))
        
        if m <= 350 or (len(anomalies_latest) > 0 and m == anomalies_latest[-1][0]):
            print(f"{m:<8} {d:<8} {cm:<12.4f} {increment:+.4f}         {status:<20}")
        
        prev_cm = cm

print(f"\n... (continuing to 5000)\n")
print(f"Anomalies found in latest formula: {len(anomalies_latest)}")

if anomalies_latest:
    print("\nAnomalies list (first 20):")
    for m, d, cm, inc in anomalies_latest[:20]:
        print(f"  m={m:<6} d={d:<6} cm={cm:.4f} increment={inc:+.4f}")

# Test 4: Full range analysis
print("\n" + "="*100)
print("FULL RANGE ANALYSIS (7 to 5000)")
print("="*100 + "\n")

orig_anomalies = []
latest_anomalies = []
prev_orig = None
prev_latest = None

for m in range(7, 5001, 7):
    d = calculate_d_precise(m)
    
    orig = original_formula(m, d)
    latest = latest_formula(m, d)
    
    if prev_orig is not None:
        orig_inc = orig - prev_orig
        latest_inc = latest - prev_latest
        
        if abs(orig_inc - 0.6) < 0.01:
            orig_anomalies.append((m, orig_inc))
        if abs(latest_inc - 0.6) < 0.01:
            latest_anomalies.append((m, latest_inc))
    
    prev_orig = orig
    prev_latest = latest

print(f"Original formula (0.6 drops):     {len(orig_anomalies)} anomalies")
print(f"Latest formula (0.6 drops):       {len(latest_anomalies)} anomalies")

if orig_anomalies and latest_anomalies:
    orig_set = set(m for m, _ in orig_anomalies)
    latest_set = set(m for m, _ in latest_anomalies)
    
    overlap = orig_set & latest_set
    only_orig = orig_set - latest_set
    only_latest = latest_set - orig_set
    
    print(f"\nComparison:")
    print(f"  Anomalies in both: {len(overlap)}")
    print(f"  Only in original: {len(only_orig)}")
    print(f"  Only in latest: {len(only_latest)}")
    
    if overlap:
        print(f"\n  Shared anomalies: {sorted(list(overlap))[:10]}...")
    if only_orig:
        print(f"\n  Lost in latest: {sorted(list(only_orig))[:10]}...")
    if only_latest:
        print(f"\n  New in latest: {sorted(list(only_latest))[:10]}...")

# Test 5: Analyze the (d/7)%2 condition
print("\n" + "="*100)
print("ANALYSIS: The (d/7)%2 Condition")
print("="*100 + "\n")

d_div_7_odd_count = 0
d_div_7_even_count = 0

print(f"{'m':<8} {'d':<8} {'d/7':<10} {'(d/7)%2':<12} {'Freq':<8}")
print("-" * 50)

freq_map = {}

for m in range(7, 5001, 7):
    d = calculate_d_precise(m)
    d_div_7_val = d / 7
    d_div_7_parity = (d / 7) % 2
    
    if d_div_7_parity == 1:
        d_div_7_odd_count += 1
    else:
        d_div_7_even_count += 1
    
    key = "ODD" if d_div_7_parity == 1 else "EVEN"
    freq_map[key] = freq_map.get(key, 0) + 1

total = d_div_7_odd_count + d_div_7_even_count

print(f"(d/7) % 2 == 1 (ODD):  {d_div_7_odd_count:>4} ({d_div_7_odd_count/total*100:>6.2f}%)")
print(f"(d/7) % 2 == 0 (EVEN): {d_div_7_even_count:>4} ({d_div_7_even_count/total*100:>6.2f}%)")

# Test 6: Summary
print("\n" + "="*100)
print("SUMMARY & KEY FINDINGS")
print("="*100 + "\n")

print(f"""
✓ New Approach: Adding (d/7)%2 as a second parity check
✓ Original anomalies (0.6 drops): {len(orig_anomalies)}
✓ Latest anomalies (0.6 drops): {len(latest_anomalies)}
✓ (d/7) is odd: {d_div_7_odd_count} times (~{d_div_7_odd_count/total*100:.1f}%)
✓ (d/7) is even: {d_div_7_even_count} times (~{d_div_7_even_count/total*100:.1f}%)

KEY QUESTION: Does the (d/7)%2 parity condition
              change the anomaly pattern in a meaningful way?
""")
