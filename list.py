import random

arr = []

arr_size = random.randint(0,100)

print arr_size

count = 0

for i in range(0, arr_size):
	rand = random.randint(1,1001)
	arr.append(rand)

x = len(arr)

print x

for r in arr:
	print r
