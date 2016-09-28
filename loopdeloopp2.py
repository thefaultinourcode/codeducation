import turtle 
import random
import sys

count=0
'''print count
while(count < 12):
	print "The count is:", count
	count = count + 1'''

'''randnum = random.randint(100,1000)

number = input("Enter a count: ")

flip = bool(random.getrandbits(1))

if(flip):
	while(count < number):
		count = count + 1
		print count
		
else:
	while(count < randnum):
		count = count + 1
		print count
	print "Life is random."'''
'''1=heads 2=tails'''
side = random.randint(1,2)

'''print "You have one guess to see which side the coin landed on"
guess = raw_input("Enter a side: heads or tails ")
control = 1

while (control == 1):
	if (guess == "heads"):
		if (side == 1):
			print "You truly are a computer psychic."
		else:
			print "You probably can't read a computer's mind."
	elif (guess == "tails"):
		if (side == 1):
			print "You probably can't read a computer's mind."
		else:
			print "You truly are a computer psychic."
	else:
		print "This isn't ternary."
	control = 2'''

uni = turtle.Screen()

print "Welcome to Turtle Bomb"

cool_number = random.randint(1,10)
uni.bgcolor("darkgreen")
uni.title("Welcome to Turtle Bomb")

you = turtle.Turtle();
you.shape("turtle")
you.color("black")

print cool_number

count == 0
while(count < 3):
	guess = input("Guess the number: ")
	if(cool_number != guess):
		print "Oh no!"
		count = count + 1
	else:
		print "You saved the day, yay!"
		sys.exit()

turtle.mainloop()