import tkinter as tk


root = tk.Tk()

titleLabel = tk.Label(root, text = "Science formula Calculator", font= ("Helvetica", 30, ), foreground = "orange")
titleLabel.grid( row = 0, column = 0, columnspan = 2 )

output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)


word1Label = tk.Label(root, text = "Value 1", background = "Green", foreground = "yellow")
word1Label.grid(row =2, column = 0, sticky = "NESW")

word1Label = tk.Label(root, text = "Value 2", background = "Green", foreground = "yellow")
word1Label.grid(row =3, column = 0, sticky = "NESW")

word1Label = tk.Label(root, text = "Value 3", background = "Green", foreground = "yellow")
word1Label.grid(row =4, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 7, column = 1)

btnGo = tk.Button(root, text = "Generate")
btnGo.grid(row = 8, column = 1)

import tkinter as tk


canvas = tk.Canvas(root,width =300, height = 100, background = "blue")
canvas.grid(row = 5, column = 0, columnspan = 2 )

canvas1 = tk.Canvas(root,width =300, height = 100, background = "red")
canvas1.grid(row = 6, column = 0, columnspan = 2)

root.mainloop()






root.mainloop() # starts the program





