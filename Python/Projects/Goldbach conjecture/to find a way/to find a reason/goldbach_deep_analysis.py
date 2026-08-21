# Comprehensive Goldbach Analysis - Anomaly Points Investigation
import math
from decimal import Decimal, getcontext
from collections import defaultdict

getcontext().prec = 500

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

def prime_factors(n):
    """Get prime factors of n"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def count_goldbach_pairs(even_num):
    """Count all Goldbach decompositions of even_num"""
    if even_num % 2 != 0 or even_num < 4:
        return []
    
    pairs = []
    for p1 in range(2, even_num // 2 + 1):
        if is_prime(p1):
            p2 = even_num - p1
            if is_prime(p2):
                pairs.append((p1, p2))
    return pairs

def get_prime_gaps(n):
    """Find prime gaps around n - primes before and after"""
    before = None
    after = None
    
    # Find largest prime <= n
    for i in range(n, 1, -1):
        if is_prime(i):
            before = i
            break
    
    # Find smallest prime > n
    for i in range(n + 1, n + 1000):
        if is_prime(i):
            after = i
            break
    
    if before and after:
        gap = after - before
        return {'before': before, 'after': after, 'gap': gap}
    return None

def next_formula(m, d):
    """Calculate cm based on whether d is odd or even"""
    if d % 2 == 1:
        cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
    else:
        cm = ((2 / 10) * m) - (d * 2 / 10)
    return cm

def calculate_d_precise(m):
    """Calculate d using Decimal for high precision"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

def analyze_goldbach_patterns(anomalies):
    """Deep analysis of Goldbach patterns in anomalies"""
    print("\n" + "="*100)
    print("GOLDBACH DECOMPOSITION ANALYSIS FOR ANOMALY POINTS")
    print("="*100 + "\n")
    
    print("NOTE: Analyzing EVEN anomalies only (odd numbers can't be Goldbach decomposed)\n")
    
    even_anomalies = [m for m in anomalies if m % 2 == 0]
    print(f"Even anomalies: {len(even_anomalies)}/{len(anomalies)}\n")
    
    print(f"{'Number':<8} {'GB Pairs':<10} {'Examples':<50} {'Min Gap':<10} {'Max Gap':<10}")
    print("-" * 90)
    
    all_pair_counts = []
    
    for m in even_anomalies:
        pairs = count_goldbach_pairs(m)
        all_pair_counts.append(len(pairs))
        
        examples = ", ".join([f"{p[0]}+{p[1]}" for p in pairs[:3]])
        if len(pairs) > 3:
            examples += f", ... ({len(pairs)-3} more)"
        
        # Get gap info
        gap_info = get_prime_gaps(m)
        min_gap = gap_info['gap'] if gap_info else 0
        max_gap = min_gap  # For single number context
        
        print(f"{m:<8} {len(pairs):<10} {examples:<50} {min_gap:<10} {max_gap:<10}")
    
    # Statistics
    print("\n" + "-"*90)
    print("GOLDBACH PAIR STATISTICS FOR EVEN ANOMALIES:")
    print(f"  Average pairs per number: {sum(all_pair_counts) / len(all_pair_counts):.2f}")
    print(f"  Min pairs: {min(all_pair_counts)}")
    print(f"  Max pairs: {max(all_pair_counts)}")
    print(f"  Median pairs: {sorted(all_pair_counts)[len(all_pair_counts)//2]}")

def compare_with_regular_multiples(anomalies):
    """Compare anomalies with regular (non-anomaly) multiples of 7"""
    print("\n" + "="*100)
    print("COMPARISON: ANOMALY vs NON-ANOMALY MULTIPLES OF 7")
    print("="*100 + "\n")
    
    anomaly_set = set(anomalies)
    
    # Get non-anomaly even multiples of 7
    non_anomalies = []
    for m in range(14, 5000, 14):  # Step by 14 to get even multiples of 7
        if m not in anomaly_set:
            non_anomalies.append(m)
    
    print("Analyzing prime factor distributions:\n")
    print(f"{'Factor':<10} {'Anomalies %':<20} {'Non-Anomalies %':<20} {'Difference':<15}")
    print("-" * 70)
    
    for factor in [2, 3, 5, 11, 13, 17]:
        anom_count = sum(1 for m in anomalies if m % factor == 0)
        anom_pct = (anom_count / len(anomalies)) * 100 if anomalies else 0
        
        non_anom_count = sum(1 for m in non_anomalies if m % factor == 0)
        non_anom_pct = (non_anom_count / len(non_anomalies)) * 100 if non_anomalies else 0
        
        diff = anom_pct - non_anom_pct
        
        print(f"{factor:<10} {anom_pct:<20.2f} {non_anom_pct:<20.2f} {diff:+.2f}%")
    
    # Goldbach analysis comparison
    print("\n" + "="*100)
    print("GOLDBACH DECOMPOSITION COMPARISON:\n")
    
    even_anomalies = [m for m in anomalies if m % 2 == 0]
    even_non_anomalies = [m for m in non_anomalies if m % 2 == 0][:len(even_anomalies)]
    
    anom_pairs = [len(count_goldbach_pairs(m)) for m in even_anomalies]
    non_anom_pairs = [len(count_goldbach_pairs(m)) for m in even_non_anomalies]
    
    print(f"{'Metric':<40} {'Anomalies':<20} {'Non-Anomalies':<20}")
    print("-" * 80)
    print(f"{'Average Goldbach pairs':<40} {sum(anom_pairs)/len(anom_pairs):<20.2f} {sum(non_anom_pairs)/len(non_anom_pairs):<20.2f}")
    print(f"{'Min Goldbach pairs':<40} {min(anom_pairs):<20} {min(non_anom_pairs):<20}")
    print(f"{'Max Goldbach pairs':<40} {max(anom_pairs):<20} {max(non_anom_pairs):<20}")
    print(f"{'Numbers with 0 pairs':<40} {sum(1 for p in anom_pairs if p == 0):<20} {sum(1 for p in non_anom_pairs if p == 0):<20}")

def analyze_prime_gaps_at_anomalies(anomalies):
    """Analyze prime gaps at anomaly points"""
    print("\n" + "="*100)
    print("PRIME GAP ANALYSIS AT ANOMALY POINTS")
    print("="*100 + "\n")
    
    print(f"{'Number':<8} {'Prime Before':<15} {'Prime After':<15} {'Gap Size':<12} {'Anomaly Type':<15}")
    print("-" * 70)
    
    gaps = []
    odd_anomalies = [m for m in anomalies if m % 2 == 1]
    even_anomalies = [m for m in anomalies if m % 2 == 0]
    
    for m in anomalies[:10]:  # First 10 for display
        gap_info = get_prime_gaps(m)
        if gap_info:
            anom_type = "ODD" if m % 2 == 1 else "EVEN"
            print(f"{m:<8} {gap_info['before']:<15} {gap_info['after']:<15} {gap_info['gap']:<12} {anom_type:<15}")
            gaps.append(gap_info['gap'])
    
    print(f"\n... and {len(anomalies) - 10} more\n")
    print(f"Prime gap statistics:")
    print(f"  Average gap at anomalies (first 10): {sum(gaps)/len(gaps):.2f}")
    print(f"  Min gap: {min(gaps)}")
    print(f"  Max gap: {max(gaps)}")

def analyze_formula_relationship():
    """Analyze relationship between formula value and properties"""
    print("\n" + "="*100)
    print("FORMULA RELATIONSHIP ANALYSIS")
    print("="*100 + "\n")
    
    anomalies = [147, 294, 434, 574, 714, 847, 980, 1120, 1253, 1386, 1519, 1652, 1785, 1918, 2051]
    
    print("Does cm value correlate with number of Goldbach pairs?\n")
    print(f"{'m':<8} {'d':<8} {'cm':<12} {'GB Pairs':<12} {'cm/GB ratio':<15}")
    print("-" * 60)
    
    correlations = []
    
    for m in anomalies:
        d = calculate_d_precise(m)
        cm = next_formula(m, d)
        
        if m % 2 == 0:
            gb_pairs = len(count_goldbach_pairs(m))
        else:
            gb_pairs = 0
        
        ratio = cm / gb_pairs if gb_pairs > 0 else 0
        correlations.append((cm, gb_pairs))
        
        print(f"{m:<8} {d:<8} {cm:<12.4f} {gb_pairs:<12} {ratio:<15.4f}")
    
    # Check correlation
    if len(correlations) > 1:
        cms = [c[0] for c in correlations]
        pairs = [c[1] for c in correlations]
        
        # Simple correlation check
        mean_cm = sum(cms) / len(cms)
        mean_pairs = sum(pairs) / len(pairs)
        
        numerator = sum((cms[i] - mean_cm) * (pairs[i] - mean_pairs) for i in range(len(cms)))
        denom_cm = sum((c - mean_cm)**2 for c in cms) ** 0.5
        denom_pairs = sum((p - mean_pairs)**2 for p in pairs) ** 0.5
        
        if denom_cm * denom_pairs > 0:
            correlation = numerator / (denom_cm * denom_pairs)
            print(f"\nPearson correlation (cm vs GB pairs): {correlation:.4f}")
            if abs(correlation) > 0.3:
                print("  → Moderate to strong correlation detected")
            else:
                print("  → Weak or no correlation")

def main():
    """Main analysis"""
    anomalies = [147, 294, 434, 574, 714, 847, 980, 1120, 1253, 1386, 1519, 1652, 1785, 1918, 2051, 2177, 2310, 2443, 2576, 2709, 2842, 2975, 3101, 3234, 3367, 3500, 3633, 3766, 3892, 4025, 4158, 4291, 4417, 4550, 4683, 4816, 4949]
    
    analyze_goldbach_patterns(anomalies)
    compare_with_regular_multiples(anomalies)
    analyze_prime_gaps_at_anomalies(anomalies)
    analyze_formula_relationship()

if __name__ == "__main__":
    main()
