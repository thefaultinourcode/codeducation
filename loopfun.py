name = ['L','e','a','h',' ','R','a','m','s','i','e','r']

grades = [100, 90, 95, 85.5, 100]


for x in name:
	print x

total = 0
counter = 0



for x in grades:
	counter = counter + 1
	print "Grade", counter, ":", x
	total = x + total
	

grade_avg = total/counter

print grade_avg

num_grades = int(raw_input("How many grades do you need to enter?"))

user_grades=[]

total = 0
counter = 0

for x in range(0, num_grades):
	y = int(raw_input("Enter grade: "))
	user_grades.append(y)
	total = total + y
	counter = counter + 1

grade_avg = total/counter
print grade_avg
