#tkinter is a module (tool box) that holds code you can use
#by shortening the name

import tkinter as tk

#root is a variable that holds the ingormation about the main window.
#That is the window with the close, min, max buttons in the top left.
#tk.TK() go in the tk tool box and use the function TK()
root = tk.Tk()

ent = tk.Entry(root)

ent.grid(row =0, column = 0)

btn = tk.Button(root,text = "Press Me")
btn.grid(row =0, column = 1)


label = tk.Label(root, text = "....")
label.grid(row =1, column = 0, columnspan =2)


#sets up your program in an infinitt loop waiting for the usser to do something. 
#This is an EVENT DRIVE PROMGRAM. This means a function is called when 

root.mainloop()