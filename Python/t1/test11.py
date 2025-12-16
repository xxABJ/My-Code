import sys
sys.set_int_max_str_digits(60000)

n = 5750
d = 0

def nb_dig(n, d):
    squared = []
    count = 0
    for i in range(n+1):
        squared.append(i**i)
        squared = str(squared).replace("[", "").replace("]","")
        if str(d) in squared:
            count += 1
        squared = []
    
    #count = 0
    #for i in squared:
    #    if str(d) in i:
    #        count += 1
    return print(count)

nb_dig(n, d)