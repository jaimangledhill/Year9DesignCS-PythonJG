import tkinter as tk
import math

#A def in python is a function 
#A function is a small piece of code you call and run
#This function is bound to teh submit key
#This means when your click it, the function runs
#Everything in function must be tabbed .
def submit():
#*********START OF FUNCTION*********
	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())
	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)

	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")
	

#*********END OF FUNCTION***********



#*********START OF PROGRAM**********
root = tk.Tk()
root.config(background = "green")
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()


btn = tk.Button(root, text="Submit", command=submit, activebackground = "red")
btn.pack()

output = tk.Text(root, width =50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




root.mainloop()
