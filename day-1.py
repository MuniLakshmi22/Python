# ============================================================
# PYTHON - VARIABLES, DATA TYPES AND TYPE CONVERSION
# ============================================================
# ============================================================
# 1. VARIABLES
# ============================================================
name = "Lakshmi"
age = 20
is_student = True
print("Variables")
print("Name:", name)
print("Age:", age)
print("Student:", is_student)

# ============================================================
# 2. DATA TYPES
# ============================================================
# ------------------------------------------------------------
# int
# ------------------------------------------------------------
print("\nInteger")
print("Value:", age)
print("Type:", type(age))

# ------------------------------------------------------------
# float
# ------------------------------------------------------------
price = 250.50
print("\nFloat")
print("Value:", price)
print("Type:", type(price))

# ------------------------------------------------------------
# complex
# ------------------------------------------------------------
number = 3 + 4j
print("\nComplex")
print("Value:", number)
print("Type:", type(number))

# ------------------------------------------------------------
# string
# ------------------------------------------------------------
print("\nString")
print("Value:", name)
print("Type:", type(name))

# ------------------------------------------------------------
# boolean
# ------------------------------------------------------------
print("\nBoolean")
print("Value:", is_student)
print("Type:", type(is_student))

# ------------------------------------------------------------
# list
# ------------------------------------------------------------
fruits = ["Apple", "Banana", "Mango"]
print("\nList")
print("Value:", fruits)
print("Type:", type(fruits))

# ------------------------------------------------------------
# tuple
# ------------------------------------------------------------
colors = ("Red", "Green", "Blue")
print("\nTuple")
print("Value:", colors)
print("Type:", type(colors))

# ------------------------------------------------------------
# set
# ------------------------------------------------------------
numbers = {10, 20, 30}
print("\nSet")
print("Value:", numbers)
print("Type:", type(numbers))

# ------------------------------------------------------------
# dictionary
# ------------------------------------------------------------
student = {
    "course": "Python"
}
print("\nDictionary")
print("Value:", student)
print("Type:", type(student))

# ============================================================
# 3. TYPE CONVERSION
# ============================================================
# ------------------------------------------------------------
# String -> Integer
# ------------------------------------------------------------
number = "100"
number = int(number)
print("\nString to Integer")
print("Value:", number)
print("Type:", type(number))

# ------------------------------------------------------------
# Integer -> Float
# ------------------------------------------------------------
number = float(number)
print("\nInteger to Float")
print("Value:", number)
print("Type:", type(number))

# ------------------------------------------------------------
# Float -> Integer
# ------------------------------------------------------------
price = int(price)
print("\nFloat to Integer")
print("Value:", price)
print("Type:", type(price))

# ------------------------------------------------------------
# Integer -> String
# ------------------------------------------------------------
number = str(number)
print("\nInteger to String")
print("Value:", number)
print("Type:", type(number))

# ------------------------------------------------------------
# String -> Float
# ------------------------------------------------------------
price = float(price)
print("\nString to Float")
print("Value:", price)
print("Type:", type(price))

# ------------------------------------------------------------
# Integer -> Boolean
# ------------------------------------------------------------
number = 1
result = bool(number)
print("\nInteger to Boolean")
print("Value:", result)
print("Type:", type(result))

# ------------------------------------------------------------
# String -> Boolean
# ------------------------------------------------------------
text = "Python"
result = bool(text)
print("\nString to Boolean")
print("Value:", result)
print("Type:", type(result))

# ------------------------------------------------------------
# List -> Tuple
# ------------------------------------------------------------
result = tuple(fruits)
print("\nList to Tuple")
print("Value:", result)
print("Type:", type(result))

# ------------------------------------------------------------
# Tuple -> List
# ------------------------------------------------------------
result = list(colors)
print("\nTuple to List")
print("Value:", result)
print("Type:", type(result))

# ------------------------------------------------------------
# List -> Set
# ------------------------------------------------------------
numbers = [10, 20, 20, 30]
result = set(numbers)
print("\nList to Set")
print("Value:", result)
print("Type:", type(result))

# ============================================================
# 4. INPUT WITH TYPE CONVERSION
# ============================================================

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print("\nUser Details")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("\nData Types")
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Salary Type:", type(salary))
print("\nData Types")
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Salary Type:", type(salary))