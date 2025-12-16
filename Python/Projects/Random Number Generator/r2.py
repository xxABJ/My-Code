class rng:
    def __init__(self):
        self.initiate = True

        self.dictionary = {
            "r1":{
                1:"a",#0
                2:"b",#1
                3:"c",#2
                4:"d",#3
                5:"e",#4
                6:"f",#5
                7:"g",#6
                8:"h",#7
                9:"i",#8
            },
            "r2":{
                1:"a",#0
                2:"b",#1
                3:"c",#2
                4:"d",#3
                5:"e",#4
                6:"f",#5
                7:"g",#6
                8:"h",#7
                9:"i",#8
            },
            "r3":{
                1:"a",#0
                2:"b",#1
                3:"c",#2
                4:"d",#3
                5:"e",#4
                6:"f",#5
                7:"g",#6
                8:"h",#7
                9:"i",#8
            },
        }

        self.r1_numbers = []
        for _ in self.dictionary["r1"].keys():
            self.r1_numbers.append(_)
        
        self.r1_letters = []
        for _ in self.dictionary["r1"].values():
            self.r1_letters.append(_)

        self.r2_numbers = []
        for _ in self.dictionary["r2"].keys():
            self.r2_numbers.append(_)
        
        self.r2_letters = []
        for _ in self.dictionary["r2"].values():
            self.r2_letters.append(_)

        self.r3_numbers = []
        for _ in self.dictionary["r3"].keys():
            self.r3_numbers.append(_)
        
        self.r3_letters = []
        for _ in self.dictionary["r3"].values():
            self.r3_letters.append(_)

        self.selector = 0

        self.numberlist = []

        self.oldnumber = 0
        self.oldletters = []

    def numberlist_generator(self, n):
        for _ in range(0,n+1):
            self.numberlist.append(_)
        self.oldnumber = n

start = rng()

def p():
    print(start.r1_numbers)
    print(start.r1_letters)
    print()
    print(start.r2_numbers)
    print(start.r2_letters)
    print()
    print(start.r3_numbers)
    print(start.r3_letters)
while start.initiate:
    p()
    break