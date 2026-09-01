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
#o/p   Variables
Name: Lakshmi
Age: 20
Student: True

# ============================================================
# 2. DATA TYPES
# ============================================================
# ------------------------------------------------------------
# int
# ------------------------------------------------------------
age = 20
print("\nInteger")
print("Value:", age)
print("Type:", type(age))
#o/p  Integer
Value: 20
Type: <class 'int'>

# ------------------------------------------------------------
# float
# ------------------------------------------------------------
price = 250.50
print("\nFloat")
print("Value:", price)
print("Type:", type(price))
#o/p   Float
Value: 250.5
Type: <class 'float'>

# ------------------------------------------------------------
# complex
# ------------------------------------------------------------
number = 3 + 4j
print("\nComplex")
print("Value:", number)
print("Type:", type(number))
#o/p   Complex
Value: (3+4j)
Type: <class 'complex'>

# ------------------------------------------------------------
# string
# ------------------------------------------------------------
name = "Lakshmi"
print("\nString")
print("Value:", name)
print("Type:", type(name))
#o/p    String
Value: Lakshmi
Type: <class 'str'>

# ------------------------------------------------------------
# boolean
# ------------------------------------------------------------
is_student = True
print("\nBoolean")
print("Value:", is_student)
print("Type:", type(is_student))
#o/p   Boolean
Value: True
Type: <class 'bool'>

# ------------------------------------------------------------
# list
# ------------------------------------------------------------
fruits = ["Apple", "Banana", "Mango"]
print("\nList")
print("Value:", fruits)
print("Type:", type(fruits))
#o/p   List
Value: ['Apple', 'Banana', 'Mango']
Type: <class 'list'>

# ------------------------------------------------------------
# tuple
# ------------------------------------------------------------
colors = ("Red", "Green", "Blue")
print("\nTuple")
print("Value:", colors)
print("Type:", type(colors))
#o/p  Tuple
Value: ('Red', 'Green', 'Blue')
Type: <class 'tuple'>

# ------------------------------------------------------------
# set
# ------------------------------------------------------------
numbers = {10, 20, 30}
print("\nSet")
print("Value:", numbers)
print("Type:", type(numbers))
#o/p  Set
Value: {10, 20, 30}
Type: <class 'set'>

# ------------------------------------------------------------
# dictionary
# ------------------------------------------------------------
student = {
    "name": "Lakshmi",
    "age": 20,
    "course": "Python"
}
print("\nDictionary")
print("Value:", student)
print("Type:", type(student))
#o/p  Dictionary
Value: {'name': 'Lakshmi', 'age': 20, 'course': 'Python'}
Type: <class 'dict'>

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
#o/p   String to Integer
Value: 100
Type: <class 'int'>

# ------------------------------------------------------------
# Integer -> Float
# ------------------------------------------------------------
number = 100
number = float(number)
print("\nInteger to Float")
print("Value:", number)
print("Type:", type(number))
#o/p   Integer to Float
Value: 100.0
Type: <class 'float'>

# ------------------------------------------------------------
# Float -> Integer
# ------------------------------------------------------------
price = 250.75
price = int(price)
print("\nFloat to Integer")
print("Value:", price)
print("Type:", type(price))
#o/p    Float to Integer
Value: 250
Type: <class 'int'>

# ------------------------------------------------------------
# Integer -> String
# ------------------------------------------------------------
number = 100
number = str(number)
print("\nInteger to String")
print("Value:", number)
print("Type:", type(number))
#o/p    Integer to String
Value: 100
Type: <class 'str'>

# ------------------------------------------------------------
# String -> Float
# ------------------------------------------------------------
price = "250.50"
price = float(price)
print("\nString to Float")
print("Value:", price)
print("Type:", type(price))
#o/p   String to Float
Value: 250.5
Type: <class 'float'>

# ------------------------------------------------------------
# Integer -> Boolean
# ------------------------------------------------------------
number = 1
result = bool(number)
print("\nInteger to Boolean")
print("Value:", result)
print("Type:", type(result))
#o/p   Integer to Boolean
Value: True
Type: <class 'bool'>

# ------------------------------------------------------------
# String -> Boolean
# ------------------------------------------------------------
text = "Python"
result = bool(text)
print("\nString to Boolean")
print("Value:", result)
print("Type:", type(result))
#o/p   String to Boolean
Value: True
Type: <class 'bool'>

# ------------------------------------------------------------
# List -> Tuple
# ------------------------------------------------------------
fruits = ["Apple", "Banana", "Mango"]
result = tuple(fruits)
print("\nList to Tuple")
print("Value:", result)
print("Type:", type(result))
#o/p     List to Tuple
Value: ('Apple', 'Banana', 'Mango')
Type: <class 'tuple'>

# ------------------------------------------------------------
# Tuple -> List
# ------------------------------------------------------------
colors = ("Red", "Green", "Blue")
result = list(colors)
print("\nTuple to List")
print("Value:", result)
print("Type:", type(result))
#o/p    Tuple to List
Value: ['Red', 'Green', 'Blue']
Type: <class 'list'>

# ------------------------------------------------------------
# List -> Set
# ------------------------------------------------------------
numbers = [10, 20, 20, 30]
result = set(numbers)
print("\nList to Set")
print("Value:", result)
print("Type:", type(result))
#o/p    List to Set
Value: {10, 20, 30}
Type: <class 'set'>

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
#o/p    INPUT WITH TYPE CONVERSION
User Details
Name: lakshmi
Age: 20
Salary: 500000.0
Data Types
Name Type: <class 'str'>
Age Type: <class 'int'>
Salary Type: <class 'float'>
