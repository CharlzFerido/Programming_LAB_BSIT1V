# Part 1: Identify & Create (Warm-up)

my_fruits = ("Mango", "Bayabas", "Orange", "Water Melo", "Dragonfruit") # favorite fruit
my_dailytask = ["wake up", "eat breakfast", "attend class", "do homework", "sleep"] # daily task
numbers = [1, 2, 3, 4, 5]

# Dictionary
student_info = {
    "name": "Christian Charlz Ferido",
    "age": 18,
    "course": "BSIT"
}

# Part 2: Manipulation Challenge
#List Tasks:
my_dailytask.append("exercise")
my_dailytask.remove("sleep")
my_dailytask.sort()

#Tuple Tasks:
#fruits[0] = "Santol"
# It will cause error because tuples are immutable

# Set Tasks:
numbers.add(6)
numbers.remove(5)
# Show duplicates removed
numbers = [1, 2, 2, 3, 4, 4, 5]
numbers = set(numbers)
print(numbers)

#Dictionary Tasks:
student_info["grade"] = 1.0
student_info["age"] = 19


# Print all keys and values
print(student_info.keys())
print(student_info.values())
print(student_info)