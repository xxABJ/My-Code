# Accepting User inputs = the ability to collect user inputs by using the "input()" function.
# The value is then stored and available to be used.

# Enabling the function of storing an input from a user, after the comment ends:
input("Can you drive?: ")

# Print with the function to demonstrate the stored value.
country = input("Where were you born?: ")

print("You were born in, "+ country)

# Printing with different data types ALWAYS have to be type casted beforehand.
# Example:

first_name = input("What is your first name?: ")
last_name = input("What is your last name "+ first_name +" ?: ")

#age = input("How old are you "+first_name"?: ") <- will not concatenate without type casting!!
age = int(input("How old are you "+ first_name +" ?: ")) # type casting = "int(input)" or float

# This will work because "age" has been type casted on line 19.
age = 220 - age

print("Hello Mr "+ first_name +" "+ last_name +",")
print("Your estimated maximum heart rate should be around: "+ str(age) +" HB/s !")
