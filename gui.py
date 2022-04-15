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
master.geometry("700x350")

  
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
Label(master, text='symbol ').grid(row=1)
Label(master, text='amount').grid(row=2)
Label(master, text='Input 3').grid(row=3)
Label(master, text='Output').grid(row=9)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
Output = Text(master, height = 30,
width = 65,  bg = "light cyan")
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3,column=1)
Output.grid(row=9,column=1)



str_out=tk.StringVar(master)
str_out.set("LOLO")

l2=Label(master,text=str_out,width=10)
l2.grid(row=9,column=5)

condition = False
# Change the label text
def lul():
    x = info()
    Output.insert('1.0',x)

def show(o1,o2,o3):
    global result
    result=clicked.get()
    #print(clicked.get())
    # result = Label(master, textvariable=clicked).place(x=120,y=100)


condition = False
#print(condition, "2")
def retrieve_input():
    #print(conditon)
    if condition:
        
      
        symbol=e1.get()
       #print(inputValue1)
        amount=e2.get()
        #print(inputValue2)
        inputValue3=e3.get()
        #print(inputValue3)
        bot(result, symbol, amount)
    master.after(1000*60*30, retrieve_input)

def start():
   global condition
   condition=True






buttonCommit1=Button(master, height=1, width=10, text="Start", 
                    command=lambda: start())
buttonCommit1.grid(row=6,column=1) 
buttonCommit2=Button(master, height=1, width=10, text="Info", 
                    command=lambda: lul())
buttonCommit2.grid(row=7,column=1)

clicked.trace('w',show)
master.after(60000, retrieve_input)
  
mainloop()