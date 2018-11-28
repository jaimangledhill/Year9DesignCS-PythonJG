import tkinter as tk


root = tk.Tk()

titleLabel = tk.Label(root, text = "Science formula Calculator", font= ("Alegreya", 30, ), foreground = "orange")
titleLabel.grid( row = 0, column = 0, columnspan = 2 )

titleLabel = tk.Label(root, text = "Welcome to this Science formula Calculator.", font= ("Alegreya", 30, ), foreground = "Black")
titleLabel.grid( row = 1, column = 0, columnspan = 2 )

titleLabel = tk.Label(root, text = "This formula can Calculate Simpsons Index and The Chi Squared Statistic.", font= ("Alegreya", 30, ), foreground = "Black")
titleLabel.grid( row = 2, column = 0, columnspan = 2 )

titleLabel = tk.Label(root, text = "Please click on the formula that you would like to be calculated.", font= ("Alegreya", 30, ), foreground = "Black")
titleLabel.grid( row = 3, column = 0, columnspan = 2 )




canvas = tk.Canvas(root,width =650, height = 250, background = "blue")
canvas.grid(row = 4, column = 0, columnspan = 2 )

canvas1 = tk.Canvas(root,width =650, height = 250, background = "red")
canvas1.grid(row = 5, column = 0, columnspan = 2)

root.mainloop()

