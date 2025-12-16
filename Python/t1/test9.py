import math
def add_binary(a,b):
    
    dynamic = 2
    binary_numbers = [128,64,32,16,8,4,2,1]
    decimal = a+b
    binary_str = ""
    
    if decimal % 2 == 1:
        decimal - 1
    
    for i in range(decimal):
        dynamic**i
        if math.sqrt(dynamic) < decimal < dynamic:
            break
    
    while decimal > 1:
        if decimal % dynamic == 0 and decimal / dynamic == 1:
            binary_str += "1"
        elif dynamic/2 < decimal < dynamic:
            binary_str += "1"
            decimal -= dynamic/2
            dynamic/=2
        elif decimal == 1:
            binary_str += "1"
        else:
            binary_str += "0"
    
    return f'{int(binary_str[1::])}'

add_binary(32,31)