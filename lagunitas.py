# Created by Monica Arbeit 4/17/18
# Lagunitas Brewing Company
# Coding Challenge #1

from collections import Counter	

print ("Question 1.")
user_input = input("Enter text: ").split()

first_list = []
for work in user_input:
	first_list.append(work)

first_comma = False 		# prevents printing out final comma
print("{", end="")
for word, value in Counter(first_list).items():
	if (first_comma):
		print(",", end=" ")
	print ("'%s': %d" % (word, value), end="")
	first_comma = True

print("}" + "\n")

# Coding Challenge #2

thelist = [[1,2],3,[[4,5],6],7]	
thelist2 = [[1,10],3,[[3, 2,[1],5],6],7]	

print("Question 2.")

def walk (o, tree_types=(list, tuple)):
	if isinstance(o, tree_types):
		for value in o:
			for subvalue in walk(value):
				yield subvalue
	else:
		yield o

print("For the list: [[1,2],3,[[4,5],6],7]")
print("The function outputs: ", end="")
print(list(walk(thelist)))	

print("For the list: [[1,10],3,[[3, 2,[1],5],6],7]")
print("The function outputs: ", end="")
print(list(walk(thelist2)))	
