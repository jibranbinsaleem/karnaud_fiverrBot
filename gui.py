from tkinter import *
import tkinter as tk
from main import bot, info
master = Tk()  

# Dropdown menu options
exchange = [
    "binance",
    "coinbasepro",
    "bittrex"
]
sv = exchange[0]
  
# datatype of menu text
clicked = tk.StringVar(master)
  
# initial menu text
clicked.set( "Exchanges" )
  
# Create Dropdown menu
drop = OptionMenu( master , clicked , *exchange )
drop.grid()

# Create Label
label = Label( master , text = " " )
label.grid()
  
# Execute tkinter
Label(master, text='Input 1').grid(row=1)
Label(master, text='Input 2').grid(row=2)
Label(master, text='Input 3').grid(row=3)
Label(master, text='Output').grid(row=9)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
Output = Text(master, height = 2,
width = 25,  bg = "light cyan")
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3,column=1)
Output.grid(row=9,column=1)



str_out=tk.StringVar(master)
str_out.set("LOLO")

l2=Label(master,text=str_out,width=10)
l2.grid(row=9,column=5)


# Change the label text
def lul():
    x = info()
    Output.insert('1.0',x)

def show(o1,o2,o3):
    global result
    result=clicked.get()
    #print(clicked.get())
    # result = Label(master, textvariable=clicked).place(x=120,y=100)
    
def retrieve_input():
    inputValue1=e1.get()
    print(inputValue1)
    inputValue2=e2.get()
    print(inputValue2)
    inputValue3=e3.get()
    print(inputValue3)
    changer_input(inputValue1,inputValue2,inputValue3)
    
def changer_input(symbol, amount, x3):
    x = bot(result, symbol, amount)
    



buttonCommit1=Button(master, height=1, width=10, text="Start", 
                    command=lambda: retrieve_input())
buttonCommit1.grid(row=6,column=1) 
buttonCommit2=Button(master, height=1, width=10, text="Info", 
                    command=lambda: lul())
buttonCommit2.grid(row=7,column=1)

clicked.trace('w',show)
  
mainloop()