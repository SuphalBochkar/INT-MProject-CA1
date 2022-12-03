# Python3 implementation of the approach

# Function to print the name of student who
# stood first after updation in rank
		
	highest = x[0]
	for j in range(1, n):
		if (x[j][1] >= highest[1]):
			highest = x[j]
			
	# Print the name and jump in rank
	print("Name: ", highest[0], ", Jump: ",
			abs(highest[2] - 1), sep="")

# Driver code

# Names of the students
names= ["sam", "ram", "geek"]

# Marks of the students
marks = [80, 79, 75]

# Updates that are to be done
updates = [0, 5, -9]

# Number of students
n = len(marks)

nameRank(names, marks, updates, n)

# This code is contributed by SHUBHAMSINGH10
