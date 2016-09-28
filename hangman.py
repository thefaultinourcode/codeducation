import random

print "Let's play hangman!\nTry to guess the word!"

fantasy=["unicorn", "dragon", "troll", "hippogriff", "phoenix"]
college=["homework", "exams", "projects", "learning", "tears"]
florida=["Tallahassee", "alligator", "palm", "sunshine", "weird"]

lists=[fantasy,college,florida]

x=random.randint(0,2)

theme = "Your word theme is: "

if(x==0):
	print theme + "fantasy!"
elif(x==1):
	print theme + "college!"
elif(x==2):
	print theme + "Florida!"

y=random.randint(0,4)
word=lists[x][y]
num=len(word)

letters=list(word)
print letters

print "The word is", num, "letters long."