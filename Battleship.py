import random 
from random import randint

print ("Wellcome to Battleship!", end="\n\n")

#initializing board

board = []
header = []
column1 = []

emptySpaceBoard = "."
missedSpaceBoard = "o"
hitSpaceBoard = "x"

for x in range(10):                 #setting the board 
      board.append([emptySpaceBoard] * 11)

import string                       #creating the header of letters
string.ascii_uppercase
header = list(string.ascii_uppercase)
header = list(map(chr, range(65,75)))
header.insert(0, "  ")
board.insert(0, header)             #header complete

for y in range(10):                 #1st column initialization
      if y <= 8:
            board[y+1][0] = " " + str(y+1)
      else:
            board[y+1][0] = str(y+1) #1st column complete
      
for row in board:                   #inserting vertical separators of cells in board
      print("|".join(row), end="|\n")


#Inserting ship

import random

randomNumber1 = random.randint(1,10)

if randomNumber1%2 == 0:            #horizontal arrangement
      randomNumber2 = random.randint(1,10)

      shipPosit1row = randomNumber2          #1st block of ship
      shipPosit1col = random.choice(header[1:6])

      shipPosit2row = shipPosit1row     #2nd block of ship
      shipPosit2col = chr(ord(shipPosit1col) + 1)

      shipPosit3row = shipPosit2row     #3rd block of ship
      shipPosit3col = chr(ord(shipPosit2col) + 1)

      shipPosit4row = shipPosit3row     #4th block of ship
      shipPosit4col = chr(ord(shipPosit3col) + 1)

      SHIP = [[shipPosit1row, shipPosit1col],[shipPosit2row, shipPosit2col], \
        [shipPosit3row, shipPosit3col],[shipPosit4row, shipPosit4col]]

      
else:                               #vertical arrangement
      randomNumber2 = random.randint(1,6)
      
      shipPosit1row = randomNumber2          #1st block of ship
      shipPosit1col = random.choice(header[1:6])

      shipPosit2row = shipPosit1row + 1    #2nd block of ship
      shipPosit2col = shipPosit1col

      shipPosit3row = shipPosit2row + 1    #3rd block of ship
      shipPosit3col = shipPosit1col

      shipPosit4row = shipPosit3row + 1    #4th block of ship
      shipPosit4col = shipPosit1col

      SHIP = [[shipPosit1row, shipPosit1col],[shipPosit2row, shipPosit2col], \
        [shipPosit3row, shipPosit3col],[shipPosit4row, shipPosit4col]]


#user guessing

playing = 0
turnCounter = 0
hit = 0

while playing == 0:                 #user Input
      userGuess = input("\n\nPlease enter a location on the board \
in the format ROW,COLUMN (Example: 2,A): ").upper()
      userGuess = userGuess.replace(".",",").replace(", ",",").split(",")
      
      guessedRow = int(userGuess[0])
      userGuess[0] = guessedRow
      
      guessedCol = int(ord(userGuess[1]) - 64)
      turnCounter += 1

      if guessedRow > 10 or guessedRow <=0 or guessedCol < 1 or guessedCol > 10: #out of range input
            print("\nInvalid location!")
            turnCounter -= 1
            
      elif hit == 3 and list(userGuess) in SHIP:         #user sinks ship
            print("\nShip sinked! Congratulations!\n")
            hit += 1
            #turnCounter += 1
            print("Number of turns:", turnCounter, end="\n\n\n")
            board[guessedRow][guessedCol] = hitSpaceBoard
            for row in board:                   
                  print("|".join(row), end="|\n")

            break
                  
      elif list(userGuess) in SHIP:         #user hits
            print("\nHit!\n")
            hit += 1
            board[guessedRow][guessedCol] = hitSpaceBoard
            #turnCounter += 1
            for row in board:                   
                  print("|".join(row), end="|\n")
                     
      elif list(userGuess) not in SHIP:      #user misses
            print("\nMissed!\n")
            board[guessedRow][guessedCol] = missedSpaceBoard
            #turnCounter += 1
            for row in board:                   
                  print("|".join(row), end="|\n")
      
if playing == 1:
      print("\nCongratulations! You sinked the ship!\n")
      print(turnCounter, "turns")
            
                       


