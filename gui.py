from tkinter import *
master = Tk()  
# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()

  
# initial menu text
clicked.set( "options" )
  
# Create Dropdown menu
drop = OptionMenu( master , clicked , *options )
drop.grid()
print(drop)

# Create Label
label = Label( master , text = " " )
label.grid()
  
  
  
  

# Execute tkinter
Label(master, text='Input 1').grid(row=1)
Label(master, text='Input 2').grid(row=2)
Label(master, text='Input 3').grid(row=3)
Label(master, text='Output').grid(row=6)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
Output = Text(master, height = 2,
width = 15,  bg = "light cyan")
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3,column=1)
Output.grid(row=6,column=1)
mainloop()