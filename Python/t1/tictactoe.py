def print_board(board):

    for y, row in enumerate(board): # row = contents of board, which are 3 lists.
        row_str = ""
        
        for x, cols in enumerate(row): # cols = contents of lists in side of board, which are 3 strings.
            row_str += cols
            if x != len(row) - 1:
                row_str += " | "

        print(row_str)
        if y != len(board) - 1:
            print("----------")

def turn(board,players):
    
    player = players["name"]
    sym = players["symbol"]
    print(f"Player {player}'s turn!")

    while True:
        while True:
            row = input("Which row?: ")
            try:
                row.isdigit()
                if 0 <= int(row) - 1 > 2:
                    print("Invalid number of row.")
                else:
                    break
            except:
                print("Not a valid answer.")

        while True:
            col = input("Which col?: ")
            try:
                col.isdigit()
                if 0 <= int(col) - 1 > 2:
                    print("Invalid number of column.")
                else:
                    break
            except:
                print("Not a valid answer.")
        
        selected = board[int(row)-1][int(col)-1]

        if selected != " ":
            print("Not an empty place!")
        else: 
            board[int(row)-1][int(col)-1] = sym
            return

def player(players):

    while True:
        print("Please choose a player name:")
        name = input("-> ")

        if len(players) < 1:
            playername = {"name": name, "symbol": "X"}
            return players.append(playername)
        else:
            playername = {"name": name, "symbol": "Y"}
            return players.append(playername)

def detect_win(board):
    
    detect_win = [
        [[0,0],[0,1],[0,2]],
        [[1,0],[1,1],[1,2]],
        [[2,0],[2,1],[2,2]],
        [[0,0],[1,0],[2,0]],
        [[0,1],[1,1],[2,1]],
        [[0,2],[1,2],[2,2]],
        [[0,0],[1,1],[2,2]],
        [[0,2],[1,1],[2,0]]
    ]

    X = "X"
    Y = "Y"
    win = X or Y

    for i, detect_win[:][:] in enumerate(board):
        if win in i:
            return True

def tictactoe():
    
    while True:
        player(players)

        if len(players) == 2:
            break
    
    print_board(board)

    for game in range(8):
        winner = 0
        turn(board,players[0]) and winner
        print_board(board) and winner + 1
        turn(board,players[1]) and winner
        print_board(board) and winner - 1

        if detect_win(board):
            print("We have a winner!")
            if player == 0:
                return print(player[0])
            else:
                return print(player[1])
    
    return print("Nobody won :'(")

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

#detect_win = [
#        ([0,0],[0,1],[0,2]),
#        ([1,0],[1,1],[1,2]),
#        ([2,0],[2,1],[2,2]),
#        ([0,0],[1,0],[2,0]),
#        ([0,1],[1,1],[2,1]),
#        ([0,2],[1,2],[2,2]),
#        ([0,0],[1,1],[2,2]),
#        ([0,2],[1,1],[2,0])
#]

players = []

tictactoe()






#print_board(board)



#for rows, line in enumerate(board):
#
#    row = rows[line]
#
#    if rows != len(line) - 1:
#        print("------------")
#
#    for cols in enumerate(line):
#        
#        col = [cols]
#        
#        print("a")
#        #pass
#        #print(row + "|")
#
#        #if cols != len(row) - 1:
#        #    print("|")
#        #if rows != len(row) - 1:
#        #    print("------------")


#b = board[][]
#print(col)
#print
# print(board)
#print(board[2][1])
#print(board[2][2])

    #print(board[rows])
    #if rows != len(row) - 1:
    #    print("------------")
    #for cols, col in enumerate(row):
    #    if cols != len(row) - 1:
    #        print("|")

#for rows, row in enumerate(board):
#    print(board[rows])
#    if rows != len(row) - 1:
#        print("------------")
#    for col in enumerate(row):
#        if col != len(col) - 1:
#            print("|")     
#board[rows][cols]
#print(board)