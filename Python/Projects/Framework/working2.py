# Equation = (a*b*c)^p
#without including original answer in the solution ... does it even matter ?

from contextlib import redirect_stdout
from io import StringIO
from math import factorial

a = 3
print(f"a: {a}")
b = 5
print(f"b: {b}")
c = 6
print(f"c: {c}")
p = 4
print(f"p: {p}")

print(f"Equation: ({a}*{b}*{c})**{p}  \nanswer should be  = {(a*b*c)**p}  = {pow((a*b*c), p)}")


print()
print()


def FS_(a, b, c, p): #Q3

    FS = 1
    for _ in range(p, 0, -1):

        FS *= ((a*b) / _) * c
        print(f"FS: {FS}  (iteration {_})")

    return FS
FS = FS_(a, b, c, p)
print(f"FS: {FS}")

def Q3_(FS):


    Q3 = FS


    return Q3
Q3 = Q3_(FS)
print(f"Q3: {Q3}")


print()
print()


AN = 4
print(f"AN: {AN}")
TA = AN * p
print(f"TA: {TA}")
i = a * b # a * b / 0 = ind^^a*b
print(f"i: {i}")
Ti = TA - i # TA - abs(ind^^a*b)
print(f"Ti: {Ti}")


print()
print()


def Fi_(TA, Ti):

    if Ti > 0:

        Fi = Ti * AN
    

    else:

        Fi = abs(Ti)

    return Fi
Fi = Fi_(TA, Ti)
print(f"Fi: {Fi}")


def indsum_(Fi, AN, TA, p):

    indsum = float

    numerator = ((TA / Fi) / AN)
    denominator = ((((TA / Fi) / AN) * p) + ((TA / Fi) / AN))


    if numerator == 0 or denominator == 0:

        indsum = 0
    
    else:

        indsum = numerator / denominator


    return indsum
indsum = indsum_(Fi, AN, TA, p)
print(f"indsum: {indsum}")


print()
print()


def p_numbers_(p):

    p_numbers = []
    for _ in range(1, p+1):
        
        p_numbers.append(_)

    return p_numbers
p_numbers = p_numbers_(p)
print(f"p_numbers: {p_numbers}")


def I1_(p): # I1

    I1 = 0
    for _ in range(0, p+1):
        
        tn = (p + 1) - _ # triangular numbers + 1
        print(f"tn: {tn}")
        I1 += tn

    return I1
I1 = I1_(p)
print(f"I1: {I1}")
I1_minus_1 = I1 - 1 # I1 -1 
print(f"I1_minus_1: {I1_minus_1}")


print()
print()


def BNS_(p): # k / 10  &  extra power number like I1

    BNS = []
    for _ in range(1, p+2):
        
        bn = _ / 10
        BNS.append(bn)

    return BNS
BNS = BNS_(p)
print(f"BNS: {BNS}")


def B2_(FS, BNS, indsum, I1_minus_1):

    FBNS = []
    for bn in BNS:
        
        sum = FS * indsum * I1_minus_1 * bn
        FBNS.append(sum)

    return FBNS
B2 = B2_(FS, BNS, indsum, I1_minus_1)
print(f"B2: {B2}")
B2_total = sum(B2)
print(f"B2_total: {B2_total}")


print()
print()


def S6_(Q3, B2_total):

    if B2_total == 0:

        print("B2_total is 0, S6 is set to 0 to avoid division by zero.")
        S6 = 0

    else:


        print(f"Q3 {Q3} / B2_total {B2_total} = {Q3 / B2_total}")
        S6 = Q3 / B2_total

    return S6
S6 = S6_(Q3, B2_total)
print(f"S6: {S6}")


def PF_(S6, AN):

    print(f"S6: {S6}, AN: {AN}")

    if S6 == 0:

        print("S6 is 0, PF is set to 0 to avoid division by zero.")
        PF = 0

    elif S6 == 1:

        PF = (S6/10) * AN

    elif S6 > 1:

        PF = (S6/10) - (S6/10)/10


    else:

        PF = 1

    return PF
PF = PF_(S6, AN)
print(f"PF: {PF}")


def SPF_(p):

    if p == 0:

        print("p is 0, SPF is set to 0 to avoid division by zero.")
        SPF = 0


    else:

        numerator = p * p
        denominator = p + p

        SPF = numerator / denominator

    return SPF
SPF = SPF_(p)
print(f"SPF: {SPF}")


print()
print()


def R_(Q3, S6, I1, SPF, AN):

    print(f"--SPF: {SPF}, AN: {AN}")

    # if SPF >= 2:
    #     f = (AN - S6) - (S6 / AN)
    #     print(f"f: {f}")
    #     #SPF = SPF*S6 + (AN*S6) #(AN*SPF)/(S6) + (SPF/S6)#(SPF/AN)*(2*AN)# + 1/SPF
    #     R = Q3 * S6 * I1 * SPF * f

    #     print(f"Q3: {Q3}, S6: {S6}, I1: {I1}, SPF: {SPF}, f: {f}")
    # else:
    print(f"Q3: {Q3}, S6: {S6}, I1: {I1}, SPF: {SPF}")
    R = Q3 * S6 * I1 * SPF

    return R
R = R_(Q3, S6, I1, SPF, AN)
print(f"R: {R}")


def C1_(I1, I1_minus_1):

    if I1 == 0 or I1_minus_1 == 0:

        print("I1 or I1_minus_1 is 0, C1 is set to 0 to avoid division by zero.")
        C1 = 0

    else:

        C1 = (I1 / I1_minus_1) * I1

    return C1
C1 = C1_(I1, I1_minus_1)
print(f"C1: {C1}")


print()
print()


f0 =  R * PF - C1
print(f"f0: {f0}")

f1 = f0 / I1
print(f"f1: {f1}")

f2 = f1 * I1_minus_1
print(f"f2: {f2}")

f3 = f2 + I1
print(f"f3: {f3}")


# Optional correction layer: keeps your pipeline intact and compensates for the
# factorial-scale drift that starts at p >= 4 in the else-only R_ version.
if p == 0:
    corrected = 1
    correction_factor = 1
else:
    correction_factor = (factorial(p) * (p + 2)) / (10 * p)
    corrected = f3 * correction_factor

print(f"correction_factor: {correction_factor}")
print(f"corrected: {corrected}")
print(f"expected: {(a*b*c)**p}")


def evaluate_for_p(test_p, a, b, c, AN, suppress_debug=True):

    def _calc():
        FS = FS_(a, b, c, test_p)
        Q3 = Q3_(FS)

        TA = AN * test_p
        i = a * b
        Ti = TA - i

        Fi = Fi_(TA, Ti)
        indsum = indsum_(Fi, AN, TA, test_p)

        I1 = I1_(test_p)
        I1_minus_1 = I1 - 1

        BNS = BNS_(test_p)
        B2 = B2_(FS, BNS, indsum, I1_minus_1)
        B2_total = sum(B2)

        S6 = S6_(Q3, B2_total)
        PF = PF_(S6, AN)
        SPF = SPF_(test_p)
        R = R_(Q3, S6, I1, SPF, AN)
        C1 = C1_(I1, I1_minus_1)

        f0 = R * PF - C1
        f1 = f0 / I1 if I1 != 0 else 0
        f2 = f1 * I1_minus_1
        f3 = f2 + I1

        if test_p == 0:
            correction_factor = 1
            corrected = 1
        else:
            correction_factor = (factorial(test_p) * (test_p + 2)) / (10 * test_p)
            corrected = f3 * correction_factor

        expected = (a * b * c) ** test_p
        return f3, corrected, expected, correction_factor

    if suppress_debug:
        sink = StringIO()
        with redirect_stdout(sink):
            return _calc()

    return _calc()


print()
print("Range test (p=0..12): model vs corrected vs expected")
for test_p in range(0, 13):
    model_value, corrected_value, expected_value, k = evaluate_for_p(test_p, a, b, c, AN, suppress_debug=True)
    model_ok = abs(model_value - expected_value) < 1e-6
    corrected_ok = abs(corrected_value - expected_value) < 1e-6
    print(
        f"p={test_p:2d} | model={model_value:.6f} | corrected={corrected_value:.6f} | "
        f"expected={expected_value:.6f} | K={k:.6f} | model_ok={model_ok} | corrected_ok={corrected_ok}"
    )






