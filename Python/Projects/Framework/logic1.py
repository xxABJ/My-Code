def normal_sums(num: list, power) -> list:
    # Logic1
    """

    *Normal Sums* value

    The resulting amount of numbers generated depends on the power. These numbers will be used in the next step.

    """


    normal_sums = []

        
    if len(num) == 1:

        a1 = num[0]
        print(a1)


        normal_sum = 1
        for denominator in range(power, 0, -1):

            normal_sum *= ((a1 * 1) / denominator) * 1
            print()
            print(denominator)
            print(normal_sum)

            normal_sums.append(normal_sum)


    elif len(num) == 2:
        
        a1 = num[0]
        a2 = num[1]
        print(a1)
        print(a2)

        
        normal_sum = 1
        for denominator in range(power, 0, -1):

            normal_sum *= ((a1 * 1) / denominator) * a2
            print()
            print(denominator)
            print(normal_sum)

            normal_sums.append(normal_sum)
        

    elif len(num) == 3:
        
        a1 = num[0]
        a2 = num[1]
        a3 = num[2]
        print(a1)
        print(a2)
        print(a3)
        

        normal_sum = 1
        for denominator in range(power, 0, -1):

            normal_sum *= ((a1 * a2) / denominator) * a3
            print()
            print(denominator)
            print(normal_sum)

            normal_sums.append(normal_sum)



    elif len(num) > 3:
        return "Too many numbers, only 3 allowed" #TODO: make it so that it can take more than 3 numbers, but for now just 3
    

    print("\nNormal Sums: ")
    print(normal_sums)

    print("\nTotal Sum: ")
    print(normal_sum)

    len_normal_sums = len(normal_sums)

    return normal_sums, len_normal_sums
        

print(normal_sums([5], 3)) 