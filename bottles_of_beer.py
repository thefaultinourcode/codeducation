#declaring how much alcohol is on the wall
bottles = 99

#for loop to go through all of the songs
for x in range(1,100):
	if(bottles==1):
		print bottles, "bottle of beer on the wall,", bottles, "bottle of beer. \nTake one down, pass it around,", bottles - 1, "bottles of beer on the wall."
	else:	
		print bottles, "bottles of beer on the wall,", bottles, "bottles of beer. \nTake one down, pass it around,", bottles - 1, "bottles of beer on the wall."
		bottles = bottles - 1