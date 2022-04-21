from time import sleep
from TicTacToeGrids import *


Player = 1
Square = 0
MatchIsRunning = True



def SwapPlayer():
    global Player
    if Player == 1:
        Player = 2
    elif Player == 2:
        Player = 1



def PrintGrid():
    # for i in GridList:
    #     print(Grids[i])
    for i in Grids["TopGrid"]:
        print(i, end = "")
    print()

    for i in Grids["MiddleGrid"]:
        print(i, end = "")
    print()

    for i in Grids["BottomGrid"]:
        print(i, end = "")
    print()
    


def Program():
    print("Welcome to TIC TAC TOE!!!")
    sleep(0.2)
    print("There will be nine options. To play, input a number from 1 to 9. \n Each number will represent a square, going from left to right, then from top to bottom.")
    sleep(0.2)

    PrintGrid()

    while MatchIsRunning:
        if Player == 1:
            Square = int(input("Player 1, please input the square number: "))
            AssignSquare(Square)
            CheckForWinner()
            SwapPlayer()
            

        elif Player == 2:
            Square = int(input("Player 2, please input the square number: "))
            AssignSquare(Square)
            CheckForWinner()
            SwapPlayer()
            
        




def AssignSquare(SquareNum):
    if SquareNum == 1:
        if Player == 1:
            Grids["TopGrid"][0] = XGrids["XTop"][0]
            # Grids["TopGrid"[0]] = "_X_|"
            PrintGrid()
            #print(Grids["TopGrid"][0])
        else:
            Grids["TopGrid"][0] = OGrids["OTop"][0]
            PrintGrid()

    elif SquareNum == 2:
        if Player == 1:
            Grids["TopGrid"][1] = XGrids["XTop"][1]
            PrintGrid()
        else:
            Grids["TopGrid"][1] = OGrids["OTop"][1]
            PrintGrid()

    elif SquareNum == 3:
        if Player == 1:
            Grids["TopGrid"][2] = XGrids["XTop"][2]
            PrintGrid()
        else:
            Grids["TopGrid"][2] = OGrids["OTop"][2]
            PrintGrid()

    elif SquareNum == 4:
        if Player == 1:
            Grids["MiddleGrid"][0] = XGrids["XMiddle"][0]
            PrintGrid()
        else:
            Grids["MiddleGrid"][0] = OGrids["OMiddle"][0]
            PrintGrid()

    elif SquareNum == 5:
        if Player == 1:
            Grids["MiddleGrid"][1] = XGrids["XMiddle"][1]
            PrintGrid()
        else:
            Grids["MiddleGrid"][1] = OGrids["OMiddle"][1]
            PrintGrid()

    elif SquareNum == 6:
        if Player == 1:
            Grids["MiddleGrid"][2] = XGrids["XMiddle"][2]
            PrintGrid()
        else:
            Grids["MiddleGrid"][2] = OGrids["OMiddle"][2]
            PrintGrid()

    elif SquareNum == 7:
        if Player == 1:
            Grids["BottomGrid"][0] = XGrids["XBottom"][0]
            PrintGrid()
        else:
            Grids["BottomGrid"][0] = OGrids["OBottom"][0]
            PrintGrid()

    elif SquareNum == 8:
        if Player == 1:
            Grids["BottomGrid"][1] = XGrids["XBottom"][1]
            PrintGrid()
        else:
            Grids["BottomGrid"][1] = OGrids["OBottom"][1]
            PrintGrid()

    elif SquareNum == 9:
        if Player == 1:
            Grids["BottomGrid"][2] = XGrids["XBottom"][2]
            PrintGrid()
        else:
            Grids["BottomGrid"][2] = OGrids["OBottom"][2]
            PrintGrid()

    else:
        print("That is not a valid square number.\n(Square numbers are from 1-9)")



def CheckForWinner():
    global MatchIsRunning
    if Player == 1:
        for i in WinningXGrids:
            for j in WinningGrids:
                if i == j:
                    print("Player 1 wins!")  #So far, this only works for across, NOT top to bottom or diagonal.
                    MatchIsRunning = False
                    break
                else:
                    print(i, j)
                    
    #pass

            
                        
                


Program()




############################ NOTES AND OTHER STUFF ############################
'''
- (23/2/2022) This code was written by me. Obviously, I needed internet help, but I did NOT copy and paste. 
  I thought that the poor code quality would make that apparent, lol.

- As of today, the code works. You can input numbers 1-9, and an x or an o will show up. However,
  there is nothing to check if either player wins, and for some reason when the grid is printed, it's printed
  as a list, with the square brakets and quotation marks. Yay me.

- (7:27 PM) I'm at the coding thing and Gabe just helped me fix the grid. Started this project today at 2 PM, roughly.

'''