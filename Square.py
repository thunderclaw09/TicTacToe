from tkinter import *
from tkinter import ttk
from Button import Square
from Button import PlayerTurn

class Button:
    def __init__(self):
        self.Square1 = Square(Square.frm, 0, 0)

    def select(self):
        global PlayerTurn
        if (self.Square.isClicked == False):
            if (PlayerTurn == "X"):
                self.Square.isClicked = True
                self.Square.option = "X"
                self.Square.Reload()  
                PlayerTurn = "O"
                
            elif (PlayerTurn == "O"):
                self.Square.isClicked = True
                self.Square.option = "O"
                self.Square.Reload()
                PlayerTurn = "X"
                
        else:
            print("You have already used this one!")