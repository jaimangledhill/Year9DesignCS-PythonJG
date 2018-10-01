# A loop structure is a structure that allows us to run a section of code a number of times.
# It is great for when we need to repeat a process.  It is also great when we need to run a pattern.

#There are two bround catagories of loops.
#comditional loop:this loops as long as something is true
#Counted loop: this loops a set number


print("0")
print("1")
print("2")
print("3")
print("4")

print("************************************")
#the general structure of a counted loop is 
#count:this is the varuable we use to track the number of times a loop runs.
#Check:this the boolean (true or false) statement we evaluate to decide if we keep going.
#Change: this is the change in the count that happens after. each loop.each

#we use i in range loop
for i in range(0, 6, 1):
	print(i)
#how would the above loop run
#we would reach line 27
# i = 0, 0, < 6 True RUN LOOP
# i = 0, 1, < 6 True RUN LOOP
# i = 0, 2, < 6 True RUN LOOP
# i = 0, 3, < 6 True RUN LOOP
# i = 0, 4, < 6 True RUN LOOP
# i = 0, 5, < 6 True RUN LOOP
# i = 0, 6, < 6 False exit loop and move on


print("**********************************************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)
print("*************************************")
print("Write a loop that will print out even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)

print("*************************************")
print("we can count backwards as well. Python3 will assume the check based on")
print("relative value of the count and check")

for i in range(3,0,-1):
	print(i)

print("*************************************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101,-1,-1):
	#Anything that is tabbed is the loop code block
	print(i)

s = "Fish Food"

#Good Practices You must do this never never type in lenght of string as a number
#Always have the computer find it.

print("*************************************")
for i in range(0,9,1):
	print(s[i])

#different way to do above

s = "Fish Food"



print("*************************************")
for i in range(0,len(s),1):
	print(s[i])

print("*************************************")

#Print out in reverse
for i in range(8,-1,-1):
	print(s[i])
print("*************************************")

#can you print very second letter
for i in range(0,len(s),2):
	print(s[i])






