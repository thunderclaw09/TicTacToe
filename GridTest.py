#from TicTacToeGrids import *
winningGridX = [
    ["_X_|", "___", "|___"],
    ["___|", "_X_", "|___"],
    ["   |", "   ", "| X "]
]


WinningGrids = [
    [winningGridX[0][0], winningGridX[0][1], winningGridX[0][2]]
]



if WinningGrids[0] == winningGridX:
    print("It's true.")
else:
    print("It's not true")
    print(WinningGrids[0], winningGridX)