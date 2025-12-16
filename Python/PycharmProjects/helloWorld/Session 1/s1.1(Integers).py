# int = Integer which is a whole number.
# Make sure that you assign an int WITHOUT speech marks!

age = 25
# (age = age + 1)
# or shortcut it like this:
age += 1
print(age)
print(type(age))

# Will not work if you try to do it as a string (TypeError), delete ## to see
##age2 = "25"
##age2 += 1
##print(age2)

# Trying to print a string variable with an int variable will not work
# Because you will need to convert the int variable to a string before
# able to print them! (TypeError), delete ## to see
# Example:

##age3 = 25
##print("Your age is: "+age3)

# You can fix it by type casting:

age4 = 25
age4 += 1
print("Your age is: "+str(age4))