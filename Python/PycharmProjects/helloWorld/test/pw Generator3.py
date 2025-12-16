import random


##main variables
letters = 'abcdefghijklmnopqrstuvwxyz'
Cletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Sletters = '!@#$%^&*()-_+?~'
numbers = '1234567890'


##assigning
m1 = random.choice(letters)     # this is to choose a single character from the ##main variables above.
m2 = random.choice(Cletters)
m3 = random.choice(Sletters)
m4 = random.choice(numbers)
mm1 = m1,m2,m3,m4


e = 0       # using a 'loop counter' to help with creating a new variable for each loop.


for i in range(10):     # loop is for re-setting the variables within ##assigning using the (import random).

    m1 = random.choice(letters)
    m2 = random.choice(Cletters)
    m3 = random.choice(Sletters)
    m4 = random.choice(numbers)
    mm1 = m1, m2, m3, m4
    a1 = random.choice(mm1)

    m1 = random.choice(letters)
    m2 = random.choice(Cletters)
    m3 = random.choice(Sletters)
    m4 = random.choice(numbers)
    mm1 = m1, m2, m3, m4
    a2 = random.choice(mm1)

    m1 = random.choice(letters)
    m2 = random.choice(Cletters)
    m3 = random.choice(Sletters)
    m4 = random.choice(numbers)
    mm1 = m1, m2, m3, m4
    a3 = random.choice(mm1)

    m1 = random.choice(letters)
    m2 = random.choice(Cletters)
    m3 = random.choice(Sletters)
    m4 = random.choice(numbers)
    mm1 = m1, m2, m3, m4
    a4 = random.choice(mm1)

    char4 = a1 + a2 + a3 + a4       # this is to make 4 unique characters together in 1 loop

    if e == 0:          # using the 'loop counter' here in a boolean if statement,
        aa1 = char4     # to create a new variable and assign it to the main variable in the loop (char4) regarding the unique characters,
        e = e + 1       # then finally adding 1 to the 'loop counter' then continuing/repeating below.

    elif e == 1:
        aa2 = char4
        e = e + 1

    elif e == 2:
        aa3 = char4
        e = e + 1

    elif e == 3:
        aa4 = char4
        e = e + 1

    else:
        break           # using a break function to stop the loop before reaching the specified (range) of the loop.

print(aa1+aa2+aa3+aa4)      # adding each new variable together. remember each variable contains 4 letters.
#print(char4)
#print(e)
