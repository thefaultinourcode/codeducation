import random

print "Welcome to Unicorn Valley!"

unicorn_fate = raw_input("Do you turn left of right?")

if (unicorn_fate=='left'):
	print "A pretty unicorn approaches you!"
elif (unicorn_fate=='right'):
	print "You trip over a pretty unicorn."
else:
	print "A unicorn attacks you for not following instructions."

pet_unicorn = raw_input("Do you pet the unicorn? y/n")

if (pet_unicorn=='y'):
	print "The unicorn accepts you as one its own kind. You are now a pretty unicorn."
elif (pet_unicorn=='n'):
	print "You made the unicorn sad. :("
else:
	print "The unicorn attacks you for not following instructions."

winner = random.randint(0, 10)

if (winner >= 6):
	print "You win a unicorn!"
else:
	print "You lost a unicorn!"