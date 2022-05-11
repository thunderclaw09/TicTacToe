from tkinter import *
from tkinter import ttk
# from TicTacToe import *

PlayerTurn = "X"

class Square:

    def __init__(self, app, col, r, id, PlayerText):
        self.option = "-"
        self.isClicked = False
        self.Button = ttk.Button(app, text=self.option, command=self.select)
        self.Button.grid(column=col, row=r)
        self.app = app
        self.id = id
        self.PlayerText = PlayerText

        # while True:
        #     if (self.isClicked == True):
        #         Reload()
        #         break

    def Reload(self):
        global PlayerTurn
        self.Button.config(text=self.option)
        self.PlayerText.config(text="Player: "+PlayerTurn)

    def select(self):
        global PlayerTurn
        if (self.isClicked == False):
            if (PlayerTurn == "X"):
                self.isClicked = True
                self.option = "X"
                PlayerTurn = "O"
                self.Reload()
                
                
            elif (PlayerTurn == "O"):
                self.isClicked = True
                self.option = "O"
                PlayerTurn = "X"
                self.Reload()
                
                
        else:
            print("You have already used this one!")

    

     

    
        