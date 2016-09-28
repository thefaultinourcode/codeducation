import turtle 
import random
import sys
uni = turtle.Screen()      # Creates a playground for turtles
uni.bgcolor("darkgreen")
uni.title("Welcome to Unicorn Valley!")

you = turtle.Turtle();
you.shape("turtle")
you.color("black")

print "Welcome to Unicorn Valley!"

you.left(90)
you.forward(50)

unicorn_fate = raw_input("Do you turn left of right?")

if (unicorn_fate=='left'):
	print "A pretty unicorn approaches you!"
	you.left(90)
	you.forward(50)
elif (unicorn_fate=='right'):
	print "You trip over a pretty unicorn."
	you.right(90)
	you.forward(50)
else:
	print "A unicorn attacks your turtle for not following instructions."
	sys.exit()

pet_unicorn = raw_input("Do you pet the unicorn? y/n")

if (pet_unicorn=='y'):
	print "The unicorn accepts you as one of its own kind. You are now a pretty unicorn."
	you.color("white")
	you.shape("triangle")
elif (pet_unicorn=='n'):
	print "You made the unicorn sad. :("
	print "You leave the forest in shame."
	if (unicorn_fate=='left'):
		you.left(90)
	elif (unicorn_fate=='right'):
		you.right(90)		
	you.forward(500)
else:
	print "The unicorn attacks your turtle for not following instructions."
	sys.exit()

turtle.mainloop()

print "Game over"

'''
winner = random.randint(0, 10)

if (winner >= 6):
	print "You win a unicorn!"
else:
	print "You lost a unicorn!" 
'''

