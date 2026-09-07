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
#------------------------------------------------------------
#output
#Variables
#Name: Lakshmi
#Age: 20
#Student: True

# ============================================================
# 2. DATA TYPES
# ============================================================
# ------------------------------------------------------------
# int
# ------------------------------------------------------------
print("\nInteger")
print("Value:", age)
print("Type:", type(age))
#------------------------------------------------------------
#output
#Integer
#Value: 20
#Type: <class 'int'>

# ------------------------------------------------------------
# float
# ------------------------------------------------------------
price = 250.50
print("\nFloat")
print("Value:", price)
print("Type:", type(price))
#-------------------------------------------------------------
#output
#Float
#Value: 250.5
#Type: <class 'float'>

# ------------------------------------------------------------
# complex
# ------------------------------------------------------------
number = 3 + 4j
print("\nComplex")
print("Value:", number)
print("Type:", type(number))
#------------------------------------------------------------
#output
#Complex
#Value: (3+4j)
#Type: <class 'complex'>

# ------------------------------------------------------------
# string
# ------------------------------------------------------------
print("\nString")
print("Value:", name)
print("Type:", type(name))
#------------------------------------------------------------
#output
#String
#Value: Lakshmi
#Type: <class 'str'>

# ------------------------------------------------------------
# boolean
# ------------------------------------------------------------
print("\nBoolean")
print("Value:", is_student)
print("Type:", type(is_student))
#------------------------------------------------------------
#output
#Boolean
#Value: True
#Type: <class 'bool'>

# ------------------------------------------------------------
# list
# ------------------------------------------------------------
fruits = ["Apple", "Banana", "Mango"]
print("\nList")
print("Value:", fruits)
print("Type:", type(fruits))
#------------------------------------------------------------
#output
#List
#Value: ['Apple', 'Banana', 'Mango']
#Type: <class 'list'>

# ------------------------------------------------------------
# tuple
# ------------------------------------------------------------
colors = ("Red", "Green", "Blue")
print("\nTuple")
print("Value:", colors)
print("Type:", type(colors))
#------------------------------------------------------------
#output
#Tuple
#Value: ('Red', 'Green', 'Blue')
#Type: <class 'tuple'>

# ------------------------------------------------------------
# set
# ------------------------------------------------------------
numbers = {10, 20, 30}
print("\nSet")
print("Value:", numbers)
print("Type:", type(numbers))
#------------------------------------------------------------
#output
#Set
#Value: {10, 20, 30}
#Type: <class 'set'>

# ------------------------------------------------------------
# dictionary
# ------------------------------------------------------------
student = {
    "course": "Python"
}
print("\nDictionary")
print("Value:", student)
print("Type:", type(student))
#------------------------------------------------------------
#output
#Dictionary
#Value: {'course': 'Python'}
#Type: <class 'dict'>

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
#------------------------------------------------------------
#output
#String to Integer
#Value: 100
#Type: <class 'int'>

# ------------------------------------------------------------
# Integer -> Float
# ------------------------------------------------------------
number = float(number)
print("\nInteger to Float")
print("Value:", number)
print("Type:", type(number))
#------------------------------------------------------------
#output
#Integer to Float
#Value: 100.0
#Type: <class 'float'>

# ------------------------------------------------------------
# Float -> Integer
# ------------------------------------------------------------
price = int(price)
print("\nFloat to Integer")
print("Value:", price)
print("Type:", type(price))
#------------------------------------------------------------
#output
#Float to Integer
#Value: 250
#Type: <class 'int'>

# ------------------------------------------------------------
# Integer -> String
# ------------------------------------------------------------
number = str(number)
print("\nInteger to String")
print("Value:", number)
print("Type:", type(number))
#------------------------------------------------------------
#output
#Integer to String
#Value: 100.0
#Type: <class 'str'>

# ------------------------------------------------------------
# String -> Float
# ------------------------------------------------------------
price = float(price)
print("\nString to Float")
print("Value:", price)
print("Type:", type(price))
#------------------------------------------------------------
#output
#String to Float
#Value: 250.0
#Type: <class 'float'>

# ------------------------------------------------------------
# Integer -> Boolean
# ------------------------------------------------------------
number = 1
result = bool(number)
print("\nInteger to Boolean")
print("Value:", result)
print("Type:", type(result))
#------------------------------------------------------------
#output
#Integer to Boolean
#Value: True
#Type: <class 'bool'>

# ------------------------------------------------------------
# String -> Boolean
# ------------------------------------------------------------
text = "Python"
result = bool(text)
print("\nString to Boolean")
print("Value:", result)
print("Type:", type(result))
#------------------------------------------------------------
#output
#String to Boolean
#Value: True
#Type: <class 'bool'>

# ------------------------------------------------------------
# List -> Tuple
# ------------------------------------------------------------
result = tuple(fruits)
print("\nList to Tuple")
print("Value:", result)
print("Type:", type(result))
#------------------------------------------------------------
#output
#List to Tuple
#Value: ('Apple', 'Banana', 'Mango')
#Type: <class 'tuple'>

# ------------------------------------------------------------
# Tuple -> List
# ------------------------------------------------------------
result = list(colors)
print("\nTuple to List")
print("Value:", result)
print("Type:", type(result))
#-------------------------------------------------------------
#output
#Tuple to List
#Value: ['Red', 'Green', 'Blue']
#Type: <class 'list'>

# ------------------------------------------------------------
# List -> Set
# ------------------------------------------------------------
numbers = [10, 20, 20, 30]
result = set(numbers)
print("\nList to Set")
print("Value:", result)
print("Type:", type(result))
#------------------------------------------------------------
#output
#List to Set
#Value: {10, 20, 30}
#Type: <class 'set'>

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
#----------------------------------------------------------------
#output
#User Details
#Name: lucky
#Age: 20
#Salary: 5000000.0
#Data Types
#Name Type: <class 'str'>
#Age Type: <class 'int'>
#Salary Type: <class 'float'>
#Data Types
#Name Type: <class 'str'>
#Age Type: <class 'int'>
#Salary Type: <class 'float'>
