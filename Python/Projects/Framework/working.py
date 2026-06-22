# Equation = (a*b*c)^p

a = 3
b = 5
c = 6
p = 2


def FS_(a, b, c, p):

    FS = 1
    for _ in range(p, 0, -1):

        FS *= ((a*b) / _) * c

    return FS
FS = FS_(a, b, c, p)
#print(FS)


AN = 4
TA = AN * p
i = a * b # a * b / 0 = ind^^a*b
Ti = TA - i # TA - abs(ind^^a*b)


def Fi_(TA, Ti):

    if Ti > 0:

        Fi = Ti * AN
    

    else:

        Fi = abs(Ti)

    return Fi
Fi = Fi_(TA, Ti)
#print(Fi)


def indsum_(Fi, AN, TA, p):

    indsum = float

    numerator = ((TA / Fi) / AN)
    denominator = ((((TA / Fi) / AN) * p) + ((TA / Fi) / AN))

    indsum = numerator / denominator

    return indsum
indsum = indsum_(Fi, AN, TA, p)
#print(indsum)


def p_numbers_(p):

    p_numbers = []
    for _ in range(1, p+1):
        
        p_numbers.append(_)

    return p_numbers
p_numbers = p_numbers_(p)
#print(p_numbers)



def tn_factorial_(p_numbers):

    tn_factorial = 1
    for tn in p_numbers:
        
        tn_factorial *= tn

    return tn_factorial
tn_factorial = tn_factorial_(p_numbers)
#print(tn_factorial)


def triangular_numbers_(p):

    triangular_numbers = 0
    for _ in range(0, p+1):
        
        tn = (p + 1) - _
        triangular_numbers += tn

    return triangular_numbers
tn_total = triangular_numbers_(p)
#print(tn_total)
tn_m1 = tn_total - 1
#print(tn_m1)


def SPF_(p):

    numerator = p * p
    denominator = p + p

    SPF = numerator / denominator

    return SPF
SPF = SPF_(p)
#print(SPF)


def BNS_(p):

    BNS = []
    for _ in range(1, p+1):
        
        bn = _ / 10
        BNS.append(bn)

    return BNS
BNS = BNS_(p)
#print(BNS)


def Q1_(FS, tn_factorial, SPF):


    Q1 = FS * tn_factorial * SPF

    
    return Q1
Q1 = Q1_(FS, tn_factorial, SPF)
#print(Q1)


# This is the actual answer to the question
def Q2_(FS, tn_factorial):


    Q2 = FS * tn_factorial


    return Q2
Q2 = Q2_(FS, tn_factorial)
#print(Q2)


def Q3_(FS):


    Q3 = FS


    return Q3
Q3 = Q3_(FS)
#print(Q3)


def FBNS_(FS, BNS, indsum, tn_m1):

    FBNS = []
    for bn in BNS:
        
        sum = FS * indsum * tn_m1 * bn
        FBNS.append(sum)

    return FBNS
FBNS = FBNS_(FS, BNS, indsum, tn_m1)
print(FBNS)
FBNS_total = sum(FBNS)
print(FBNS_total)


def BNSt_(FS, BNS, indsum, tn_m1):

    if len(BNS) >= 3:
        
        BNSt = []
        BNSc = FS * indsum * tn_m1 * BNS[-1]
        BNSt.append(BNSc)

        BNSa = FS * indsum * tn_m1 * BNS[-3]
        BNSt.append(BNSa)


    else:

        BNSt = []
        l = len(FBNS)
        print(l)
        c = -3
        rw = -(l % c)
        print(rw)

        if rw == 2:

            print("here")
            BNSt = []
            BNSa = FS * indsum * tn_m1 * -(rw-1/10)
            BNSt.append(BNSa)

            BNSc = FS * indsum * tn_m1 * BNS[0]
            BNSt.append(BNSc)


        elif rw == 1:
            
            BNSt = []
            BNSa = FS * indsum * tn_m1 * -(rw/10)
            BNSt.append(BNSa)

            BNSc = FS * indsum * tn_m1 * BNS[0]
            print(FS)
            print(indsum)
            print(tn_m1)
            print(BNS[1])
            print(BNSc)
            BNSt.append(BNSc)

    print(BNSt)
    return BNSt
BNSt = BNSt_(FS, BNS, indsum, tn_m1)
print(BNSt)
BNSt_total = BNSt[0] + BNSt[1]


R = Q1 / FBNS_total


FH = Q2 / BNSt_total


SH = R / 2


f0 = (Q3 * R) - (FH + SH)
f1 = f0 / tn_total
f2 = f1 * tn_m1
f3 = f2 + tn_total





