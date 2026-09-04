# ============================================================
# PYTHON DAY 5 - FUNCTIONS
# ============================================================
# ============================================================
# 1. DEFINING FUNCTIONS
# ============================================================

def greet():
    print("Hello, welcome to Python!")
print("----- DEFINING FUNCTION -----")
greet()
#-------------------------------------------------------------
#output
#----- DEFINING FUNCTION -----
#Hello, welcome to Python!

# ============================================================
# 2. ARGUMENTS & PARAMETERS
# ============================================================

# name and food are parameters
def order_food(name, food):
    print("Customer:", name)
    print("Food:", food)
print("\n----- ARGUMENTS & PARAMETERS -----")
# "Lakshmi" and "Biryani" are arguments
order_food("Lakshmi", "Biryani")
#-------------------------------------------------------------
#output
#----- ARGUMENTS & PARAMETERS -----
#Customer: Lakshmi
#Food: Biryani

# ============================================================
# 3. RETURN VALUES
# ============================================================

def calculate_total(price, quantity):
    total = price * quantity
    return total
print("\n----- RETURN VALUES -----")
amount = calculate_total(250, 2)
print("Price:", 250)
print("Quantity:", 2)
print("Total:", amount)
#-------------------------------------------------------------
#output
#----- RETURN VALUES -----
#Price: 250
#Quantity: 2
#Total: 500

# ============================================================
# 4. LAMBDA FUNCTIONS
# ============================================================

# Normal function
def square(number):
    return number * number
print("\n----- LAMBDA FUNCTION -----")
print("Normal Function:", square(5))
#-------------------------------------------------------------
#output
#----- LAMBDA FUNCTION -----
#Normal Function: 25

# Lambda function
square_lambda = lambda number: number * number
print("Lambda Function:", square_lambda(5))
#-------------------------------------------------------------
#output
#Lambda Function: 25

# Another lambda example
add = lambda a, b: a + b
print("Addition:", add(10, 20))
#-------------------------------------------------------------
#output
#Addition: 30

# ============================================================
# 5. SCOPE - LOCAL VARIABLE
# ============================================================

def local_example():
    message = "This is a local variable"
    print(message)
print("\n----- LOCAL SCOPE -----")
local_example()
#-------------------------------------------------------------
#output
#----- LOCAL SCOPE -----
#This is a local variable

# ============================================================
# 5. SCOPE - GLOBAL VARIABLE
# ============================================================

hotel_name = "Sunrise Hotel"
def global_example():
    print("Hotel Name:", hotel_name)
print("\n----- GLOBAL SCOPE -----")
global_example()
print("Outside Function:", hotel_name)
#-------------------------------------------------------------
#output
#----- GLOBAL SCOPE -----
#Hotel Name: Sunrise Hotel
#Outside Function: Sunrise Hotel

# ============================================================
# 6. LOCAL AND GLOBAL VARIABLES TOGETHER
# ============================================================

hotel = "Sunrise Hotel"       # Global variable
def show_details():
    food = "Chicken Biryani"  # Local variable
    print("Hotel:", hotel)
    print("Food:", food)
print("\n----- LOCAL & GLOBAL TOGETHER -----")
show_details()
#-------------------------------------------------------------
#output
#----- LOCAL & GLOBAL TOGETHER -----
#Hotel: Sunrise Hotel
#Food: Chicken Biryani

# ============================================================
# 7. RECURSION BASICS
# ============================================================
def countdown(number):
    # Base condition
    if number == 0:
        print("Done!")
        return
    print(number)
    # Function calls itself
    countdown(number - 1)
print("\n----- RECURSION -----")
countdown(5)
#-------------------------------------------------------------
#output
#----- RECURSION -----
#5
#4
#3
#2
#1
#Done!

# ============================================================
# 8. RECURSION - FACTORIAL EXAMPLE
# ============================================================
def factorial(number):
    # Base condition
    if number == 1:
        return 1
    # Recursive call
    return number * factorial(number - 1)
print("\n----- RECURSION FACTORIAL -----")
result = factorial(5)
print("Factorial of 5:", result)
#-------------------------------------------------------------
#output
#----- RECURSION FACTORIAL -----
#Factorial of 5: 120
