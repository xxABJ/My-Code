# Useful functions related to numbers using the (import math) module!
import math

pi = 3.14
pi_abs = -3.14

a = 32
b = 135
c = 21
d = 124

# Print with the "round()" function to round a number to the nearest whole number:
print(round(pi))

# Print with the ".ceil" function within the math module to round up a number:
print(math.ceil(pi))

# Print with the ".floor" function within the math module to round down a number:
print(math.floor(pi))

# Print with the "abs" function to find the absolute number of a number:
print(abs(pi_abs))

# Print with the "pow" function to calculate to the power of a number:
print(pow(pi,3))

# Print with the ".sqrt" function within the math module to find the square root of a number:
print(math.sqrt(pi))

# Print with the "max" function to find the highest number between other numbers:
print(max(a,b,c,d))

# Print with the "mix" function to find the lowest number between other numbers:
print(min(a,b,c,d))
