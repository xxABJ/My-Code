# to find a CM of a multiple of seven - with ANOMALY ANALYSIS
import math
from decimal import Decimal, getcontext

# Set precision high enough for large numbers
getcontext().prec = 500

def next_formula(m, d):
    """Calculate cm based on whether d is odd or even"""
    if d % 2 == 1:
        cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        return cm
    else:
        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

def calculate_d_precise(m):
    """Calculate d using Decimal for high precision"""
    formula = Decimal(m) / (Decimal(2) ** m)
    log_formula = formula.ln() / Decimal(10).ln()
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

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

def goldbach_decomposition(even_num):
    """Find a Goldbach decomposition (two primes that sum to even_num)"""
    if even_num % 2 != 0:
        return None
    
    for p1 in range(2, even_num // 2 + 1):
        if is_prime(p1):
            p2 = even_num - p1
            if is_prime(p2):
                return (p1, p2)
    return None

def analyze_anomalies(anomalies):
    """Analyze the anomaly points for patterns"""
    
    print("\n" + "="*90)
    print("ANOMALY POINTS ANALYSIS (where cm increases by 0.6 instead of 1.0)")
    print("="*90 + "\n")
    
    print(f"{'m':<8} {'m/7':<8} {'m is Prime?':<15} {'Prime Factors':<25} {'Goldbach Pair (if even)':<25}")
    print("-" * 95)
    
    goldbach_patterns = []
    
    for m in anomalies:
        quotient = m // 7
        prime_check = "YES" if is_prime(m) else "NO"
        factors = prime_factors(m)
        factors_str = "×".join(map(str, factors)) if factors else "1"
        
        # Try to find Goldbach decomposition
        goldbach = goldbach_decomposition(m)
        if goldbach:
            gb_str = f"{goldbach[0]} + {goldbach[1]}"
            goldbach_patterns.append((m, goldbach))
        else:
            gb_str = "N/A"
        
        print(f"{m:<8} {quotient:<8} {prime_check:<15} {factors_str:<25} {gb_str:<25}")
    
    print("\n" + "="*90)
    print("PATTERN SUMMARY")
    print("="*90)
    
    # Check if all anomalies are multiples of 7
    all_div_7 = all(m % 7 == 0 for m in anomalies)
    print(f"✓ All anomalies divisible by 7: {all_div_7}")
    
    # Check common factors
    print(f"\nCommon divisors analysis:")
    gcd_val = anomalies[0]
    for m in anomalies[1:]:
        gcd_val = math.gcd(gcd_val, m)
    print(f"  GCD of all anomalies: {gcd_val}")
    print(f"  GCD / 7 = {gcd_val // 7}")
    
    # Spacing analysis
    spacings = [anomalies[i+1] - anomalies[i] for i in range(len(anomalies)-1)]
    print(f"\nSpacings between anomalies:")
    print(f"  Min spacing: {min(spacings)}")
    print(f"  Max spacing: {max(spacings)}")
    print(f"  Average spacing: {sum(spacings) / len(spacings):.1f}")
    print(f"  Unique spacings: {sorted(set(spacings))}")
    
    # Prime factors of anomalies
    print(f"\nPrime factor frequency in anomalies:")
    all_factors = {}
    for m in anomalies:
        for factor in set(prime_factors(m)):
            all_factors[factor] = all_factors.get(factor, 0) + 1
    
    for factor in sorted(all_factors.keys()):
        pct = (all_factors[factor] / len(anomalies)) * 100
        print(f"  {factor}: appears in {all_factors[factor]}/{len(anomalies)} anomalies ({pct:.1f}%)")
    
    # Check divisibility by small primes
    print(f"\nDivisibility patterns in anomalies:")
    for p in [2, 3, 5, 7, 11, 13]:
        count = sum(1 for m in anomalies if m % p == 0)
        pct = (count / len(anomalies)) * 100
        print(f"  Divisible by {p}: {count}/{len(anomalies)} ({pct:.1f}%)")

def test_multiples_of_seven_precise(start=7, end=5000, step=7):
    """Test the formula on multiples of seven using high precision"""
    print("Testing formula on multiples of seven (High Precision):\n")
    print(f"{'Multiple':<12} {'d':<8} {'cm (result)':<15} {'Change':<12}")
    print("-" * 50)
    
    drops_found = []
    prev_cm = None
    
    for m in range(start, end + 1, step):
        try:
            d = calculate_d_precise(m)
            cm = next_formula(m, d)
            
            change = ""
            if prev_cm is not None:
                diff = cm - prev_cm
                if abs(diff - 1.0) < 0.01:
                    change = "+1.0 ✓"
                elif abs(diff - 0.6) < 0.01:
                    change = "+0.6 ⚠"
                    drops_found.append((m, cm, diff))
                else:
                    change = f"+{diff:.1f}"
            
            print(f"{m:<12} {d:<8} {cm:<15.4f} {change:<12}")
            prev_cm = cm
            
        except Exception as e:
            print(f"{m:<12} ERROR: {str(e)[:30]}")
            break
    
    print("\n" + "="*50)
    print(f"Total transitions: {(end - start) // step}")
    print(f"Anomalies found (0.6 increment drops): {len(drops_found)}")
    if drops_found:
        print("\nFirst 10 anomaly points:")
        for m, cm, diff in drops_found[:10]:
            print(f"  m = {m:<6} | cm = {cm:<8.4f} | change = {diff:.1f}")
        if len(drops_found) > 10:
            print(f"  ... and {len(drops_found) - 10} more")
        
        # Extract just the m values for analysis
        anomaly_m_values = [m for m, _, _ in drops_found]
        analyze_anomalies(anomaly_m_values)

# Run test on multiples of seven - high precision
test_multiples_of_seven_precise(start=7, end=5000, step=7)
