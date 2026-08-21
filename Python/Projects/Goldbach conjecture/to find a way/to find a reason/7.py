# to find a CM of a multiple of seven
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
    # formula = m / 2^m using Decimal
    formula = Decimal(m) / (Decimal(2) ** m)
    
    # log10(formula) = log(formula) / log(10)
    log_formula = formula.ln() / Decimal(10).ln()
    
    # d = ceil(-log10(formula))
    d = int(-log_formula) if (-log_formula) == int(-log_formula) else int(-log_formula) + 1
    return d

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
        print("\nAnoaly points:")
        for m, cm, diff in drops_found:
            print(f"  m = {m:<6} | cm = {cm:<8.4f} | change = {diff:.1f}")

# Run test on multiples of seven - high precision
test_multiples_of_seven_precise(start=7, end=5000, step=7)


#@TODO: 


## d is odd & !mof7 = -2   . . .  odd & mof7 = +2


# in report
# + why & what Parity-Driven Discontinuity

### check other multiples, 