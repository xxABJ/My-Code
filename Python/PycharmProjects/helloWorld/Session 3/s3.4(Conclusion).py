# Conclusion:

# Math functions is a way to do math stuff with python using the (import.math) function
# Example:

import math

a = 10
b = 35
c = 251
d = 34.23189515
e = -314855

# Print with the built-in "round" function to make a whole number by removing any decimals: (does not round up or down)
print(round(d))

# Print with the ".ceil" math function to round up a number:
print(math.ceil(d))

# Print with the ".floor" math function to round down a number:
print(math.floor(d))

# Print with the built-in "pow" function to make a number to the power of:
print(pow(a,2))

# Print with the ".sqrt" math function to square root a number:
print(math.sqrt(c))

# Print with the built-in "abs" function to find the absolute number of a number:
print(abs(e))

# Print with the built-in "max" function to find the largest number:
print(max(a,b,c,d,e))

# Print with the built-in "min" function to find the smallest number:
print(min(a,b,c,d,e))



# String slicing can be used to create a substring from a string. Types of slicing = indexing operator [] or slice()
# Can be used to select an amount of characters from a string, or how many positions to move before reading a string,
# and/or even reading a reversed string.
# Example:

name = "Steve Jobs"

# Print with the indexing operator [start] to select a certain position and read a character (starts with 0):
print(name[6])

# Print with indexing operator [start:stop] to select a portion of characters within a string (colon to separate types):
# REMEBER 'start' is inclusive and 'stop' is exclusive, add one more position for the exclusive.
print(name[0:5])
print(name[6:10])
# sc1 = A Shortcut to the above which means *start reading from the beginning and stop at the assigned position:
# sc2 = A Shortcut to the above which means *keep reading till the end of the string:
print(name[:5]) # sc1
print(name[6:]) # sc2

# Print with the indexing operator [start:stop:step], step = many positions to jump too before reading (default is 1):
print(name[0:10:1])
# sc3 = A Shortcut to the above which means *everything from the beginning till the end (in between).
print(name[::1]) # sc3
# Print with the same indexing operator, but step is jumping 2 positions before reading:
print(name[0:10:2])
# sc4 = A shortcut to the above which means *everything from the beginning till the end (in between).
print(name[::2]) # sc4

# Print with the indexing operator [start:stop:step], but making step = -1 (reading in reverse):
print(name[::-1])
# Can also jump to more than one position if the number is more than -1 (reading in reverse):
print(name[::-2])

# The slicing function "slice()":
# First number is a positive (left-to-right, inclusive), second number is a negative (right-to-left, exclusive):

website1 = "http://315.24.16.258.com/"
website2 = "http://gg.com/"
website3 = "https://www.shockbyte.com/account_login/"

# Print using the indexing operator by assigning an object first and then using the slicing function "slice()"
# to make a substring from a string.
slice1 = slice(7,-5)
print(website1[slice1])
print(website2[slice1])

# Print without assigning an object with a longer link name, still the same idea:
print(website3[slice(8,-15)])



# "if" statements can be used to check if a block of code is true.
# Can be followed by an "elif" statement to move on to another option.
# Finally, can be ended with an "else" statement to check if the block of code is false. AS A LAST RESORT

height = float(input("How tall are you in cm ?: "))

# Make sure to right the code in order, so it does not skip specific results!
# Print the results to the statements regarding the input:

if height < 0:
    print("How is that possible bro, you are negative height ? -.-")
elif height <= 180:
    print("You are allowed to ride the roller coaster!")
else:
    print("You are NOT allowed to ride the roller coaster!")



# Logical operators (and,or,not) = need conditional statements to give a result.
# 'and' need TWO or more conditional statements
# 'or' need ONE or more conditional statement
# 'not' need an operation and then it can flip it but adding (not) to it!

age = int(input("How old are you?: "))

# Make sure to right the code in order, so it does not skip specific results!
# Print the results to the statements regarding the input:

if age == 100:
    print("You have lived a century!")
elif age == 10:
    print("You have lived a decade!")
elif age < 0:
    print("Bro how are you negative years old?")
elif age <= 17 and age >= 12: # Numbers in between!
    print("You are a teenager and can go to on the field trip!")
elif age < 12 or age > 17:
    print("You do not meet the the age range to go on the field trip!")


# The 'not' operation will flip the statement:
# Print to see if you are a teenager:
print("Not using the 'not operation, SAME FUNCTIONS")
age2 = int(input("How old are you?: "))

if age2 >= 12 and age2 <= 17:
    print("You are a TEENAGER!")
elif age2 < 12 or age2 > 17:
    print("You are not a TEENAGER")

# Print to see if you are a teenager (flipped by adding brackets and a 'not' operation):
print("Using the 'not operation, SAME FUNCTIONS")
age3 = int(input("How old are you?: "))

if not (age3 >= 12 and age3 <= 17):
    print("You are a TEENAGER!")
elif not (age3 < 12 or age3 > 17):
    print("You are not a TEENAGER")

