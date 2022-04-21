#CHECK FOR WINNER FIX
#create another list with all possible combinations referecing Grids, then loop through them, comparing them to the 
#player winning list.

Grids = {
    "TopGrid" : ["___|", "___", "|___"],
    "MiddleGrid" : ["___|", "___", "|___"],
    "BottomGrid" : ["   |", "   ", "|   "]
}

XGrids = {
    "XTop" : ["_X_|", "_X_", "|_X_"],
    "XMiddle" : ["_X_|", "_X_", "|_X_"],
    "XBottom" : [" X |", " X ", "| X "]
}

OGrids = {
    "OTop" : ["_O_|", "_O_", "|_O_"],
    "OMiddle" : ["_O_|", "_O_", "|_O_"],
    "OBottom" : [" O |", " O ", "| O "]
}

WinningGrids = [
    [Grids["TopGrid"]], 
    [Grids["MiddleGrid"]], 
    [Grids["BottomGrid"]],
    [Grids["TopGrid"][0], Grids["MiddleGrid"][0], Grids["BottomGrid"][0]],
    [Grids["TopGrid"][1], Grids["MiddleGrid"][1], Grids["BottomGrid"][1]],
    [Grids["TopGrid"][2], Grids["MiddleGrid"][2], Grids["BottomGrid"][2]],
    [Grids["TopGrid"][0], Grids["MiddleGrid"][1], Grids["BottomGrid"][2]],
    [Grids["TopGrid"][2], Grids["MiddleGrid"][1], Grids["BottomGrid"][0]]
]

# WinningXGrids = {
#     "Across" : [XGrids["XTop"], XGrids["XMiddle"], XGrids["XBottom"]],
#     "Down1" : [XGrids["XTop"][0], XGrids["XMiddle"][0], XGrids["XBottom"][0]],
#     "Down2" : [XGrids["XTop"][1], XGrids["XMiddle"][1], XGrids["XBottom"][1]],
#     "Down3" : [XGrids["XTop"][2], XGrids["XMiddle"][2], XGrids["XBottom"][2]],
#     "Diagonal1" : [XGrids["XTop"][0], XGrids["XMiddle"][1], XGrids["XBottom"][2]],
#     "Diagonal2" : [XGrids["XTop"][2], XGrids["XMiddle"][1], XGrids["XBottom"][0]]
# }

# WinningOGrids = {
#     "Across" : [OGrids["OTop"], OGrids["OMiddle"], OGrids["OBottom"]],
#     "Down1" : [OGrids["OTop"][0], OGrids["OMiddle"][0], OGrids["OBottom"][0]],
#     "Down2" : [OGrids["OTop"][1], OGrids["OMiddle"][1], OGrids["OBottom"][1]],
#     "Down3" : [OGrids["OTop"][2], OGrids["OMiddle"][2], OGrids["OBottom"][2]],
#     "Diagonal1" : [OGrids["OTop"][0], OGrids["OMiddle"][1], OGrids["OBottom"][2]],
#     "Diagonal2" : [OGrids["OTop"][2], OGrids["OMiddle"][1], OGrids["OBottom"][0]]
# }

WinningXGrids = [
    [XGrids["XTop"]], 
    [XGrids["XMiddle"]], 
    [XGrids["XBottom"]],
    [XGrids["XTop"][0], XGrids["XMiddle"][0], XGrids["XBottom"][0]],
    [XGrids["XTop"][1], XGrids["XMiddle"][1], XGrids["XBottom"][1]],
    [XGrids["XTop"][2], XGrids["XMiddle"][2], XGrids["XBottom"][2]],
    [XGrids["XTop"][0], XGrids["XMiddle"][1], XGrids["XBottom"][2]],
    [XGrids["XTop"][2], XGrids["XMiddle"][1], XGrids["XBottom"][0]]
]

WinningOGrids = [
    [OGrids["OTop"]], 
    [OGrids["OMiddle"]], 
    [OGrids["OBottom"]],
    [OGrids["OTop"][0], OGrids["OMiddle"][0], OGrids["OBottom"][0]],
    [OGrids["OTop"][1], OGrids["OMiddle"][1], OGrids["OBottom"][1]],
    [OGrids["OTop"][2], OGrids["OMiddle"][2], OGrids["OBottom"][2]],
    [OGrids["OTop"][0], OGrids["OMiddle"][1], OGrids["OBottom"][2]],
    [OGrids["OTop"][2], OGrids["OMiddle"][1], OGrids["OBottom"][0]]
]

''' THIS IS THE PROBLEM (24/2/2022)
['_X_|', '_X_', '| X '] [['_X_|', '_O_', '|___']]
['_X_|', '_X_', '| X '] [['___|', '_X_', '|_O_']]  as you can see, the rows are being compared wrong. That's why 
['_X_|', '_X_', '| X '] [['   |', '   ', '| X ']]  you only win by across.

_X_|, _X_, | X .
'''