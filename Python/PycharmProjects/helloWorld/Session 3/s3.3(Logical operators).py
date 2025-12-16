# Logical operators (and,or,not) = can be used to check if the conditional statement is true.
# The "and" operator needs to have TWO or more "conditional statements" as true.
# The "or" operator needs to have ONE or more "conditional statement" as true.

# Example "and,or":

print("Without using the (not) operator, SAME FUNCTIONS")
age = int(input("How old are you?: "))

# Print will succeed if BOTH statements are true by using the "and" operator:
if age >= 12 and age <= 17:
    print("You are a teenager !")

# Print will succeed if ONE statement are true by using the "or" operator:
elif age < 12 or age > 17:
    print("You are not a teenager !")


# The "not" operator needs to have ONE or more "conditional statements" as true but it will flip the statement.
# Therefore is can be used to reverse the whole statement if needed.

# Example "not":

print("Using the (not) operator, SAME FUNCTIONS")
age2 = int(input("(age2) How old are you?: "))

# Print with the "not" regarding the same statements. Brackets are required and the results are flipped there for
# printed message need to be fixed to make sense of the subject variable (age).
if not (age2 >= 12 and age2 <= 17):
    print("You are a teenager !")
elif not (age2 < 12 or age2 > 17):
    print("You are not a teenager !")