# 7_NEW.py - Comprehensive Test Suite
# Tests the enhanced formula with divisibility-by-7 condition
import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def next_formula(m, d):
    """
    Enhanced formula with divisibility-by-7 condition
    
    if d is (odd & M of 7):      cm = (2/10)×m - ((d×2+2)/10)
    elif d is (odd & !M of 7):   cm = (2/10)×m - ((d×2-2)/10)
    elif d is even:              cm = (2/10)×m - (d×2/10)
    """
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

def test_basic_calculation(m):
    """Test basic calculation for a single m"""
    d = calculate_d_precise(m)
    cm = next_formula(m, d)
    return d, cm

def test_multiples_range(start=7, end=500, step=7, label="Multiples of 7"):
    """Test multiples of a given start value"""
    print(f"\n{'='*80}")
    print(f"TEST: {label} (range {start} to {end}, step {step})")
    print(f"{'='*80}\n")
    
    print(f"{'m':<8} {'d':<8} {'cm':<12} {'m%7':<8} {'d parity':<12} {'Change':<12}")
    print("-" * 80)
    
    anomalies = []
    prev_cm = None
    results = []
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        cm = next_formula(m, d)
        
        m_mod_7 = m % 7
        d_parity = "ODD" if d % 2 == 1 else "EVEN"
        
        change = ""
        if prev_cm is not None:
            diff = cm - prev_cm
            if abs(diff - 1.0) < 0.01:
                change = "+1.0 ✓"
            elif abs(diff - 0.6) < 0.01:
                change = "+0.6 ⚠"
                anomalies.append((m, cm, diff))
            elif abs(diff - 0.8) < 0.01:
                change = "+0.8 ◆"
            else:
                change = f"+{diff:.2f}"
        
        print(f"{m:<8} {d:<8} {cm:<12.4f} {m_mod_7:<8} {d_parity:<12} {change:<12}")
        results.append((m, d, cm, m_mod_7, d_parity))
        prev_cm = cm
    
    print("\n" + "-"*80)
    print(f"Total values tested: {(end - start) // step + 1}")
    print(f"Anomalies (0.6 drops) found: {len(anomalies)}")
    if anomalies:
        print("\nAnomalies:")
        for m, cm, diff in anomalies[:10]:
            print(f"  m = {m:<6} | cm = {cm:<8.4f} | change = {diff:.1f}")
        if len(anomalies) > 10:
            print(f"  ... and {len(anomalies) - 10} more")
    
    return results, anomalies

def test_non_multiples_of_7(start=2, end=500, step=1):
    """Test non-multiples of 7 to see how formula behaves"""
    print(f"\n{'='*80}")
    print(f"TEST: Non-Multiples of 7 (sample: every 7 values, starting at {start})")
    print(f"{'='*80}\n")
    
    print(f"{'m':<8} {'d':<8} {'cm':<12} {'m%7':<8} {'Formula Branch':<25}")
    print("-" * 80)
    
    count = 0
    for m in range(start, min(end, start + 700), 7):
        if m % 7 != 0:  # Only non-multiples
            d = calculate_d_precise(m)
            cm = next_formula(m, d)
            
            if d % 2 == 1 and m % 7 != 0:
                branch = "odd d, !M7: d×2-2"
            elif d % 2 == 1 and m % 7 == 0:
                branch = "odd d, M7: d×2+2"
            else:
                branch = "even d: d×2"
            
            print(f"{m:<8} {d:<8} {cm:<12.4f} {m%7:<8} {branch:<25}")
            count += 1
            if count >= 10:
                break
    
    print(f"\n... (tested up to {min(end, start + 700)})")

def test_formula_branches():
    """Analyze which formula branch is used most often"""
    print(f"\n{'='*80}")
    print(f"TEST: Formula Branch Distribution (m=7 to 5000)")
    print(f"{'='*80}\n")
    
    branches = {
        'even_d': 0,
        'odd_d_m7': 0,
        'odd_d_not_m7': 0
    }
    
    for m in range(7, 5001, 7):
        d = calculate_d_precise(m)
        
        if d % 2 == 0:
            branches['even_d'] += 1
        elif d % 2 == 1 and m % 7 == 0:
            branches['odd_d_m7'] += 1
        else:
            branches['odd_d_not_m7'] += 1
    
    total = sum(branches.values())
    print(f"Even d (d×2 formula):              {branches['even_d']:>4} ({branches['even_d']/total*100:>6.2f}%)")
    print(f"Odd d + M7 (d×2+2 formula):        {branches['odd_d_m7']:>4} ({branches['odd_d_m7']/total*100:>6.2f}%)")
    print(f"Odd d + !M7 (d×2-2 formula):       {branches['odd_d_not_m7']:>4} ({branches['odd_d_not_m7']/total*100:>6.2f}%)")
    print(f"Total: {total}")

def test_difference_from_original():
    """Compare NEW formula against ORIGINAL formula"""
    print(f"\n{'='*80}")
    print(f"TEST: Comparison - NEW vs ORIGINAL Formula")
    print(f"{'='*80}\n")
    
    def original_formula(m, d):
        """Original formula (no divisibility-by-7 check)"""
        if d % 2 == 1:
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        else:
            cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm
    
    print(f"{'m':<8} {'d':<8} {'Original':<15} {'NEW':<15} {'Difference':<15} {'Note':<20}")
    print("-" * 90)
    
    differences = []
    
    for m in range(7, 350, 7):
        d = calculate_d_precise(m)
        original = original_formula(m, d)
        new = next_formula(m, d)
        diff = new - original
        
        note = ""
        if abs(diff) > 0.001:
            note = "DIFFERENCE! ⚠"
            differences.append((m, d, diff))
        
        print(f"{m:<8} {d:<8} {original:<15.4f} {new:<15.4f} {diff:<15.4f} {note:<20}")
    
    print("\n" + "-"*90)
    if differences:
        print(f"FOUND {len(differences)} DIFFERENCES between formulas!")
        print("\nValues where formulas diverge:")
        for m, d, diff in differences[:10]:
            print(f"  m = {m:<6} | d = {d:<4} | difference = {diff:+.4f}")
        if len(differences) > 10:
            print(f"  ... and {len(differences) - 10} more")
    else:
        print("No differences found! Formulas are equivalent for multiples of 7.")

def main():
    """Run all tests"""
    print("\n" + "🔍 "*40)
    print("COMPREHENSIVE TEST SUITE FOR 7_NEW.py")
    print("🔍 "*40)
    
    # Test 1: Multiples of 7 (like original investigation)
    results_m7, anomalies_m7 = test_multiples_range(start=7, end=350, step=7, label="Multiples of 7")
    
    # Test 2: Larger multiples of 7
    results_large, anomalies_large = test_multiples_range(start=7, end=5000, step=7, label="Extended Range - Multiples of 7 (up to 5000)")
    
    # Test 3: Non-multiples of 7
    test_non_multiples_of_7()
    
    # Test 4: Formula branch distribution
    test_formula_branches()
    
    # Test 5: Compare with original
    test_difference_from_original()
    
    # Summary
    print(f"\n{'='*80}")
    print("TEST SUMMARY")
    print(f"{'='*80}\n")
    print(f"Anomalies in range 7-350: {len(anomalies_m7)}")
    print(f"Anomalies in range 7-5000: {len(anomalies_large)}")
    if anomalies_large:
        print(f"\nAnomalies in extended range: {[m for m, _, _ in anomalies_large]}")

if __name__ == "__main__":
    main()
