#Weight on mars is 38% of person's weight on earth.
from tkinter import *
from tkinter import ttk
from Square import Button

def Update(button):
    button.Button.config(text=button.option)
    print("It updated. Here's the button option: " + button.option)

class TicTacToe:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

        # Square1 = Square(self.frm, 0, 0, Update)
        Button1 = Button()


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



