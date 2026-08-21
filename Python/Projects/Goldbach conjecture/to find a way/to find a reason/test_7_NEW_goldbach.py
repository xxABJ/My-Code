# Goldbach Analysis for 7_NEW.py Formula
import math
from decimal import Decimal, getcontext

getcontext().prec = 500

def next_formula(m, d):
    """Enhanced formula with divisibility-by-7 condition"""
    if d % 2 == 1:
        if m % 7 == 0:
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        else:
            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
    else:
        cm = ((2 / 10) * m) - (d * 2 / 10)
    return cm

def calculate_d_precise(m):
    """Calculate d using Decimal"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

def is_prime(n):
    """Check if n is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_goldbach_pairs(even_num):
    """Count Goldbach decompositions"""
    if even_num % 2 != 0 or even_num < 4:
        return []
    
    pairs = []
    for p1 in range(2, even_num // 2 + 1):
        if is_prime(p1):
            p2 = even_num - p1
            if is_prime(p2):
                pairs.append((p1, p2))
    return pairs

def find_anomalies(start=7, end=5000, step=7):
    """Find anomalies using the new formula"""
    anomalies = []
    prev_cm = None
    
    for m in range(start, end + 1, step):
        d = calculate_d_precise(m)
        cm = next_formula(m, d)
        
        if prev_cm is not None:
            diff = cm - prev_cm
            if abs(diff - 0.6) < 0.01:
                anomalies.append(m)
        
        prev_cm = cm
    
    return anomalies

def analyze_goldbach_for_anomalies(anomalies):
    """Analyze Goldbach properties of anomalies"""
    print("\n" + "="*100)
    print("GOLDBACH ANALYSIS FOR NEW FORMULA ANOMALIES")
    print("="*100 + "\n")
    
    even_anomalies = [m for m in anomalies if m % 2 == 0]
    
    print(f"Total anomalies: {len(anomalies)}")
    print(f"Even anomalies (can have Goldbach): {len(even_anomalies)}")
    print(f"Odd anomalies: {len(anomalies) - len(even_anomalies)}\n")
    
    print(f"{'m':<8} {'GB Pairs':<12} {'Examples':<50}")
    print("-" * 75)
    
    gb_counts = []
    
    for m in even_anomalies:
        pairs = count_goldbach_pairs(m)
        gb_counts.append(len(pairs))
        
        examples = ", ".join([f"{p[0]}+{p[1]}" for p in pairs[:3]])
        if len(pairs) > 3:
            examples += f" ... ({len(pairs)-3} more)"
        
        print(f"{m:<8} {len(pairs):<12} {examples:<50}")
    
    if gb_counts:
        print("\n" + "-"*75)
        print(f"Average Goldbach pairs: {sum(gb_counts) / len(gb_counts):.2f}")
        print(f"Min: {min(gb_counts)}, Max: {max(gb_counts)}, Median: {sorted(gb_counts)[len(gb_counts)//2]}")

def compare_formulas_goldbach():
    """Compare Goldbach richness between old and new formula"""
    print("\n" + "="*100)
    print("COMPARISON: Goldbach Richness (Original vs NEW Formula)")
    print("="*100 + "\n")
    
    # Original formula for comparison
    def original_formula(m, d):
        if d % 2 == 1:
            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        else:
            cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm
    
    # Find anomalies with original formula (multiples of 7 only)
    original_anomalies = []
    prev_cm = None
    
    for m in range(7, 5001, 7):
        d = calculate_d_precise(m)
        cm = original_formula(m, d)
        
        if prev_cm is not None:
            diff = cm - prev_cm
            if abs(diff - 0.6) < 0.01:
                original_anomalies.append(m)
        prev_cm = cm
    
    # Find anomalies with new formula (multiples of 7 only)
    new_anomalies = find_anomalies(7, 5000, 7)
    
    print(f"Original formula anomalies: {len(original_anomalies)}")
    print(f"NEW formula anomalies: {len(new_anomalies)}")
    
    if original_anomalies == new_anomalies:
        print("\n✓ ANOMALIES ARE IDENTICAL!")
        print("The new formula produces the SAME anomaly points as the original.")
        
        # Analyze Goldbach for new formula
        even_anom = [m for m in new_anomalies if m % 2 == 0]
        gb_new = [len(count_goldbach_pairs(m)) for m in even_anom]
        
        print(f"\nGoldbach analysis for these anomalies:")
        print(f"  Average pairs: {sum(gb_new) / len(gb_new):.2f}")
        print(f"  This matches the ORIGINAL investigation!")
    else:
        print(f"\n⚠ ANOMALIES DIFFER!")
        print(f"Different points: {set(original_anomalies) ^ set(new_anomalies)}")

def test_non_multiples():
    """Test how the new formula behaves on non-multiples of 7"""
    print("\n" + "="*100)
    print("SPECIAL TEST: NEW Formula Behavior on Non-Multiples of 7")
    print("="*100 + "\n")
    
    print("Testing numbers that are NOT multiples of 7:")
    print(f"{'m':<8} {'d':<8} {'cm':<12} {'Formula Used':<30} {'Note':<20}")
    print("-" * 90)
    
    count = 0
    for m in range(2, 500, 7):  # Every 7th number starting at 2
        if m % 7 != 0:  # Ensure not multiple of 7
            d = calculate_d_precise(m)
            cm = next_formula(m, d)
            
            if d % 2 == 1:
                formula_used = "odd d, !M7: d×2-2"
            else:
                formula_used = "even d: d×2"
            
            print(f"{m:<8} {d:<8} {cm:<12.4f} {formula_used:<30}")
            count += 1
            if count >= 15:
                break

def main():
    print("\n" + "🔬 "*40)
    print("GOLDBACH ANALYSIS FOR 7_NEW.py")
    print("🔬 "*40)
    
    # Find anomalies
    anomalies = find_anomalies(7, 5000, 7)
    
    # Analyze Goldbach
    analyze_goldbach_for_anomalies(anomalies)
    
    # Compare formulas
    compare_formulas_goldbach()
    
    # Test non-multiples
    test_non_multiples()
    
    print("\n" + "="*100)
    print("KEY FINDINGS")
    print("="*100)
    print(f"""
✓ Anomalies detected: {len(anomalies)}
✓ Formula branch added: divisibility-by-7 check for odd d
✓ Impact on multiples of 7: NONE (formulas equivalent)
✓ Impact on non-multiples of 7: Uses alternative formula (d×2-2 instead of d×2+2)
    
IMPLICATION: The new formula extends to handle non-multiples of 7,
while preserving all Goldbach properties of the original formula
for multiples of 7!
""")

if __name__ == "__main__":
    main()
