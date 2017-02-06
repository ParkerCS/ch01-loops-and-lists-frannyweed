#LISTS (35PTS TOTAL)
#In these exercises you write functions. Of course, you should not only write the functions,
#you should also write code to test them. For practice, you should also comment your
#functions as explained above.

import random
#PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]
def magic(ask):
    i = (random.randrange(len(answer_list)))
    print(answer_list[i])
magic(input("Ask the magic 8-ball a question: "))

# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
shuffled = []
cards = []
suit = ["Heart", "Diamond", "Club", "Spade"]
value = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
for f in range(len(suit)):
    for e in range(len(value)):
        cards.append([suit[f],value[e]])

def shuffle():
    for i in range(len(cards)):
        order = random.randrange(len(cards))
        shuffled.append(cards[order])
        del[cards[order]]
shuffle()
print(shuffled)

# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.
sequence = []
number = int(input("Enter a number: "))
for i in range(1,number+1):
    sequence.append(i)
primes = []

def prime():
    sequence[0]= 0
    for j in range(1,len(sequence)-1):
        if sequence[j] != 0:
            for k in range(1,number):
                if sequence[k] != 0 and sequence[k] != sequence[j]:
                    if sequence[k] % sequence[j] == 0:
                        sequence[k] = 0
    for a in range(len(sequence)):
        if sequence[a] != 0:
            primes.append(sequence[a])

prime()
print(primes)
print("The prime numbers from 1 to " + str(number) + " are " + str(primes))

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
row = [1,2,3]
column = [1,2,3]
move = []
won = False
player1_won = False
player2_won = False

options = []
display = [(" " * 7 + "|"),(" " * 7 + "|"),(" " * 7),(" " * 7 + "|"),(" " * 7 + "|"),(" " * 7),(" " * 7 + "|"), (" " * 7 + "|"),(" " * 7),(" " * 7 + "|") * 2 + " " *7]
player_1 = []
player_2 = []

def plays():
    v2 = (" " * 7 + "|")
    v3 = (" " * 7 + "|")
    v4 = (" " * 7)
    v5 = (" " * 7 + "|")
    v6 = (" " * 7 + "|")
    v7 = (" " * 7)
    v8 = (" " * 7 + "|")
    v9 = (" " * 7 + "|")
    v10 = (" " * 7)
    if move[round] == [1,1]:
        if round % 2 == 0:
            v2 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v2 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(0)
        display.insert(0,v2)
    if move[round] == [1,2]:
        if round % 2 == 0:
            v3 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v3 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(1)
        display.insert(1,v3)
    if move[round] == [1,3]:
        if round % 2 == 0:
            v4 = " " * 3 + "x" + " " * 3
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v4 = " " * 3 + "o" + " " * 3
            player_2.append([ask_row, ask_column])
        display.pop(2)
        display.insert(2,v4)
    if move[round] == [2, 1]:
        if round % 2 == 0:
            v5 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v5 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(3)
        display.insert(3,v5)
    if move[round] == [2,2]:
        if round % 2 == 0:
            v6 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v6 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(4)
        display.insert(4,v6)
    if move[round] == [2,3]:
        if round % 2 == 0:
            v7 = " " * 3 + "x" + " " * 3
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v7 = " " * 3 + "o" + " " * 3
            player_2.append([ask_row, ask_column])
        display.pop(5)
        display.insert(5,v7)
    if move[round] == [3,1]:
        if round % 2 == 0:
            v8 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v8 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(6)
        display.insert(6,v8)
    if move[round] == [3,2]:
        if round % 2 == 0:
            v9 = " " * 3 + "x" + " " * 3 + "|"
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v9 = " " * 3 + "o" + " " * 3 + "|"
            player_2.append([ask_row, ask_column])
        display.pop(7)
        display.insert(7,v9)
    if move[round] == [3,3]:
        if round % 2 == 0:
            v10 = " " * 3 + "x" + " " * 3
            player_1.append([ask_row, ask_column])
        elif round % 2 == 1:
            v10 = " " * 3 + "o" + " " * 3
            player_2.append([ask_row, ask_column])
        display.pop(8)
        display.insert(8,v10)

def display_board():
    for l in range(9):
        if l == 2 or l == 5:
            print("_" * 7 + "|"+ "_" * 7 + "|"+ "_" * 7)
        elif l == 1:
            print(display[0] + display[1] + display[2])
        elif l == 4:
            print(display[3] + display[4] + display[5])
        elif l == 7:
            print(display[6] + display[7] + display[8])
        else:
            print(display[9])

def check(test):
    for m in range(len(test)):
        for k in range(len(test)):
            for l in range(len(test)):
                if test[l][0] == test[m][0] == test[k][0] and test[l][1] != test[m][1] and test[l][1] != test[k][1] and test[k][1] != test[m][1]:
                    return True
                elif test[l][1] == test[m][1] == test[k][1] and test[l][1] != test[m][1] and test[l][1] != test[k][1] and test[k][1] != test[m][1]:
                    return True
                if test[m] == [2, 2]:
                    if test[l] == [1, 1] and test[k] == [3,3] or test[l] == [1,3] and test[k] == [3,1]:
                        return True
    return False

round = -1
okay = False
show = False

while True:
    ask_row = int(input("Select a row: "))
    ask_column = int(input("Select a column: "))
    round += 1
    if round == 0:
        move.append([ask_row,ask_column])
        plays()
        display_board()
        continue
    for j in range(len(move)):
        if move[j] == [ask_row, ask_column]:
            print("That spot has already been taken. Try again")
            round -= 1
            continue
        else:
            okay = True
            show = True
    move.append([ask_row, ask_column])
    plays()
    display_board()
    if round % 2 == 0:
        check(player_1)
        if check(player_1) == True:
            print("Player 1 won!")
            break
    if round % 2 == 1:
        check(player_2)
        if check(player_2) == True:
            print("Player 2 won!")
            break