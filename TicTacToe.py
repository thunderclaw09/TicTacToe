#Weight on mars is 38% of person's weight on earth.
from tkinter import *
from tkinter import ttk
from Button import Square


firstRow = 1
secondRow = 2
thirdRow = 3

class TicTacToe:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

        Title = ttk.Label(self.frm, text="TIC TAC TOE")
        Title.grid(column=1, row=0)

        Square1 = Square(self.frm, 0, firstRow, 1)
        Square2 = Square(self.frm, 1, firstRow, 2)
        Square3 = Square(self.frm, 2, firstRow, 3)
        
        Square4 = Square(self.frm, 0, secondRow, 4)
        Square5 = Square(self.frm, 1, secondRow, 5)
        Square6 = Square(self.frm, 2, secondRow, 6)

        Square7 = Square(self.frm, 0, thirdRow, 7)
        Square8 = Square(self.frm, 1, thirdRow, 8)
        Square9 = Square(self.frm, 2, thirdRow, 9)


        # self.Answer = ttk.Label(self.frm, text=" ")
        # self.Answer.grid(column=0, row=5)
        # self.InputNum = ttk.Entry(self.frm, width=40)
        # self.InputNum.grid(row=2)

        # self.label1 = ttk.Label(self.frm, text="Please input your a number, and the program").grid(column=0, row=0)
        # self.label2 = ttk.Label(self.frm, text="will tell you if it's a prime number.").grid(column=0, row=1)
        
        # self.Close = ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=3, row=5)
        # self.Enter = ttk.Button(self.frm, text="Enter", command=self.EnterFunction).grid(column=3, row=2)

        

        mainloop()


    # def EnterFunction(self):
    #     print("Enter pressed!")
    #     Number = int(self.InputNum.get())
    #     divisor = 2
    #     Output = ""
    #     while True:
    #         result = Number % divisor
    #         if result > 0:
    #             divisor+=1
    #         elif Number == 2:
    #             Output = "The number is a prime number!"
    #             break
    #         elif result == 0:
    #             Output = "The number is not a prime number!"
    #             break
    #         elif divisor == Number:
    #             Output = "The number is a prime number!"
    #             break
            

        # self.Answer.config(text=Output) 
        
        print("It should have worked.")


    
    

    

  

ticTacToe = TicTacToe()



