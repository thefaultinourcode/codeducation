import random

#the user can ask their question
question = raw_input("What would you like to ask the magic eightball? ")

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

#pick an answer
n=random.randint(0,7)

#print the answer out
print answers[n]