import random

a, b, c, d = 0, 3, 4, 9

l = [a,b,c,d]

d = {
    't': b,
    'b': a,
    'l': c,
    'r': d
}



#print(list(reversed(sorted(l))))
print(f"list: {list(sorted(d.values()))}")

biggest = list(reversed(sorted(d.values())))

#print(f"reversed: {biggest}")
#print(f"biggest two: {biggest[:2]}\n")


#full_list = list(d.keys())
#print(f"full_list: {full_list}")
#popped_value = full_list.pop(full_list.index('b'))
#print(f"filtered_list: {full_list}")

print(d.get('t'))


A = (0, 4)
B = (2, 1)



print(tuple(a + b for a, b in zip(A, B)))

row = 26
print(30 - ((row - 2) + (2)) - 2)


print(len({1:3,2:5,4:'k', 8:0}))


a = (10, 0)

b = (-1, 1)

print(tuple(a + b for a, b in zip(a, b)))



class testing:

    class a:

        def __init__(self, main):
            self.main = main


        def adding(self):
            self.main.total += 1
    
    class b:
        pass

    class c:
        pass


class a:

    class b:
        
        
        
        
        class c:
            pass

        
        
        
        
        class d:
            pass
       

        
    class c:
        pass


    def __init__(self):

        #self.A = testing.a(self)

        self.total = 0

        
        self.assignment = {
            1: testing.a(self)
        }

        self.total_assignments = 0
        self.assignments = {}
    def assign(self, num):

        return self.assignment.get(num).adding()
    

    def print_total(self):

        print(self.total)


print("\n", "-"*5, "\n")
t = testing()
t.print_total()
print(list(t.assignment.values()))
t.assign(1)
print(list(t.assignment.values()))
t.assign(1)
print(list(t.assignment.values()))
t.print_total()

print()
for _ in range(1, 4):
    print(_)

ran = ["r", "l"]


print(random.choice(ran))



arrows = {
    "l": "←",
    "r": "→",
    "u": "↑",
    "d": "↓"
}

round = 0
while round < 5:
    print("neovim!")
    round += 1



print("******************************************")
print("And I Am using . . .")
print("Vim Motions :p")
print("But I have to try to")
print("type without looking !")
print("And use the Vim Motions without looking :D")
print("******************************************")

