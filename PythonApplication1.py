import os
from time import sleep

#possible moves on board
moves = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]

#initialize variables 
playAgain = "y"
winner = ""
playerOneWins = 0
playerTwoWins = 0

#function defs
def getRow(r):
     if r == 1:
         return 0
     elif r == 2:
         return 2
     elif r == 3:
         return 4

def getCol(c):
      if c == 1:
         return 0
      elif c == 2:
         return 2
      elif c == 3:
         return 4

#begin game
while playAgain == "y":

    gameboard = [
["   ", "|", "   ", "|", "   "],
["---", "|", "---", "|", "---"], 
["   ", "|", "   ", "|", "   "],
["---", "|", "---", "|", "---"], 
["   ", "|", "   ", "|", "   "],
]

    txt = input("Tic Tac Toe\nBegin Game? (y/n):\n").lower()

    while txt not in ["y"]:
        txt = input("Begin Game? (y/n):\n")

        #print empty gameboard
    if txt == "y":
        gameGoing = True
        sleep(1)
        os.system('cls')

        rows = ""
        for row in gameboard:
            for element in row:
                rows += element
            print(rows)
            rows = ""
   
    while gameGoing:


        playerOne = input("PLAYER 1: Enter a move (column, row)\n").lower()

            #throw error if input isn't valid
        while (playerOne not in moves) or (len(playerOne) != 3) or (playerOne[1] != ","):
            playerOne = input("Invalid move.\nPLAYER 1: Enter a move (column, row)\n").lower()
            
            #throw error if space is already filled
        while gameboard[getRow(int(playerOne[2]))][getCol(int(playerOne[0]))] != "   ":
            playerOne = input("Invalid move.\nPLAYER 1: Enter a move (column, row)\n").lower()

            #clears screen, reprints board with move
        gameboard[getRow(int(playerOne[2]))][getCol(int(playerOne[0]))] = " X "

        sleep(1)
        os.system('cls')

        for row in gameboard:
            for element in row:
                rows += element
            print(rows)
            rows = ""

            #checks after each move for win
        if (gameboard[0][0] == " X " and gameboard[0][2] == " X " and gameboard[0][4] == " X ") or (gameboard[2][0] == " X " and gameboard[2][2] == " X " and gameboard[2][4] == " X ") or (gameboard[4][0] == " X " and gameboard[4][2] == " X " and gameboard[4][4] == " X "):
            gameGoing = False
            winner = "PLAYER 1"
            playerOneWins += 1

        if (gameboard[0][0] == " X " and gameboard[2][0] == " X " and gameboard[4][0] == " X ") or (gameboard[0][2] == " X " and gameboard[2][2] == " X " and gameboard[4][2] == " X ") or (gameboard[0][4] == " X " and gameboard[2][4] == " X " and gameboard[4][4] == " X "):
            gameGoing = False
            winner = "PLAYER 1"
            playerOneWins += 1

        if (gameboard[0][0] == " X " and gameboard[2][2] == " X " and gameboard[4][4] == " X ") or (gameboard[0][4] == " X " and gameboard[2][2] == " X " and gameboard[4][0] == " X "):
            gameGoing = False
            winner = "PLAYER 1"
            playerOneWins += 1

            #checks for tie
        if gameGoing:
            if gameboard[0][0] != "   " and gameboard[0][2] != "   " and gameboard[0][4] != "   " and gameboard[2][0] != "   " and gameboard[2][2] != "   " and gameboard[2][4] != "   " and gameboard[4][0] != "   " and gameboard[4][2] != "   " and gameboard[4][4] != "   ":
                gameGoing = False
                winner = "DRAW"
        
                #if no win or tie, player 2 moves
        if gameGoing:
            playerTwo = input("PLAYER 2: Enter a move (column, row)\n").lower()

            while (playerTwo not in moves) or (len(playerTwo) != 3) or (playerTwo[1] != ","):
                playerTwo = input("Invalid move.\nPLAYER 2: Enter a move (column, row)\n").lower()
            

            while gameboard[getRow(int(playerTwo[2]))][getCol(int(playerTwo[0]))] != "   ":
                playerTwo = input("Invalid move.\nPLAYER 2: Enter a move (column, row)\n").lower()

            gameboard[getRow(int(playerTwo[2]))][getCol(int(playerTwo[0]))] = " O "

            sleep(1)
            os.system('cls')

            rows = ""
            for row in gameboard:
                for element in row:
                    rows += element
                print(rows)
                rows = ""

            if (gameboard[0][0] == " O " and gameboard[0][2] == " O " and gameboard[0][4] == " O ") or (gameboard[2][0] == " O " and gameboard[2][2] == " O " and gameboard[2][4] == " O ") or (gameboard[4][0] == " O " and gameboard[4][2] == " O " and gameboard[4][4] == " O "):
                gameGoing = False
                winner = "PLAYER 2"
                playerTwoWins += 1

            if (gameboard[0][0] == " O " and gameboard[2][0] == " O " and gameboard[4][0] == " O ") or (gameboard[0][2] == " O " and gameboard[2][2] == " O " and gameboard[4][2] == " O ") or (gameboard[0][4] == " O" and gameboard[2][4] == " O " and gameboard[4][4] == " O "):
                gameGoing = False
                winner = "PLAYER 2"
                playerTwoWins += 1

            if (gameboard[0][0] == " O " and gameboard[2][2] == " O " and gameboard[4][4] == " O ") or (gameboard[0][4] == " O " and gameboard[2][2] == " O " and gameboard[4][0] == " O "):
                gameGoing = False
                winner = "PLAYER 2"
                playerTwoWins += 1

    if winner == "DRAW":
        print("DRAW!")
        print("PLAYER ONE WINS: %s\nPLAYER TWO WINS: %s" % (playerOneWins, playerTwoWins))
    else:
        print(winner + " HAS WON!")
        print("PLAYER ONE WINS: %s\nPLAYER TWO WINS: %s" % (playerOneWins, playerTwoWins))

    playAgain = input("Play again? (y/n):\n").lower()

    while playAgain not in ["y", "n"]:
        playAgain = input("Invalid response.\nPlay again? (y/n):\n").lower()

    sleep(1)
    os.system('cls')





    
    
