# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.
row = [1, 2, 3]
column = [1, 2, 3]
options = []
move = []

#def player1():
   # display_board("")
#def opponent():
    #display_board("o")
def display_board():
    v = (" " * 7 + "|") * 2 + " " * 7
    v2 = (" " * 7 + "|")
    v3 = (" " * 7 + "|")
    v4 = (" " * 7)
    v5 = (" " * 7 + "|")
    v6 = (" " * 7 + "|")
    v7 = (" " * 7)
    v8 = (" " * 7 + "|")
    v9 = (" " * 7 + "|")
    v10 = (" " * 7)
    if round != 0:
        for c in range(round):
            if move[c] == [[1], [1]]:
                if round % 2 == 0:
                    playerv2 = "x"
                    v2 = " " * 3 + playerv2 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv2 = "o"
                    v2 = " " * 3 + playerv2 + " " * 3 + "|"
            elif move[c] == [[1], [2]]:
                if round % 2 == 0:
                    playerv3 = "x"
                    v3 = " " * 3 + playerv3 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv3 = "o"
                    v3 = " " * 3 + playerv3 + " " * 3 + "|"
            elif move[c] == [[1], [3]]:
                if round % 2 == 0:
                    playerv4 = "x"
                    v4 = " " * 3 + playerv4 + " " * 3
                elif round % 2 == 1:
                    playerv4 = "o"
                    v4 = " " * 3 + playerv4 + " " * 3
            elif move[c] == [[2], [1]]:
                if round % 2 == 0:
                    playerv5 = "x"
                    v5 = " " * 3 + playerv5 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv5 = "o"
                    v5 = " " * 3 + playerv5 + " " * 3 + "|"
            elif move[c] == [[2], [2]]:
                if round % 2 == 0:
                    playerv6 = "x"
                    v6 = " " * 3 + playerv6 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv6 = "o"
                    v6 = " " * 3 + playerv6 + " " * 3 + "|"
            elif move[c] == [[2], [3]]:
                if round % 2 == 0:
                    playerv7 = "x"
                    v7 = " " * 3 + playerv7 + " " * 3
                elif round % 2 == 1:
                    playerv7 = "o"
                    v7 = " " * 3 + playerv7 + " " * 3
            elif move[c] == [[3], [1]]:
                if round % 2 == 0:
                    playerv8 = "x"
                    v8 = " " * 3 + playerv8 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv8 = "o"
                    v8 = " " * 3 + playerv8 + " " * 3 + "|"
            elif move[c] == [[3], [2]]:
                if round % 2 == 0:
                    playerv9 = "x"
                    v9 = " " * 3 + playerv9 + " " * 3 + "|"
                elif round % 2 == 1:
                    playerv9 = "o"
                    v9 = " " * 3 + playerv9 + " " * 3 + "|"
            elif move[c] == [[3], [3]]:
                if round % 2 == 0:
                    playerv10 = "x"
                    v10 = " " * 3 + playerv10 + " " * 3
                elif round % 2 == 1:
                    playerv10 = "o"
                    v10 = " " * 3 + playerv10 + " " * 3
    for l in range(9):
        if l == 2 or l == 5:
            print("_" * 7 + "|" + "_" * 7 + "|" + "_" * 7)
        elif l == 1:
            print(v2 + v3 + v4)
        elif l == 4:
            print(v5 + v6 + v7)
        elif l == 7:
            print(v8 + v9 + v10)
        else:
            print(v)
round = 0
display_board()


for k in range(len(row)):
    for m in range(len(column)):
        options.append([row[k], column[m]])
print(options)
complete = 0
ask_row = int(input("Select a row: "))
ask_column = int(input("Select a column: "))
move.append([[ask_row], [ask_column]])
display_board()
done = False
won = False
while not done:
    ask_row = int(input("Select a row: "))
    ask_column = int(input("Select a column: "))
    round += 1
    for j in range(len(move)):
        if move[j] == [[ask_row], [ask_column]]:
            print("That spot has already been taken. Try again")
            round -= 1
        else:
            move.append([[ask_row], [ask_column]])
    display_board()
    for m in range(len(move)):
        for k in range(len(move)):
                for l in range(len(move)):
                    if move[l][0] == move[m][0] == move[k][0] and move[l] != move[m] and move[l] != move[k] and move[k] != move[m]:
                        won = True
                    elif move[l][1] == move[m][1] == move[k][1] and move[l] != move[m] and move[l] != move[k] and move[k] != move[m]:
                        won = True
                    if move[m] == [[2],[2]]:
                        if move[l] == [[1],[1]] and move[k] == [[3],[3]] or move[l] == [[1],[3]] and move[k] == [[3],[1]]:
                            won = True
                            #done = True
    for u in range(len(move)):
        for v in range(len(options)):
            if move[u] == options[v]:
                complete += 1
    if complete == 10:
        print("You draw - no one wins")
        break


    #if won == True:
        #print("You won!")
       # del(move[:])
      #  round = -1
    # while True:
    #   ask for row
    #   ask for column
    #       if row/column already occupied:
    #           display error
    #   place player marker in row/col
    #   display board
    #   check for winner:
    #       announce winner
    #       break
    #   check board full:
    #       announce draw
    #       break
    #   switch player