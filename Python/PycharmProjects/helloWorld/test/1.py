import random
import time


#colour = [r,b,g]
#light = 1
#randomizer = light * random.choice(colour)
#s1 = random.choice(colour)
#s2 = random.choice(colour)
#s3 = random.choice(colour)
#s4 = random.choice(colour)
#s5 = random.choice(colour)
#s6 = random.choice(colour)
#s7 = random.choice(colour)
#s8 = random.choice(colour)
#s9 = random.choice(colour)
#s10 = random.choice(colour)
#s5 = s1,s2,s3,s4
#seq = 0

def randomStart():

    green = '#  g  #'
    red = '#  r  #'
    blue = '#  b  #'

    g = green
    r = red
    b = blue

    top = '#######'
    randomStart = g,r,b
    bot = '#######'
    rS = random.choice(randomStart)
    print(top),
    print(rS),
    print(bot)

cr = 0
cb = 0
cg = 0

seq = 0

while seq < 5:
    randomStart()
    start = input("What is the colour? ")
    if start == randomStart(rS):
        seq = seq + 1
        randomStart()
    else:
        print("Wrong Answer :P")
        print("Try again!")
        break

    rS2 = randomStart,
    start2 = input("What is the colour sequence ? ")
    if start2 == rS2:
        seq = seq + 1
        randomStart()
    else:
        print("Wrong Answer :P")
        print("Try again!")
        break

    rS3 = randomStart
    start3 = input("What is the colour sequence ? ")
    if start3 == rS3:
        break
        #seq = seq + 1
        #randomStart()
    else:
        #print("Wrong Answer :P")
        #print("Try again!")
        break

            #b = answer1+c
            #print(c+b)
            #s1 = random.choice(colour)



        #if seq == 2:
        #    print(c>answer1)
        #    seq = seq + 1



    #while answer == rightColour:


#memory =

#game = print(randomizer)
#sequence = print(game)

#answer = str = input("What is the letter?: ")
#class start():
#    randomizer > answer

#class engine():
#    game > answer
#    while answer == sequence:
#        for round in light:
#            if input == game:
#                set(light) + 1
#                exec(start())

#            else:
#                print("Wrong Answer :P")
#                print("Try again!")