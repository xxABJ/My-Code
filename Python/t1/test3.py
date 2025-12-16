List = []

def cardwnumber():
    for number in range(5):
        quantity = "("+str(number+1)+"). "
        #odd_numbers = number * 2 + 1
        card = str(quantity) + str((len(List) * 2 + 1 ))
        List.append(card)

    return List

cardwnumber()
print(List)