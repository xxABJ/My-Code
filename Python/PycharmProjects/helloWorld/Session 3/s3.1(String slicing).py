# String slicing = slicing can be referred to creating a substring by extracting elements from
# another string. The slicing principle can be applied to different collection as well.
# Can be made by using the index operator: indexing[]
# Or can be made by using the slice function: slice() to create a slice object.

# The format of indexing is [start:stop:step] by using a number to assign the position of the
# characters desired.

name = "Ali Jassim"

# Print using the index operator "[start]":
first_name = name[0]
print(first_name)

# Even though this might make sense that it should print the first 3 characters, it won't because
# the starting index is INCLUSIVE and the stopping index is EXCLUSIVE !!
# Print using the index operators "[start:stop]". A colon is needed to separate & assign:
first_name = name[0:2]
print(first_name)

# Due to the last note, we added one position to the desired slice.
# to the desired slice.
# Print using the index operators "[start:stop]":
first_name = name[0:3]
print(first_name)

# Print with a shortcut which means everything from the beginning to the selected position:
first_name = name[:3]
print(first_name)

# Print using an extra slicing for a last name (add one because EXCLUSIVE):
last_name = name[4:11]
print(last_name)

# Print with a shortcut which means everything from the selected position to the end:
last_name = name[4:]
print(last_name)

# Step index operator is the allocation of how many positions to move before reading a character.
# Default number of step is [::1], so it reads every other character.
# Print a slice using the index operator "[start:stop:step]" with the default step value:

random_name = name[0:11:1]
print(random_name)

# Print a slice using the indexing operator "[start:stop:step]" with another step value meaning it
# moves 2 positions before reading the character:
random_name = name[0:11:2]
print(random_name)

# Print using a shortcut regarding the above indexing operator which means the whole variable:
random_name = name[::2]
print(random_name)


# Print using a feature that can reverse a variable regarding the indexing operator; (-1):
reversed_name = name[::-1]
print(reversed_name)

# Moving on to the slice function "slice()",  we can use this function to remove extra characters on a website link.
# Example:

website1 = "http://google.com"
website2 = "https://www.shockbyte.com"

# Using the slice function combined with the indexing operator by taking the variable and adding the square brackets
# followed by the slice function brackets.
# The slice function works similar to the indexing operator. It counts how much INCLUSIVE and EXCLUSIVE positions you
# need by moving "left to right" with positive numbers and moving "right to left" with negative numbers.

# Print using the slice function to separate the name of the website link:
print(website1[slice(7,-4)])

# Print using another variable with a longer link name, still the same idea:
print(website2[slice(12,-4)])
