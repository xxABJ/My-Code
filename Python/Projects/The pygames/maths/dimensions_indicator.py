## n^y

# Any Number n
_n = 3

# To the power of y
_p = 5

"""
A module to handle "direction layers" (or dimensions?) and indicators in mathematical calculations by Abj.

Run's like a normal power calculator, but with a special focus on a new perspective of numbers called "indicators",
which requires all numbers to obtain a new fixed value called "direction layer", which acts as a layer of depth for the number,
without introducing a new dimension to the number system.

Most importantly, this allows for the division by zero problem to be viewed in a new perspective by using indicators as a new perspective to zero.

The idea is that there are "anti" numbers that exist in another layer of depth, which are accessible acendingly dividing by 0, or decendingly by dividing by ind0. (ind is short for indicator)
When a number is divided by 0, it goes to an "anti" layer of depth, which is represented by the indicator perspective.

This module also uses another way to find the power of numbers, and through that, it takes a number n, and raises it to the power of y.
If n is 0 or 1, then the indicator perspective is used to avoid division by zero in the main formula.

The main formula used in this module just uses some back and forward calculations of ratios of n and y,
but with a "fabric layer" idea that comes from [TR(a*a) - TL(a+a) - BR(a/a), BL(a)],
where (TR/TL) / BL = will always equal 4, 2a/(a**2/2a) = 4. Except when a = 0. (with the indicator perspective, a would be ind0.dl=1)

Fabric layers might be
# - no.expresions - no.operators

"""

def dbz(inp, dl="", indicator=False):
    #creates a new type of int with a direction layer using a dict
    #has to by convienent
    if int(dl) == 0:
        inp = {'value': inp, 'dl': int(dl)}
        return inp
    elif 0 < int(dl):
        new_dl = 1
        dl = int(dl)+new_dl
        inp = {'value': inp, 'dl': dl}
        return inp
    elif indicator == True and int(dl) == 0:
        inp = {'value': ("ind", inp), 'dl': int(dl)}
        return inp
    elif indicator == True and 0 < int(dl):
        new_dl = 1
        dl = int(dl)+new_dl
        inp = {'value': ("ind", inp), 'dl': int(dl)}
        return inp
    else:
        exit("dbz error")
    
# indicator = another prespective to 0
n = _n ; y = _p
i = 1
d = (y - y) + 1
d1 = d
dy = -d

dys = []
for d in range(y):
    inte = -1
    dys.append(inte)
else:
    inte = -1
    dys.append(inte)
print(f"dys = {dys}")

if y%2 == 0: #even
    ny = n**y
    print(f"ny = {n} ^ {y} = {ny}")
    print("y is even")
    ans = 1
    for ds2 in dys[:]:
        ans *= ds2
    j_n = ans
    j_n *= -1 ## could this be the fabric layer of a number?
    a = j_n
    print(f"jn = {j_n} , a = {a}")
else: #odd
    ny = n**y
    print(f"ny = {n} ^ {y} = {ny}")
    print("y is odd")
    ans = 1
    for ds2 in dys[:1]:
        ans *= ds2
    j_n = ans
    a = j_n
    print(f"jn = {j_n} , a = {a}")

jn = (n + 1)
jys = []
for jas in range(y):
    inte = jn
    jys.append(inte)
else:
    inte = jn
    jys.append(inte)
print(f"jys = {jys}")

ans = 1
for j in jys:
    ans *= j
    ja = ans
print(f"ja = {ja}")
ans_b2 = 1
for j in jys[:1]: # y-1 root ja
    ans_b2 *= j
    b2 = ans_b2
print(f"b2 = {b2}")

b = n - y - ja - b2 - (-i) * a
print(f"b = (n - y - ja) - ((y-1)root_ja) - (-i) x a")
print(f"b = {n} - {y} - {ja} - {b2} - {-(-i)} * {a} , b = {b}")
print(f"b = n:{n} - y:{y} - ja( jn1({jn}) x jn2 x jn3 ... [y*(jn)amount] ):{ja} - b2((y-1)root_ja):{b2} - -i(indicator):{-(-i)} * a([-i x da] if even or [-i x da-1] if odd):{a} , b = {b}")
 
if n == 0:
    ## indicator perspective
    dbz_n = dbz(n, dl=0, indicator=True)
    dbz_n['value'] = ("ind",y-1)
    new_n = dbz_n['value'][1]
    c = abs((dbz_n['value'][1]) - dbz_n['value'][1] + (y-1)) * 3*(y-1)
    print(f"""\n
          since n is 0, an indicator perspective is required:
          dbz_n = dbz({n}, dl=0, indicator=True) -> dbz_n['value'] = {dbz_n['value']}, and direction layer (dl) = {dbz_n['dl']}
          and if n=0 then c is ({y-1} - ({y-1}/{n}) * {y-1}), which would not be possible due to try to ({y-1}/{n}), therefore dividing by zero normally is not possible.

          So to avoid that we use the indicator perspective, therefore:
                        dbz_n = dbz({n}, dl=0, indicator=True)
                        dbz_n['value'] = ("ind", {y-1})
                        new_n = dbz_n['value'][1] , new_n = {dbz_n['value'][0]}{dbz_n['value'][1]}
          
          conversion is required:
          abs of |{dbz_n['value'][0]}{dbz_n['value'][1]}|  +  ({dbz_n['value'][0]}{dbz_n['value'][1]}) * 1/ind0 + ({y-1}), which should equal: ({y-1}) when the direction layers are the same (i.e n and y have default dl's which is 0)

          New formula would be, c = {y-1} - {dbz_n['value'][0]}{dbz_n['value'][1]} * {y-1}

          final answer c = {((abs(dbz_n['value'][1]) + (dbz_n['value'][1])) + (y-1)) * (3*(y-1))}
          (SKIPPED ACTUAL INDICATOR CONVERSION CODE DUE TO NOT HAVING ACTUAL METHOD FOR IT)\n
        """)

elif n == 1:
    ## indicator perspective is required here as well because in the main formula, n=1 would cause division by 0, so we use indicator perspective to avoid that
    dbz_c = dbz(b, dl=0, indicator=True)
    dbz_c['value'] = ("ind", b)
    new_c = dbz_c['value'][1]
    c = ((abs(dbz_c['value'][1]) - (dbz_c['value'][1])) + (b))

    print(f"""\n
          since n is 1, an indicator perspective is required to avoid division by 0 in the main formula
          
          main formula = {b} * ( {n**y} / ( {b} * ( {b} / {c} ) / {b} ) / {b} * {b} / {c},
          where within the denominator we have ..(b:{b}/c:{c}),
          and if n=1 then c is ({y-1} - ({y-1}/{n}) * {y-1}), which would equal to ({((y-1) - (y-1/n)) * (y-1)}), therefore dividing by zero normally is not possible.

          So to avoid that we use the indicator perspective, therefore:

                        dbz_c = dbz(b, dl=0, indicator=True)
                        dbz_c['value'] = ("ind", b)
                        new_c = dbz_c['value'][1] , new_c = {dbz_c['value'][0]}{dbz_c['value'][1]}
          
          conversion is required:
          abs of |{dbz_c['value'][0]}{dbz_c['value'][1]}|  -  ({dbz_c['value'][0]}{dbz_c['value'][1]}) * 1/ind0 + ({b}), which should equal: ({b}) when the direction layers are the same (i.e n and y have default dl's which is 0)

          conversion for the c in: (b*(b/c)/b), becomes:
          c ('[]') = ( b: {b} * ( b / [ abs of |{dbz_c['value'][0]}{dbz_c['value'][1]}|  -  {dbz_c['value'][0]}{dbz_c['value'][1]} * 1/ind0 + ({b}) ] / b: {b} ),

          So the new c becomes:
          {abs(dbz_c['value'][1])} + ({dbz_c['value'][1]}) + {b}
          c = {((abs(dbz_c['value'][1]) + (dbz_c['value'][1])) + (b))}

          final answer of c when we do (b*(b/c)/b) = {(b * ( b / ((abs(dbz_c['value'][1]) - (dbz_c['value'][1])) + (b)) ) / b)}
          (SKIPPED ACTUAL INDICATOR CONVERSION CODE DUE TO NOT HAVING ACTUAL METHOD FOR IT)\n
        """)
    

else:
    c = ((y-1) - (y-1/n)) * (3*(y-1))
    print(f"c = {y-1} - {(y-1/n)} * {y-1} , c = {(y-1 - (y-1/n)) * 3*(y-1)}")

def calculate():
    #calculate = b * (n**y / (b*(b/c)/b)) / b * b/c
    print(f"""

    | ({b} * {(n**y / (b*(b/c)/b))}) = {b * (n**y / (b*(b/c)/b))}
    | ___________________________________________________________ 
    | 
    | {b}                     

    
                                 X        
                             
    
    | {b}
    | ___________________________________________________________
    | 
    | {c}


                                 X

                            
      {-i}


FINAL ANSWER = {b * (n**y / (b*(b/c)/b)) / b * b/c}

""")
    
calculate()