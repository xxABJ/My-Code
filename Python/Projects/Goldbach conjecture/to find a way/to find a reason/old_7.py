import math

num = 42

m = num

formula = m / 2**m # will be a decimal number ... x e-7

# count how many decimal places are there to reach first digit greator than 0 as d
# if d is odd then next_formula = (2/10) * (m) - ((d * 2 + 2) / 10))
# elif d is even then next formula = (2/10) * (m) - (d * 2 / 10)

d = math.ceil(-math.log10(formula))

def next_formula(d):

    if d % 2 == 1:

        cm = ((2 / 10) * m) - ((d * 2 + 2) / 10)
        return cm

    
    else:

        cm = ((2 / 10) * m) - (d * 2 / 10)
        return cm

cm = next_formula(d)

print(int(d))
print(cm)