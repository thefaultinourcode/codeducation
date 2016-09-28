import random

print "Welcome to the Magic Eight Ball Build Your Own Future Machine!"

#(sarcastic) options for answers
a1 = "Ask again later."
a2 = "Yes, that will definitely happen."
a3 = "That is not in your future."
a4 = "No."
a5 = "No, but you'll get a pet unicorn."
a6 = "Maybe, it's a little unclear."
a7 = "Why are you asking me? I'm just a computer program."
a8 = "???"

#answers stored in an array
answers = [a1, a2, a3, a4, a5, a6, a7, a8]

question = raw_input("What would you like to ask the magic eightball? ")

def magic_eight_ball(question):
	print question
	#pick an answer
	n=random.randint(0,7)

	#the answer that is the key to your future
	x = answers[n]

	#return the answer
	return x

def in_future():
	print "Let's increment your happiness points now that your future is so certain to work out!"
	for x in range(1,6):
		if(x==1):
			print x, "happiness point!"
		else:
			print x, "happiness points!"

def not_in_future():
	answer = True
	while(answer):
		print "That's a bummer. Let's try again until you get another answer:"
		x = magic_eight_ball(question)
		print "\n", x, "\n"
		if(x!=a3):
			print "Yay, another answer!"
			answer = False

def unicorn():
	unicorn = """\
                        /
                    .,. /
                  ,ttttn
       ,,.__    .,XXX"nI)
      X  XXXXXXXXXXXXX ""
      .X XXXXXXXXXXXXXXxx   -Paul Neubauer-
     "  .XX"XX      X  ./
        *X' (X      X  "
         X   ")      X
         X,   '"     '"       Silver Unicorn
"""
	return unicorn

def unclear():
	count = 0
	randnum = random.randint(1,8)
	while(count < randnum):
		count = count + 1
		print count
	print "Life is random. Have a number:", randnum

def program():
	print "This is just the product of a weird college student's imagination."
	x=raw_input("Seriously, do you know how she made this? y/n")
	if(x=='y'):
		print "Well, then you already know this is an illusion."
	elif(x=='n'):
		print "Well, then let me explain: "
		print "I made up answers and assigned them to variables and stuck them in an array."
		print "Then I used the raw_input function to take your question. You can literally put anything in there, and it will be accepted as a question."
		print "Anything!"
		print "I made a function to use the random class to pick a random number between 0-7."
		print "I used that number to select the answer out of an array."


x = magic_eight_ball(question)

if(x==a1):
	magic_eight_ball(question)
elif(x==a2):
	print a2
	in_future()
elif(x==a3):
	print a3
	not_in_future()
elif(x==a4):
	print a4
elif(x==a5):
	print a5
	x = unicorn()
	print x
elif(x==a6):
	print a6
	unclear()
elif(x==a7):
	print a7
	program()
elif(x==a8):
	print a8
	print "Sometimes ??? is all that needs to be said"
