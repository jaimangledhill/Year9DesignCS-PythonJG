#Imports all the tools for tkinter and gives it the name tk.  This means to look in the tkinter "tool box"
#we use tk.<something>
import tkinter as tk


#This is a function called chage.  It is called automatically when the dropdown is changed. The *args
#is a parameter that is a special type in python.  We use it when we want to tell the function to take
#anything
def change(*args):
	#Anything indented is inside the function. 
	print("running change")
	print(var.get())
	#END OF THE FUNCTION

#This creates your main window using the tkinter.  The main window is called root
root = tk.Tk()

#This is a list called OPTIONS.  It stores all the possible options that the drop menu can have
OPTIONS =  ["eggs","bunny","chicken","dog"]

#A StringVar is a special varialbe we attach to widget. 
var = tk.StringVar(root)
var.set(OPTIONS[0])	#SETS VAR TO OPTIONS[0]
var.trace("w",change) #TELLS THE PROGRAM THAT ANYTIME WE CHANGE VAR TO RUN THE FUNCTION CHANGE.
	
	
#SETS UP TEH DROP DOWN MENU. 
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3])
dropDownMenu.pack()


root.mainloop()


print("End program")