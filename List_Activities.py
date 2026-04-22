#1. Basic List Activities
#Activity 1: Create a List

my_fruits=["Santol", "Mangga", "Bayabas"]
print(my_fruits)

#Activity 2: Access Items
#Task: Print the first and last item

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])

#🔹 Activity 3: List Length
#Task: Print how many items are in the list

colors = ["red", "blue", "green", "yellow"]
print(len(colors))

#2. Modify Lists
#Activity 4: Change Item
#Task: Replace "banana" with "orange"

fruits = ["apple", "banana", "cherry"]
fruits[1]="orange"
print(fruits)

#Activity 5: Add Items
#Task: 
# Add "mango" to the list
# Insert "grape" at index 1

fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "grape")
print(fruits)

#Activity 6: Remove Items
#Task:
#Remove "banana"
#Remove last item

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits.pop()
print(fruits)

#3. Looping Through Lists
#Activity 7: For Loop
#Task: Print each item

animals = ["dog", "cat", "bird"]
for x in animals:
 print(x)  

#Activity 8: With Index
#Task: Print index and value

numbers = [10, 20, 30]
for x,y in enumerate(numbers):
 print(x,":",y)

#List Operations
#Activity 9: Check if Item Exists
# Check if "banana" is in the list

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
 print("Banna is available")

#Activity 10: Sorting
# Sort ascending
# Sort descending
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

numbers.sort(reverse= True)
print(numbers)

#Activity 11: Copy List
# Create a copy of list1 into list2
list1 = ["a", "b", "c"]
list2 = list1.copy()
print(list2)


