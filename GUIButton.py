import tkinter as tk

root = tk.Tk()
root.title("GUI Button")

btn1 = tk.Button(root, text="Button 1")
btn2 = tk.Button(root, text="Button 1")


btn1.pack()
btn2.pack()


root.mainloop()
