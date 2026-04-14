#List:
my_fruits = ["Mango", "Bayabas", "Orange", "Water Melo", "Dragonfruit"]
my_fruits.append("Santol")
my_fruits.remove("Orange")
my_fruits.sort()
print("Fruit List", my_fruits)

#Tuple:
tuple_fruits = ("Mango", "Bayabas", "Dragonfruit")
tuple_fruits[0] = "Santol"
#Tuple is immutable, which means you cannot change it, add, and remove.

#set:
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(3)
print(numbers)

#Dictionary
student_info = {
    "name": "Christian Charlz Ferido",
    "age": 18,
    "course": "BSIT"
}

student_info["grade"] = 1.0
student_info["age"] = 19
print(student_info.keys())