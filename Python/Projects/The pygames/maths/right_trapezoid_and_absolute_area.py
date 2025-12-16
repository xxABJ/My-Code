## area of right trapezoid
def rt(a, b, c):
    print(f"\na = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    return print(f"area of trapezoid: {((a*c) + (b*c)) / 2}")

## absolute area (aA) under a curve
def aa_rt(y2, y1, x2, x1):
    print(f"absolute area under a curve aA:")
    print(f"\ny2 = {y2}")
    print(f"y1 = {y1}")

    if y2 > y1:
        print(f"\nThe curve is ascending because y2:{y2} is -BIGGER- than y1:{y1}")
    elif y2 < y1:
        print(f"\nThe curve is descending because y2:{y2} is -SMALLER- than y:{y1}")
    elif y2 == y1:
        print(f"\nThe curve is straight because y2:{y2} is the -SAME- as y1:{y1}")

    print(f"\nx2 = {x2}")
    print(f"x1 = {x1}")

    print(f"\nformula of aA:")
    print(f"|y2| + |y1| * |x2 - x1| / 2\n")

    aA = ((y2 + y1) * (x2 - x1)) / 2

    print(f"without using the absolute values for the x's (checking for a negative), A = {aA}\n")

    if aA < 0:
        return print(f"aA = {aA * -1}")
    else:
        return print(f"aA = {aA}")

    #values = [y2, y1, x2, x1]
    #for absolute_values in values:
    #    print(f"{absolute_values} = index: {values.index(absolute_values)}")
    #    if absolute_values < 0:
    #        new_value = absolute_values * -1
    #        print(f"new_value: {new_value}\n")
    #        values[values.index(absolute_values)] = new_value
    #
    #Y2 = values[0]; print(f"Y2 = {Y2}") 
    #Y1 = values[1]; print(f"Y1 = {Y1}")
    #X2 = values[2]; print(f"X2 = {X2}") 
    #X1 = values[3]; print(f"X1 = {X1}")
    #
    #return print(f"\naA = {aA}\n")

def P_aa_rt(y2, y1, x2, x1):
    aA = ((y2 + y1) * (x2 - x1)) / 2

    if aA < 0:
        return print(f"\ty2: {y2}\ty1: {y1}\tx2: {x2}\tx1: {x1}\taA = {aA * -1}")
    else:
        return print(f"\ty2: {y2}\ty1: {y1}\tx2: {x2}\tx1: {x1}\taA = {aA}")
    
def roc(y2, y1, x2, x1):
    print(f"\ny2 = {y2}")
    print(f"y1 = {y1}")

    if y2 > y1:
        print(f"\nThe curve is ascending because y2:{y2} is -BIGGER- than y1:{y1}")
    elif y2 < y1:
        print(f"\nThe curve is descending because y2:{y2} is -SMALLER- than y:{y1}")
    elif y2 == y1:
        print(f"\nThe curve is straight because y2:{y2} is the -SAME- as y1:{y1}")

    print(f"\nx2 = {x2}")
    print(f"x1 = {x1}")

    print(f"\n(y2 - y1) = {(y2 - y1)}")
    print(f"(x2 - x1) = {(x2 - x1)}")

    aA = ((y2 + y1) * (x2 - x1)) / 2
    roc = ((y2 - y1) / (x2 - x1))
    if aA < 0:
        print(f"(negative changed)aA = {aA * -1}")
        aA *= -1
    else:
        print(f"aA = {aA}")
    print(f"aA * roc: {aA*roc}") # <<< 
    print(f"aA / roc: {aA/roc}") # <<< 

    return print(f"\nrate of change = {(y2 - y1) / (x2 - x1)}")

#rt(64,47,12)
#
#print()
#print("---------------")
#print()
#
#aa_rt(47, 64, 11, 23)

#print()
#print("---------------")
#print()
#
#P_aa_rt(7.01, 4.01, 1.01, 3.01)
#P_aa_rt(7.02, 4.02, 1.02, 3.02)
#P_aa_rt(7.03, 4.03, 1.03, 3.03)
#P_aa_rt(7.04, 4.04, 1.04, 3.04)
#P_aa_rt(7.05, 4.05, 1.05, 3.05)
#P_aa_rt(7.06, 4.06, 1.06, 3.06)
#P_aa_rt(7.07, 4.07, 1.07, 3.07)
#P_aa_rt(7.08, 4.08, 1.08, 3.08)
#P_aa_rt(7.09, 4.09, 1.09, 3.09)
#P_aa_rt(7.1, 4.1, 1.1, 3.1)
#P_aa_rt(7.11, 4.11, 1.11, 3.11)
#P_aa_rt(7.111, 4.111, 1.111, 3.111)
#P_aa_rt(7.112, 4.112, 1.112, 3.112)
#P_aa_rt(7.1135, 4.1135, 1.1135, 3.1135)
#P_aa_rt(7.1136, 4.1136, 1.1136, 3.1136)
#
#print()
#print("---------------")
#print()

roc(7.0, 7.1, 2.0, 2.1)
roc(7.1, 7.2, 2.1, 2.2)
roc(7.2, 7.3, 2.2, 2.3)
print()