# Conclusion of the session:
# Ability to multi assign variables in one line by adding a comma "," after each variable.
# Type casting is a function that changes data types indefinitely. Required for prints.
# Accepting inputs can be useful to store data from the user.

# Example of Multiple Assignemnt:
name, age, height = "Ali" , 25 , 169.8
# OR
steve = ali = john = 25 #Same values i.e ages!

print(name +" "+ str(age) +" "+ str(height))
print(steve)
print(ali)
print(john)

# Example of Type casting:
x = "10" #str
y = 12.3 #float
z = 15 #int

x = float(x)
z = float(z)

print("The total area is: "+ str(x*y*z) +" cm3 !")

#Example of Accepting User inputs
first_name = input("What is your name?: ")
middle_name = input("What is your middle name "+ first_name +" ?: ")
last_name = input("And your last name Mr. "+ middle_name +" ?: ")

#Example of type casting for successful Concatenation with print strings:
the_age = int(input("What is your age Mr. "+ middle_name +" ?: "))
the_height = float(input("And your height ?: "))

print("Alrighty, Time to test this out !")
print("Your full name is: "+ first_name +" "+ middle_name +" "+ last_name)
print("Also, you are "+ str(the_age) +" years old, and "+ str(the_height) +" cm tall !")
