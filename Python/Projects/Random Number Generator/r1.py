import tkinter
from tkinter import ttk
#tkinter GUI setup
#window = tkinter.Tk()
#window.title("RNG Generator")
#window.geometry("300x200")
#label = ttk.Label(window, text="RNG Generator", font=("Arial", 16))
#label.pack(pady=20)
#button_frame = ttk.Frame(window)
#button_frame.pack(pady=10)
#for i in range(10):
#    button = ttk.Button(button_frame, text=str(i), command=lambda num=i: start.produce(num))
#    button.grid(row=i//5, column=i%5, padx=5, pady=5)
#window.mainloop()

class rng():
    def __init__(self):
        self.operators = ["0","+","*","-","/"]
        self.initiate = True
        #self.rng_generate = False
        self.state = 0

    def change_state(self):
        if self.state < 4:
            self.state += 1
        else:
            self.state = 0

    def filler(self, n, operator):
        looper = n
        if operator == "0":
            self.change_state()
            return 0
        
        elif operator == "+":
            while True:
                self.change_state()
                if ((looper+(looper/3)+looper)*(looper/4)+looper%(looper/5)+looper)*10 % looper == 0 or ((looper+(looper/3)+looper)*(looper/4)+looper%(looper/5)+looper)*10 % looper < looper//2:
                    looper += (n - 1)
                else:
                    looper = ((looper+(looper/3)+looper)*(looper/4)+looper%(looper/5)+looper)*10 % looper
                    return looper
        
        elif operator == "*":
            while True:
                self.change_state()
                if ((looper*(looper/2)*looper)*(looper/3)*looper%(looper/4)*looper)*10 % looper == 0 or ((looper*(looper/2)*looper)*(looper/3)*looper%(looper/4)*looper)*10 % looper < looper//2:
                    looper += (n - 1)
                else:
                    looper = ((looper*(looper/2)*looper)*(looper/3)*looper%(looper/4)*looper)*10 % looper
                    return looper
                
        elif operator == "-":
            while True:
                self.change_state()
                if (((looper-(looper/3)-looper)*(looper/4)-looper%(looper/5)-looper)*-10) % looper == 0 or (((looper-(looper/3)-looper)*(looper/4)-looper%(looper/5)-looper)*-10) % looper < looper//2:
                    looper += (n - 1)
                else:
                    looper = (((looper-(looper/3)-looper)*(looper/4)-looper%(looper/5)-looper)*-10) % looper
                    return looper
        
        elif operator == "/":
            self.change_state()
            return 1

    def produce(self, n):
        filler_operator = self.operators[self.state]
        filler_size = n
        filler = self.filler(filler_size, filler_operator)

        bar = filler * 2
        dynamic_progress = filler//2
        states = 0
        for _ in range(int(bar)):
            d = filler//2
            if dynamic_progress < bar:
                dynamic_progress += d
                states += 1
            else:
                break
        
        list_n = []
        for _ in range(n):
            list_n.append(1)
            self.change_state()
        
        numbers_len = len(str(n))

        if numbers_len == 1:
            print(f"Single digit number: ({n})")
            if self.operators[self.state] == "0":
                #print(f"rng_value = {sum(list_n[-states])}")
                ans = 0
                print(f"rng_value = {0}")
                for random in range(ans+1):
                    self.change_state()

            elif self.operators[self.state] == "+":
                ans = sum(list_n[:-states+(n+n)])
                print(f"rng_value = {sum(list_n[:-states+(n+n)])}")
                #for random in range(ans+1):
                #    self.change_state()

            elif self.operators[self.state] == "*":
                ans = sum(list_n[:-states+(n*n)])
                print(f"rng_value = {sum(list_n[:-states+(n*n)])}")
                #for random in range(ans+1):
                #    self.change_state()

            elif self.operators[self.state] == "-":
                ans = sum(list_n[:-states+(n-n)])
                print(f"rng_value = {sum(list_n[:-states+(n-n)])}")
                #for random in range(ans+1):
                #    self.change_state()

            elif self.operators[self.state] == "/":
                #print(f"rng_value = {sum(list_n[-states+1])}")
                ans = 1
                print(f"rng_value = {1}")  
                #for random in range(ans+1):
                #    self.change_state()

        elif numbers_len == 2:
            print(f"Double digit number: ({n})")
            for _ in range((n//2)):
                if self.operators[self.state] == "0":
                    operator = 0
                    rng_ind += operator
                elif self.operators[self.state] == "+":
                    operator = (n/2)+(n/2)
                    rng_ind += operator
                elif self.operators[self.state] == "*":
                    operator = (n/2)*(n/2)
                    rng_ind += operator
                elif self.operators[self.state] == "-":
                    operator = (n/2)-(n/2)
                    rng_ind += operator
                elif self.operators[self.state] == "/":
                    operator = (n/2)/(n/2)
                    rng_ind += operator
            print(f"RNG VALUE: {2}")

        else:
            print("3-digit+ number:")
            numbers = str(n)
            list_of_numbers = []
            for single_number in numbers:
                 list_of_numbers.append(single_number)
            
            doubleDigit_total = 0
            for total in list_of_numbers:
                doubleDigit_total += total

            if doubleDigit_total <= 99:
                pass

            else:
                pass

    def print_state(self):
        print(f"END OF CODE - Current State: {self.state}, self.operators: {self.operators[self.state]}")




rn = input("Enter a number: ")
while not rn.isdigit():
    rn = input("Invalid input. Please enter a valid number: ")

rn = int(rn)
filler_size = 0

start = rng()
while start.initiate:
    start.change_state()

    if rn == filler_size:
        start.produce(rn)
        filler_size += 1
        continue
        #start.initiate = False
        #start.print_state()

    elif rn < filler_size:
        rn = input("Enter a number: ")
        while not rn.isdigit():
            rn = input("Invalid input. Please enter a valid number: ")
        
        rn = int(rn)
        filler_size = 0

    else:
        filler_size += 1
        if filler_size % rn == 0:
            start.change_state()
        elif filler_size % rn == 1:
            start.change_state()
            start.change_state()
        elif filler_size % rn == 2:
            start.change_state()
            start.change_state()
            start.change_state()

    #num = pressed button_value
    #start.produce(num)

    #start.rnd_generate = False