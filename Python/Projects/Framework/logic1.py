def Logic1(num, power):



    if type(num) == list:
        
        if len(num) == 2:
           
            a1 = num[0]
            a2 = num[1]

            print(a1)
            print(a2)

            if type(power) == int:
            
                normal_sum = 1
                for denominator in range(power, 0, -1):

                    normal_sum *= ((a1 * 1) / denominator) * a2
                    print("\n",normal_sum)
                
                print("hello")
                return normal_sum
            

            else:
                pass


        else:
            pass


    else:
        pass


print(Logic1([5, 4], 2)) 
