import random

#main variables
letters = 'abcdefghijklmnopqrstuvwxyz'
Cletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Sletters = '!@#$%^&*()-_+?~'
numbers = '1234567890'

#assigning
m1 = random.choice(letters)
m2 = random.choice(Cletters)
m3 = random.choice(Sletters)
m4 = random.choice(numbers)

m5 = random.choice(letters)
m6 = random.choice(Cletters)
m7 = random.choice(Sletters)
m8 = random.choice(numbers)

m9 = random.choice(letters)
m10 = random.choice(Cletters)
m11 = random.choice(Sletters)
m12 = random.choice(numbers)

m13 = random.choice(letters)
m14 = random.choice(Cletters)
m15 = random.choice(Sletters)
m16 = random.choice(numbers)

mm1 = m1,m2,m3,m4
mm2 = m5,m6,m7,m8
mm3 = m9,m10,m11,m12
mm4 = m13,m14,m15,m16

#mixing
a1 = random.choice(mm1)
a2 = random.choice(mm2)
a3 = random.choice(mm3)
a4 = random.choice(mm4)
aa1 = a1 + a2 + a3 + a4
#e = aa1

a5 = random.choice(mm1)
a6 = random.choice(mm2)
a7 = random.choice(mm3)
a8 = random.choice(mm4)
aa2 = a5 + a6 + a7 + a8
#e1 = aa2

a9 = random.choice(mm1)
a10 = random.choice(mm2)
a11 = random.choice(mm3)
a12 = random.choice(mm4)
aa3 = a9 + a10 + a11 + a12
#e2 = aa3

a13 = random.choice(mm1)
a14 = random.choice(mm2)
a15 = random.choice(mm3)
a16 = random.choice(mm4)
aa4 = a13 + a14 + a15 + a16
#e3 = aa4

list
set

print(mm1)
print(mm2)
print(mm3)
print(mm4)
print(a1)
print(aa1)
print(aa1+aa2+aa3+aa4)