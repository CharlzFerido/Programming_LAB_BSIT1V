#Dictionary Activities
#(Key-value pairs, editable, accessed by keys)
#Dictionaries store data as key:value pairs

#Activity 1: Fill in the Blanks
student = {
   "name": "Ana",
   "age": 20,
   "course": "IT"
}

print(student["name"])


#Activity 2: Add and Update
#Task:
#1. Add "grade": 95
#2. Change age to 21

student = {"name": "Ana", "age": 20}
student["grade"]= 95
student["age"]= 21

# Activity 3: Loop Through Dictionary
# Task: Print all keys and values
# Expected output:
# brand : Toyota
# model : Corolla
# year : 2020

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

for x,y in car.items():
    print(x, ":", y)

# Activity 4 (Challenge): Mini Phonebook

numbers={
    "Jirus": 9519526826,
    "jeshley": 9925583351,
    "Ced": 9162173629,
    "jerone": 9389386772,
}
name=input("Enter name: ")
print("Phone No. of", numbers[name])
