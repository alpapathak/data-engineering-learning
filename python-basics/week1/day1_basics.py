# Day 1: Python Basics
# Author: alpapathak
# Date: [Today's date]

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

# Integers
age = 30
year = 2025
print(f"Age: {age}, Year: {year}")

# Floats
temperature = 72.5
pi = 3.14159
print(f"Temperature: {temperature}°F")

# Strings
name = "Data Engineer"
language = "Python"
print(f"I am a {name} learning {language}")

# Booleans
is_learning = True
is_expert = False
print(f"Currently learning: {is_learning}")

# None (null in other languages)
result = None
print(f"Result before calculation: {result}")

# ============================================
# 2. BASIC OPERATORS
# ============================================

# Arithmetic
x = 10
y = 3

print(f"\nArithmetic Operations:")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")  # Float division
print(f"{x} // {y} = {x // y}")  # Integer division
print(f"{x} % {y} = {x % y}")  # Modulo
print(f"{x} ** {y} = {x ** y}")  # Power

# Comparison
print(f"\nComparison Operations:")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")

# Logical
a = True
b = False
print(f"\nLogical Operations:")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# ============================================
# 3. STRING OPERATIONS
# ============================================

first_name = "Data"
last_name = "Engineer"

# Concatenation
full_name = first_name + " " + last_name
print(f"\nFull name: {full_name}")

# String methods
message = "hello data engineering"
print(f"Uppercase: {message.upper()}")
print(f"Capitalize: {message.capitalize()}")
print(f"Title case: {message.title()}")
print(f"Length: {len(message)}")
print(f"Contains 'data': {'data' in message}")

# String formatting (3 ways)
name = "alpapathak"
day = 1

# Method 1: f-strings (modern, recommended)
print(f"My name is {name} and today is Day {day}")

# Method 2: .format()
print("My name is {} and today is Day {}".format(name, day))

# Method 3: % formatting (old style)
print("My name is %s and today is Day %d" % (name, day))

# ============================================
# 4. TYPE CONVERSION
# ============================================

# String to int
age_str = "25"
age_int = int(age_str)
print(f"\nConverted '{age_str}' to {age_int}, type: {type(age_int)}")

# Int to string
number = 100
number_str = str(number)
print(f"Converted {number} to '{number_str}', type: {type(number_str)}")

# String to float
price_str = "19.99"
price = float(price_str)
print(f"Converted '{price_str}' to {price}, type: {type(price)}")

print("\n✅ Day 1 Basics Complete!")