#Collections
# List
shopping_cart = ['Oreo', 'Oatmeal', 'milk']

# Tuple
my_info = ("Charlz", "Ferido", 18)

# Set
my_accounts = {'luv123', 'Ccf1001', '1007CRF'}

# Dictionary
my_fb = {
    "Username": "Charlz Ferido",
    "Age": 18,
    "Student": True
}

# --- Condition (if statement returning True/False) ---
age = my_fb["age"]

result = age >= 18  # condition

# --- Output ---
print("List:", shopping_cart)
print("Tuple:", my_info)
print("Set:", my_accounts)
print("Dictionary:", my_fb)

print("Is age 18 or above?", result)

# Optional if statement usage
if result:
    print("You are an adult.")
else:
    print("You are not an adult.") 