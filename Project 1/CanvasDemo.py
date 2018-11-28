import tkinter as tk


root = tk.Tk()

canvas = tk.Canvas(root,width =300, height = 100, background = "blue")
canvas.pack()

canvas1 = tk.Canvas(root,width =300, height = 100, background = "red")
canvas1.pack()

root.mainloop()

