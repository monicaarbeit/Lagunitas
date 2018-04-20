# Created by Monica Arbeit 4/17/18
# Lagunitas Brewing Company
# Coding Challenge #1

from collections import Counter	

print ("Question 1.")

# Take in user input and input into list of strings
user_input = input("Enter text: ").split()
mylist = []
for word in user_input:
	mylist.append(word)

# Correctly print w/o "Counter"
first_comma = False 							# prevents printing out final comma
print("{", end="")
for word, value in Counter(mylist).items():
	if (first_comma):
		print(",", end=" ")
	print ("'%s': %d" % (word, value), end="")
	first_comma = True

print("}" + "\n")

# Coding Challenge #2

# Lists to flatten
thelist1 = [[1,2],3,[[4,5],6],7]	
thelist2 = [[1,10],3,[[3, 2,[1],5],6],7]	

print("Question 2.")

# Traverses tree to flatten a potentially nested list
def walk (o, tree_types=(list, tuple)):
	if isinstance(o, tree_types):
		for value in o:
			for subvalue in walk(value):
				yield subvalue
	else:
		yield o

# Prints the results from two lists
print("For the list: [[1,2],3,[[4,5],6],7]")
print("The function outputs: ", end="")
print(list(walk(thelist1)))	

print("For the list: [[1,10],3,[[3, 2,[1],5],6],7]")
print("The function outputs: ", end="")
print(list(walk(thelist2)))	
