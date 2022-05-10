from tkinter import *
from tkinter import ttk
# from TicTacToe import *

PlayerTurn = "X"

class Square:

    def __init__(self, app, col, r):
        self.option = "-"
        self.isClicked = False
        self.Button = ttk.Button(app, text=self.option, command=self.select)
        self.Button.grid(column=col, row=r)
        self.app = app

        # while True:
        #     if (self.isClicked == True):
        #         Reload()
        #         break

    def Reload(self):
        self.Button.config(text=self.option)

    def select(self):
        global PlayerTurn
        if (self.isClicked == False):
            if (PlayerTurn == "X"):
                self.isClicked = True
                self.option = "X"
                self.Reload()
                PlayerTurn = "O"
                
            elif (PlayerTurn == "O"):
                self.isClicked = True
                self.option = "O"
                self.Reload()
                PlayerTurn = "X"
                
        else:
            print("You have already used this one!")

    

     

    
        