import turtle

#data input

print "Hello and welcome to the turtle data bar graph generator!"

#declare list for #of turtles

num_turtles = []

#declare list for location of turtles

loc_turtles = []

cont = True

#while loop to input variables
while (cont):
	#ask for # of turtles
	t_num = input("How many turtles were in this location?")
	#put # of turtles in array
	num_turtles.append(t_num)
	#ask for location of turtles
	l_name = raw_input("What was the location?")
	#put turtles in array
	loc_turtles.append(l_name)
	#ask if more input
	more = raw_input("Do you have more data to enter? (y/n)")
	if(more=="n"):
		cont = False

 


wn = turtle.Screen()
bar = turtle.Turtle()

'''
turtle.write("Leah", False, align="center", font=("Times New Roman", 48, "bold"))
turtle.write("Leah", False, align="center", font=("Times New Roman", 48, "bold"))
'''

for num in num_turtles:
	#graph turtle
	turtle.write(num, False, align="left", font=("Arial", 36))
	bar.left(90)
	bar.forward(num)
	bar.right(90)
	bar.forward(10)
	bar.right(90)
	bar.right(num)

	bar.left(10)	

	



turtle.mainloop()