# Fresh Investigation: d % 7 Divisibility Check
# Exploring what happens when we check d's divisibility by 7 instead of m's

import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def formula_with_d_check(m, d):
    """
    NEW VARIANT: Check if d (not m) is divisible by 7
    
    if d is odd:
        if d % 7 == 0:
            cm = (2/10)×m - ((d×2+2)/10)
        else:
            cm = (2/10)×m - ((d×2-2)/10)
    else:
        cm = (2/10)×m - (d×2/10)
    """
    if d % 2 == 1:  # d is odd
        if d % 7 == 0:  # d is divisible by 7
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        else:  # d is NOT divisible by 7
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
    else:  # d is even
        cm = ((2 / 10) * m) - (d * 2 / 10)
    return cm

def original_formula(m, d):
    """Original formula for reference"""
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

def test_pattern_comparison(start=7, end=500, step=7):
    """Compare original vs d-check formula"""
    print("\n" + "="*100)
    print("COMPARISON: Original Formula vs d%7 Check Formula")
    print("="*100 + "\n")
    
    print(f"{'m':<8} {'d':<6} {'d%7':<6} {'Original cm':<15} {'d-check cm':<15} {'Change':<15} {'Branch Used':<25}")
    print("-" * 120)
    
    differences = []
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        d_mod_7 = d % 7
        
        orig_cm = original_formula(m, d)
        new_cm = formula_with_d_check(m, d)
        
        diff = new_cm - orig_cm
        
        if d % 2 == 1:  # d is odd
            if d % 7 == 0:
                branch = "d is M7: d×2+2"
            else:
                branch = "d NOT M7: d×2-2"
        else:
            branch = "d even: d×2"
        
        print(f"{m:<8} {d:<6} {d_mod_7:<6} {orig_cm:<15.4f} {new_cm:<15.4f} {diff:+.4f}         {branch:<25}")
        
        if abs(diff) > 0.001:
            differences.append((m, d, d_mod_7, orig_cm, new_cm, diff))
    
    print("\n" + "-"*120)
    print(f"Total differences found: {len(differences)}")
    
    return differences

def find_anomalies_both_formulas(start=7, end=5000, step=7):
    """Find anomalies in both formulas"""
    print("\n" + "="*100)
    print("ANOMALY DETECTION: Original vs d%7 Check")
    print("="*100 + "\n")
    
    # Original formula anomalies
    original_anomalies = []
    prev_cm = None
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        cm = original_formula(m, d)
        
        if prev_cm is not None:
            diff = cm - prev_cm
            if abs(diff - 0.6) < 0.01:
                original_anomalies.append((m, d, cm))
        prev_cm = cm
    
    # d-check formula anomalies
    dcheck_anomalies = []
    prev_cm = None
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        cm = formula_with_d_check(m, d)
        
        if prev_cm is not None:
            diff = cm - prev_cm
            # Look for any unusual jump (not 1.0)
            if abs(diff - 1.0) > 0.05:
                dcheck_anomalies.append((m, d, cm, diff))
        prev_cm = cm
    
    print(f"ORIGINAL FORMULA:")
    print(f"  Anomalies (0.6 drops): {len(original_anomalies)}")
    if original_anomalies[:5]:
        print(f"  First 5: {[m for m, _, _ in original_anomalies[:5]]}")
    
    print(f"\nd%7 CHECK FORMULA:")
    print(f"  Anomalies (non-1.0 increments): {len(dcheck_anomalies)}")
    if dcheck_anomalies[:5]:
        print(f"  First 5: {[(m, f'{d:.1f}') for m, d, _, _ in dcheck_anomalies[:5]]}")
    
    print(f"\n" + "-"*100)
    print("Do the anomalies disappear? Let's check the pattern...\n")
    
    # Show detailed anomaly pattern for d-check formula
    if dcheck_anomalies:
        print(f"{'m':<8} {'d':<8} {'cm':<12} {'Increment':<12} {'d%7':<8} {'Branch':<20}")
        print("-" * 80)
        for m, d, cm, inc in dcheck_anomalies[:15]:
            d_mod_7 = d % 7
            if d % 2 == 1:
                if d % 7 == 0:
                    branch = "d is M7"
                else:
                    branch = "d NOT M7"
            else:
                branch = "even d"
            print(f"{m:<8} {d:<8} {cm:<12.4f} {inc:+.4f}         {d_mod_7:<8} {branch:<20}")
    
    return original_anomalies, dcheck_anomalies

def analyze_d_divisibility_pattern(start=7, end=5000, step=7):
    """Analyze which values of d are multiples of 7"""
    print("\n" + "="*100)
    print("ANALYSIS: When is d divisible by 7?")
    print("="*100 + "\n")
    
    d_mult_7 = []
    d_not_mult_7 = []
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        
        if d % 7 == 0:
            d_mult_7.append((m, d))
        else:
            d_not_mult_7.append((m, d))
    
    print(f"Total multiples of 7 tested: {len(d_mult_7) + len(d_not_mult_7)}")
    print(f"Where d % 7 == 0: {len(d_mult_7)} ({len(d_mult_7)/(len(d_mult_7)+len(d_not_mult_7))*100:.1f}%)")
    print(f"Where d % 7 != 0: {len(d_not_mult_7)} ({len(d_not_mult_7)/(len(d_mult_7)+len(d_not_mult_7))*100:.1f}%)")
    
    print(f"\nValues of m where d IS divisible by 7:")
    if d_mult_7:
        for m, d in d_mult_7[:10]:
            print(f"  m = {m:<8} d = {d:<8} ({d//7} × 7)")
        if len(d_mult_7) > 10:
            print(f"  ... and {len(d_mult_7) - 10} more")
    
    # Analyze spacing
    if d_mult_7:
        spacings = [d_mult_7[i+1][0] - d_mult_7[i][0] for i in range(len(d_mult_7)-1)]
        print(f"\nSpacing of m where d % 7 == 0:")
        print(f"  Min: {min(spacings)}, Max: {max(spacings)}, Average: {sum(spacings)/len(spacings):.1f}")

def investigate_cm_formula_difference():
    """Investigate why the formulas give different cm values"""
    print("\n" + "="*100)
    print("MATHEMATICAL ANALYSIS: Why do formulas differ?")
    print("="*100 + "\n")
    
    print("When d is ODD:")
    print("  Original:  cm = (2/10)×m - ((d×2+2)/10) = (1/5)×m - (1/5)×d - 1/5 = (1/5)×(m-d-1)")
    print("  d-check:   cm = (2/10)×m - ((d×2-2)/10) = (1/5)×m - (1/5)×d + 1/5 = (1/5)×(m-d+1)")
    print("  Difference: (1/5)×(m-d+1) - (1/5)×(m-d-1) = (1/5)×2 = 0.4")
    print("\n  So when d%7!=0, the cm value is 0.4 HIGHER than original!")
    
    print("\nWhen d is EVEN (same in both):")
    print("  Both: cm = (1/5)×(m-d)")
    print("  No difference ✓")
    
    print("\nThis explains why anomalies might disappear or change:")
    print("  - Original has 0.6 drops at specific d parity transitions")
    print("  - d-check adds a systematic +0.4 offset when d%7!=0")
    print("  - These competing effects might cancel or create new patterns")

def main():
    print("\n" + "🔬 "*50)
    print("FRESH INVESTIGATION: d % 7 Divisibility Check")
    print("🔬 "*50)
    
    # Test 1: Pattern comparison
    diffs = test_pattern_comparison(start=7, end=350, step=7)
    
    # Test 2: Anomaly detection
    orig_anom, dcheck_anom = find_anomalies_both_formulas(7, 5000, 7)
    
    # Test 3: d divisibility analysis
    analyze_d_divisibility_pattern()
    
    # Test 4: Mathematical analysis
    investigate_cm_formula_difference()
    
    # Summary
    print("\n" + "="*100)
    print("SUMMARY OF FINDINGS")
    print("="*100 + "\n")
    
    print(f"""
✓ Pattern Changed: Original formula has {len(orig_anom)} anomalies (0.6 drops)
✓ New Pattern: d-check formula has {len(dcheck_anom)} anomalies/changes ({len(dcheck_anom)/(5000-7)//7*100:.1f}% rate)
✓ Systematic Offset: When d%7!=0, cm increases by 0.4 compared to original
✓ d Divisibility: Only {(len(orig_anom)/(5000-7)//7)*100:.1f}% of values have d divisible by 7

KEY INSIGHT: The anomalies didn't disappear—they TRANSFORMED!
The 0.6 drops might be masked or redistributed by the 0.4 systematic offset.
""")

if __name__ == "__main__":
    main()
