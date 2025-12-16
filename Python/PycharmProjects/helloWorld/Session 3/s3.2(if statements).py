# if statement = is a block of code that will only execute if the condition is true. The statement ends with a ":" colon.
# Can be followed by an elif to move on to the next option for the "block of code".
# Finally, it can be ended by an else statement to the "block of code" when the condition is false.
# (if) is for first option, (elif) is for next option and (else) is for the last resort!

# Example:

name = input("Hello! What is you name?: ")
age = int(input("Hello "+ name +", How old are you?: "))

if age >= 18:
    print("You are an adult "+ name +" !")
elif age < 0:
    print(name +" ... you either are not born or you are trolling.")
elif age == 100:
    print("You are a century old "+ name +" !") # If you try to print this by inputting 100, you will not get it printed
                                                # because positioning matters in python. So you have to rearrange like the
                                                # below "block of code" **ADD # TO THE TOP FIRST**
else:                                           #                       __
    print("You are not an adult")               #                       ||
                                                #                       ||
#################################################                      _||_
# Rearraging (Example) to fit the answers of the if statements:        \  /
#                                                                       \/
if age == 100:
     print("You are a century old "+ name +" !")
elif age >= 18:
     print("You are an adult "+ name +" !")
elif age < 0:
     print(name +" ... you either are not born or you are trolling.")
else:
     print("You are not an adult")
