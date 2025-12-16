# String methods!
# A few useful methods and features available for stings!

name = "ali jassim"

# Print with "len()" method to find the length of the string:
print(len(name))

# Print with ".find" method to see what place is your selected letter (will find the first only):
# Also, computers always start counting from 0 !!
print(name.find("i"))

# Print with ".capitalize()" method to add a capital letter to the first word in the string:
print(name.capitalize())

# Print with ".upper()" method to make the string upper case:
print(name.upper())

# Print with ".lower()" method to make the string lower case:
print(name.lower())

# Print with ".isdigit()" method to check if the string is fully a number:
print(name.isdigit())

# Print with ".isaplha()" method to check if the string is only alphabetical characters without
# any spaces or numbers, only letters:
print(name.isalpha())

# Print with ".count()" method to count how many characters are present in the string
# from the selected choice:
print(name.count("s"))

# Print with ".replace()" method to replace a certain character to a new selected one
# in that order, having a comma "," in between (every possible match):
print(name.replace(" ","-"))

# Print with "*(any number)" feature to clone the string as many as the selected number:
print(name*5)
