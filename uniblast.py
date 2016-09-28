import random

print "Welcome to DRAGONBLAST!"
print "Save the unicorns from the angry dragons!"
print "Play this game by guessing a random number between 1-10 to appease the dragon"
print "You will have 3 attempts to guess the right number"

dragon = """
                                                                 __,
                                                    __...---`````_,
                        .-``-.     .-``-......__.-``   _.--``````  ___,
                       ^      :   :               -`````---````````_,
                       ^_      :  :....._                    _.-```
                        |`|-.   `.    o  ``-.__.-`````...````
                             `.   `...__. ,'.___.-```;:'
                               `._     ; ;        .:'___,
                                  ````` ;        _...--`
                               __..--```       -```-.
                      .|,|_.-``___....---```````--.._\
                      `-,,--```     ..---```````--.    
                                     `-.          ;).    
                                        ;        ;'..)    
              __.-`|`-./                ;       ;).        \.-`/8e.__
             __.   |   .                '      ;'..)       .  (88 8.__
             __:  /|\  :_           __ ;      ;_          _: 8  )88:__
                `/_|_\'/ '-._      / /;      ;) \     _.-' \`._/8*'
                       '.    ``-._/  |;     ;/   \_.-``   ,'      
                         `-.          \;    ;\         ,-'
                            `-._     /  ;   ; \     ,-'
                                `.__/    ;  ;  \__,'
                                          ; ;)`.
                                           ;;'..)
                                            ;

"""
print dragon

dragon2 = """\
@@@@@@@@@@@@@@@@@@@@@**^^""~~~"^@@^*@*@@**@@@@@@@@@
@@@@@@@@@@@@@*^^'"~   , - ' '; ,@@b. '  -e@@@@@@@@@
@@@@@@@@*^"~      . '     . ' ,@@@@(  e@*@@@@@@@@@@
@@@@@^~         .       .   ' @@@@@@, ~^@@@@@@@@@@@
@@@~ ,e**@@*e,  ,e**e, .    ' '@@@@@@e,  "*@@@@@'^@
@',e@@@@@@@@@@ e@@@@@@       ' '*@@@@@@    @@@'   0
@@@@@@@@@@@@@@@@@@@@@',e,     ;  ~^*^'    ;^~   ' 0
@@@@@@@@@@@@@@@^""^@@e@@@   .'           ,'   .'  @
@@@@@@@@@@@@@@'    '@@@@@ '         ,  ,e'  .    ;@
@@@@@@@@@@@@@' ,&&,  ^@*'     ,  .  i^"@e, ,e@e  @@
@@@@@@@@@@@@' ,@@@@,          ;  ,& !,,@@@e@@@@ e@@
@@@@@,~*@@*' ,@@@@@@e,   ',   e^~^@,   ~'@@@@@@,@@@
@@@@@@, ~" ,e@@@@@@@@@*e*@*  ,@e  @@""@e,,@@@@@@@@@
@@@@@@@@ee@@@@@@@@@@@@@@@" ,e@' ,e@' e@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@" ,@" ,e@@e,,@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@~ ,@@@,,0@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@
"""


randnum = random.randint(1,10)
print randnum

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

num = 0

'''
while (randnum != num):
	num = raw_input("Enter the dragon's number!")
	print 
'''


for num in range(1,4):
	save = input("Enter the dragon's number!")
	if(randnum == save):
		print "You saved the unicorn!"
		print unicorn
		break
	else:
		print save
		print randnum
		print "Oh no, wrong number!"
		if(num == 3):
			print dragon2
			print "Poor unicorn :("


for num in range(1,4):
	save = raw_input("Enter the dragon's number!")
	if(randnum == int(save)):
		print "You saved the unicorn!"
		print unicorn
		break
	else:
		print save
		print randnum
		print "Oh no, wrong number!"
		if(num == 3):
			print dragon2
			print "Poor unicorn :("

