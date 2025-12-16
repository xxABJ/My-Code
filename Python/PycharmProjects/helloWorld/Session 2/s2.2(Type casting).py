# Type casting = is the ability to convert a data type of value to another data type value.
# Useful if you want to concatenate with stings.

a = 1 #int
b = 2.6 #float
c = "3" #str

# Add a concatenation to change data type indefinitely:

# a = float(a)
# c = float(c)

# print(a)
# print(b)
# print(c)

# Converting to whole number will NOT round to nearest whole number, but would simply remove the
# decimal point:

# b = int(b)

# print(b)

# Very useful if you want to print the values while combined with a string:
# Type casting before concatenating the print code:

#Type casting:
a = str(a)
b = str(b)
c = str(c) # <- This is not needed due to the variable "c" being a string initially.

#Concatenating with a string:
print("a is equal to: " +a)
print("b is equal to: " +b)
print("c is equal to: " +c)
