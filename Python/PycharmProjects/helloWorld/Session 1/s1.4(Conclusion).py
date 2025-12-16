# Conclusion to the session:
# A variable is a placeholder to store data types, it can be a string, an integer or a boolean !
## A variable is a container for a value. ##
# A string (str) is a series of characters !
# An integer (int) is a numeral data type that can store whole numbers only !
# A float (float) is a numeral data type that can ALSO store decimal portions !
# A Boolean (bool) is a data type that can store to values only; True or False !

# Example of a variable:
area = "71"
street = "127"
door = "9"

print(type(area))
print("Your Area code is: " +area)
print("Your Street number is: " +street)
print("Your Door number is: " +door)

# Example of an integer: (please note that this is just an example, minutes does not go to 100!)
time = 630
time_dif = 300

print(type(time))
print(time + time_dif)
# Printing with a string (string concatenation = adding +str to print without errors):
print("Your home time is " + str(time) + " and the time difference is + " + str(time_dif) + " hours.")
print("So we can basically add it together which will give us: " + str(time+time_dif))

# Example of a float:
pi = 3.14

print(type(pi))
print(pi)
# Printing with a string (string concatenation = adding +str to print without errors):
print("PI can be rounded up to the nearest 2 decimal places. That is: " + str(pi))

# Example of a boolean:
adult = True

print(type(adult))
print(adult)
# Printing with a string (string concatenation = adding +str to print without errors):
print("Are you an adult?: " + str(adult))