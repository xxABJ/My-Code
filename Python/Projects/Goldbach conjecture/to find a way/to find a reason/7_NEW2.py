import math

num = 42

m = num

formula = m / 2**m # will be a decimal number ... x e-7

# count how many decimal places are there to reach first digit greator than 0 as d
# if d is (odd & M of 7) then next_formula = (2/10) * (m) - ((d * 2 + 2) / 10))
# elif d is (odd & ! M of 7) then next_formula = (2/10) * (m) - ((d * 2 - 2) / 10))
# elif d is even then next formula = (2/10) * (m) - (d * 2 / 10)

d = math.ceil(-math.log10(formula))

def next_formula(d):

    if d % 2 == 1:

        if m % 7 == 0 and (d / 7) % 2 == 1:

            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm

        elif m % 7 == 0 and (d / 7) % 2 == 0:

            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm

        elif m % 7 != 0 and (d / 7) % 2 == 1:

            cm = ((2 / 10) * m) - ((d * 2 - 2) / 10)
            return cm

        elif m % 7 != 0 and (d / 7) % 2 == 0:

            cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
            return cm

    
    else:

        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

cm = next_formula(d)

print(int(d))
print(cm)

def cm_patched(m):
    d = next_formula(d)
    if d % 2 == 1:
        cm = 0.2*m - (2*d + 2)/10
    else:
        cm = 0.2*m - (2*d)/10

    d_next = next_formula(d+ 7)
    is_anomaly = (d % 2 == 1) and (d_next == d + 1)

    if is_anomaly:
        cm += 0.4

    return cm


print(cm_patched(m))