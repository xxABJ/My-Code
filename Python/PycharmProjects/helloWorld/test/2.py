wallet = 25  # change number to see outcomes
socks = 0

for price in range(10):
    if wallet >= price:
        wallet = wallet - price
        socks = socks + 1
    else:
        break

if (socks % 2) > 0:
    print("I can pair my socks")
else:
    print("I need one more...")

    start = input("What is the colour? ")
    if start == s1:

        s1 = random.choice(colour)
        seq = seq + 1
        if seq == 1:
            print(s1 > start)
            seq = seq + 1

        for game in range(10):
            answer1 = input("What is the sequence now? ")
            c = answer1
            if answer1 == s1 > start:
                answer1 = s1 > start
                print(c)
                # c = answer1
                s1 = random.choice(colour)

            elif answer1 == c:
                # answer1 = c
                s1 = random.choice(colour)
                answer1 = s1 > c
                print(answer1 + c)

            else:

                print('Wrong answer :p')
                print('Try again !')
                break