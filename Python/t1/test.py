while True:  
    a: str = input("-> ")
    
    if not a.isdigit():
        
        decimal_point: str = '.'
        dp = 0
        
        for decimal_point, char in enumerate(a):
            if decimal_point:
                dp += 1
            
        if 0 < dp < 2:
            print("has a decimal point")
            dp = 0

        else:
            print("invalid input")

    else:
        print("does not have a decimal point")

#if a.isdigit():
#    print("counts as a float")
#else:
#    print("does not count as a float")