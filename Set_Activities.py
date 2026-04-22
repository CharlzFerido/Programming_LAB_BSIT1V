#Set Activities (Unique values, unordered, no duplicates)
#Sets do not allow duplicate values and are unordered

#Activity 1: Remove Duplicates
# Convert to set and print unique values

numbers = [1, 2, 2, 3, 4, 4, 5]
x=set(numbers)
print(x)

#Activity 2: Add and Remove
# Add "orange"
# Remove "banana"
fruits = {"apple","banana"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)

#Activity 3: Set Operations
# Find:
# union
# intersection
A = {1, 2, 3}
B = {3, 4, 5}

c=A.union(B)
print(c)
C=A.intersection(B)
print(C)

#Activity 4 (Challenge): Common Students
#Given:
classA = {"John", "Ana", "Mark"}
classB = {"Ana", "Mark", "Liza"}

classC=classA.intersection(classB)
print(classC)
classC=classA.union(classB)
print(classC)

#Task:
#Find students in BOTH classes
#Find ALL students






