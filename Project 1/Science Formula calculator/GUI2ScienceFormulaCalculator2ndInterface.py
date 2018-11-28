import tkinter as tk


root = tk.Tk()

titleLabel = tk.Label(root, text = "Biology:", font= ("Alegreya", 30, ), foreground = "Green")
titleLabel.grid( row = 0, column = 0, columnspan = 2 )

titleLabel = tk.Label(root, text = "Simpsons Index:", font= ("Alegreya", 25, ), foreground = "Blue")
titleLabel.grid( row = 0, column = 2)

canvas = tk.Canvas(root,width =400, height = 200, background = "black")
canvas.grid(row = 3, column = 1, columnspan = 2 )

labTitle = tk.Label(root, text = "Number of Species")
labTitle.grid(row = 4, column = 0, columnspan = 3)

entry = tk.Entry(root)
entry.grid(row = 5, column = 0, columnspan = 3)

labInfo = tk.Label(root, text = "(number must be greater than 1)")
labInfo.grid(row = 6, column = 0, columnspan = 3)



root.mainloop()