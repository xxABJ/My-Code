import math

#while
#    for
#        while

def print_maze():
    for row in maze:
        print(row)

#maze = {}
#for row in range(10):
#    default_row = row
#    maze = {row:"row"}
#    for col in range(10):
#        maze[row] = {col: ["col" , {(row, col): "e"}]}
#        row += 1
#    row = default_row
#
#maze = {"row": {"col"+str(col): [(row, col), "e"] for col in range(10)} for #row in range(10)}

size = 80
s = int(math.sqrt(size))
maze = {"row"+str(row): {"col"+str(col): ["e", (row, col)] for col in range(s)} for row in range(s)}

#maze = {row: {col: ["e", (row, col)] for col in range(s)} for row in range(s)}

print()
#space = " "
#columns_names = []
#for rows in maze:
#    for key, value in maze[rows].items():
#        columns_names.append(key)
#        break
#col_space = "      "
#for cols in columns_names:
#    print(f"{col_space}{cols}  ", end=space)
#    globals
#    col_space = ""
#for rows in maze:
#    print(f"\n{rows}    ", end=space)
#    for cols in maze[rows]:
#        for i in range(1):
#            print(f"{maze[rows][cols]}     ", end=space)

# do a better job to manipulate the printing of the maze
# print column names
columns_names = []
for rows in maze:
    for key, value in maze[rows].items():
        columns_names.append(key)
    break
col_space = "           "
for cols in columns_names:
    print(f"{col_space}{cols}  ", end=" ")
    col_space = "         "
# print rows with their values
for rows in maze:
    print(f"\n{rows}  ", end=" ")
    for cols in maze[rows]:
        print(f"{maze[rows][cols]}  ", end=" ")


print()
print()

for row in maze:
    for col in maze[row]:
        print(f"{maze[row][col][0]}", end="  ")
    print()

print()
for row in maze:
    for col in maze[row]:
        print(f"{maze[row][col][1]}", end="  ")
    print()


print("\n------------------")
print(maze)