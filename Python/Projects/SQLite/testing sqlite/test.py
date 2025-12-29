import threading, time

e = '| Welcome to the program |'
d = ['|------------------------|'.join(input("\n| Type your name: ")).join('\n|------------------------|')]

def text(d):
    for line in d:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()

def i(d, e):
    time.sleep(5)
    print("in")
    d[e] = input("| Type your name: ").join(d[e][-1])
    #print(e)

#def text2(d):
#    text(d)

p1 = threading.Thread(target=text, args=(d,))
p1.start()

p2 = threading.Thread(target=i, args=(d, 1,))
p2.start()
#
#p3 = threading.Thread(target=text2, args=(d,))
#p3.start()

p1.join()
p2.join()
#p3.join()
