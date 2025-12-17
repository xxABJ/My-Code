import json, os, random

def print_maze():
    for row in maze:
        print(row)

maze = []
for row in range(10):
      maze.append([])
      for col in range(10):
          maze[row].append([])

for col in maze[0]:
    end = random.randint(0, len(maze[0])-1)
    maze[0][end] = ["E"]
    break

#for col in maze[-1]:
#    start = random.randint(0, len(maze[-1])-1)
#    maze[-1][start] = ["S"]
#    break
le = 0; re = len(maze[0])-1
side = random.choice([le, re])
maze[-1][le] = ["S"]

up = "up" #-1
down = "down" #+1
right = "right" #+1
left = "left" #-1

#"↑", "↓", "→", "←"
#t = 1
complete = False
limit = 0
while limit < 10*10:

    marker = []
    for row, col in [(row, col) for row in range(len(maze)) for col in range (len(maze[0]))][::-1]: # Main-condition
        limit += 1
        direction = random.choice([up, right])
        #print(f"row: {row}, col: {col}")
        
        #if maze[row][col] == ["m"] and col == 0:
        #    print("left edge marker")
        #    direction = random.choice([up, right])
        #    if direction == up:
        #        print(up, "marker")
        #        maze[row-1][col] = ["m"]
        #        #marker = maze[row-1][col]
        #        marker = (row-1, col)
        #    elif direction == right:
        #        print(right, "marker")
        #        maze[row][col+1] = ["m"]
        #        #marker = maze[row][col+1]
        #        marker = (row, col+1)
        #
        #if maze[row][col] == ["S"] and col == 0:# or col == len(maze[0])-1:
        #    print("left edge")
        #    direction = random.choice([up, right])
        #    if direction == up:
        #        print(up)
        #        maze[row-1][col] = ["m"]
        #        #marker = maze[row-1][col]
        #        marker = (row-1, col)
        #    elif direction == right:
        #        print(right)
        #        maze[row][col+1] = ["m"]
        #        #marker = maze[row][col+1]
        #        marker = (row, col+1)

        # This way assigner is based on the order of code execution [ :'( ] @TODO: Try to change how it is based on. Is this nessecary? @LINE: 74 & 125 for a working assigner?
        while True: # Random from a start point. Temp?
            if maze[row][col] == ["S"] and (col == 0 or col == len(maze[0])-1):
                if col == 0:
                    print("left edge")
                    #direction = random.choice([up, right])
                    ups = -1
                    rights = 1
                    lefts = -1
                    if direction == up:
                        while direction == up:
                            print(up)
                            maze[row+ups][col] = ["u"]
                            marker.append((row+ups, col))
                            direction = random.choice([up, right, left])
                            ups -= 1
                            #### NO DIRECTION FOR IF: the choice is |right| , so *Main-condition keeps on running and "var: limit" reachs the limit. ###
                            if direction == left:
                                print(right, "- breaking up")
                                maze[row+ups][col+rights] = ["r"]
                                marker.append((row+ups, col+rights))
                                break
                    if direction == right:
                        while direction == right:
                            print(right)
                            if ups == -1:
                                maze[row][col+rights] = ["r"]
                                marker.append((row, col+rights))
                            else:
                                maze[row+ups][col+rights] = ["r"]
                                marker.append((row+ups, col+rights))
                            direction = random.choice([up, right, left])
                            rights += 1
                            #### NO DIRECTION FOR IF: the choice is |up| , so *Main-condition keeps on running and "var: limit" reachs the limit. ###
                            if direction == left:
                                if ups == -1:
                                    print("(UP) no ups movement- breaking right")
                                    maze[row+ups][col+rights] = ["u"]
                                    marker.append((row+ups, col+rights))
                                elif ups < -1 and rights > 1:
                                    ups -= 1
                                    print("(UP) ups and rights movement - breaking right")
                                    maze[row+ups][col+rights] = ["u"]
                                    marker.append((row+ups, col+rights))
                                else:
                                    ups -= 1
                                    print("(UP) ups - breaking right")
                                    maze[row+ups][col+rights] = ["u"]
                                    marker.append((row+ups, col+rights))
                                #maze[row+ups][col+rights] = ["m_u"]
                                #marker.append((row+ups, col+rights))
                                break
                
                #@TODO: complete right edge movement
                elif col == len(maze[0])-1:
                    print("right edge")
                    direction = random.choice([up, left])
                    ups = -1
                    if direction == up:
                        while direction == up:
                            print(up)
                            maze[row+ups][col] = ["u"]
                            marker.append((row-ups, col))
                            direction = random.choice([up, left])
                            ups -= 1
                    if direction == left:
                        if ups == -1:
                            print(left)
                            maze[row][col-1] = ["l"]
                            marker.append((row, col-1))
                        else:
                            print(left)
                            maze[row+ups][col-1] = ["l"]
                            marker.append((row+ups, col-1))

                #@TODO: Fix marker assignment display
                ## Currenty for left edge only ##
                if marker:
                    print("marker:", marker, "\n")
                    for (row, col) in marker:
                        if maze[row][col] == ["u"]:
                            maze[row][col] = ["↑"]
                        elif maze[row][col] == ["r"]:
                            maze[row][col] = ["→"]
                        elif maze[row][col] == ["l"]:
                            maze[row][col] = ["←"]

            break

                        #if ups == -1:
                        #    print(right)
                        #    maze[row][col+rights] = ["m_r"]
                        #    marker.append((row, col+rights))
                        #else:
                        #    print(right)
                        #    maze[row+ups][col+rights] = ["m_r"]
                        #    marker.append((row+ups, col+rights))

        #if maze[row][col] == ["m"] and col == len(maze[0])-1:
        #    print("right edge marker")
        #    direction = random.choice([up, left])
        #    if direction == up:
        #        print(up, "marker")
        #        maze[row-1][col] = ["m"]
        #        #marker = maze[row-1][col]
        #        marker = (row-1, col)
        #    elif direction == left:
        #        print(left, "marker")
        #        maze[row][col-1] = ["m"]
        #        #marker = maze[row][col-1]
        #        marker = (row, col-1)

        #if maze[row][col] == ["S"] and col == len(maze[0])-1:
        #    print("right edge")
        #    direction = random.choice([up, left])
        #    if direction == up:
        #        print(up)
        #        maze[row-1][col] = ["m"]
        #        #marker = maze[row-1][col]
        #        marker = (row-1, col)
        #    elif direction == left:
        #        print(left)
        #        maze[row][col-1] = ["m"]
        #        #marker = maze[row][col-1]
        #        marker = (row, col-1)

        #if maze[row][col] == ["S"] and col == len(maze[0])-1:
        #    print("right edge")
        #    direction = random.choice([up, left])
        #    if direction == up:
        #        print(up)
        #        maze[row-1][col] = ["↑"]
        #    elif direction == left:
        #        print(left)
        #        maze[row][col-1] = ["←"]
        #break

        #if marker:
        #    print("marker:", marker)
        #    for assigning in marker:
        #        if maze[assigning[0]][assigning[1]] == "u":
        #            maze[assigning[0]][assigning[1]] = "↑"
        #        elif maze[assigning[0]][assigning[1]] == "r":
        #            maze[assigning[0]][assigning[1]] = "→"
        #        elif maze[assigning[0]][assigning[1]] == "l":
        #            maze[assigning[0]][assigning[1]] = "←"

                #elif direction == down:
                #    breakpoint()
                #    print_maze()
                #    maze[marker[0]][marker[1]] = ["↓"]
                #    print()
                #    print_maze()
                #    print()
                #elif direction == right:
                #    breakpoint()
                #    print_maze()
                #    maze[marker[0]][marker[1]] = ["→"]
                #    print()
                #    print_maze()
                #    print()
                #elif direction == left:
                #    breakpoint()
                #    print_maze()
                #    maze[marker[0]][marker[1]] = ["←"]
                #    print()
                #    print_maze()
                #    print()

        #print(marker)
        #marker = []
        
        if len(maze[row][col]) == 0:
            maze[row][col] = ["."]
            #print(". added")

print()
print_maze()