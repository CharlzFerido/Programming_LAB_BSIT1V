# A program for you to calculate the length of a string.
x="Christian"
print("Length:", len(x))

#  A program counts the number of characters in a string.
x="Christian"
count=len(x)
print("Number of Characters:", count)

#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
x = "Christian"
first = x[0]
new_string = first + x[1:].replace(first, "$")

print("Modified string:", new_string)

#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
x=("Christian")
y=("Ferido")
new_x= x[:2] + y[2:]
new_y= y[:2] + x[2:]
print("Result:", new_x + " " + new_y)

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
a="Hello"
b= "I'm"
c= "Charlz"
d= "Ferido"

print( a + " " + b + " " + c + " " + d)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them
x= input("Enter First String: ")
y= input("Enter Second String: ")

print("Result:", x + " " + y)

# Using + Concatenate in Python using your name and your age in a paragraph
name= input("Enter your Name: ")
age= input("Enter your Age: ")
print( "Hi! I am " + name + ", " + age + " years old"  )



