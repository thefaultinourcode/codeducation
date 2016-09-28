#having fun learning about loops in python

count = 0
while (count < 9):
	print "The count is: ", count
	#+ only works with a string, use a comma or get an error
	count = count + 1

#letter represents current letter being reiterated
for letter in "Python":
	print "Current Letter :" + letter

#prints 1-9
for x in range(1,10):
	print x

#iterates over each letter
word = "Dominic"
for x in word:
	print x

#being ridiculous
magic = "unicorn"
for h in magic:
	print "Check out my " + h

print "unicorn"

name = raw_input("How many h's does your name have?")

counth=0

for currentChar in name:
	if currentChar == "h":
		counth = counth + 1

print "this contains", counth, "h(s)!"

""" Don't do this:
x = 0
while (x == 0):
	print x
"""

for num in range(1,101):
	if (num > 50):
		print num