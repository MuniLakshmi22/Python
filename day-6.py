# ============================================================
# PYTHON DAY 6 - MODULES & PACKAGES
# ============================================================
# ============================================================
# 1. IMPORTING MODULES
# ============================================================
import math
print("----- IMPORTING MODULE -----")
print("Square root of 25:", math.sqrt(25))
print("Value of Pi:", math.pi)
#-------------------------------------------------------------
# OUTPUT:
# ----- IMPORTING MODULE -----
# Square root of 25: 5.0
# Value of Pi: 3.141592653589793

# ============================================================
# 2. CREATING MY OWN MODULE
# ============================================================
def greet(name):
    return "Hello " + name
def add(a, b):
    return a + b
def food_bill(price, quantity):
    return price * quantity
print("\n----- MY OWN MODULE -----")
print("Greeting:", greet("Lakshmi"))
print("Addition:", add(10, 20))
print("Food Bill:", food_bill(250, 2))
#-------------------------------------------------------------
# OUTPUT:
# ----- MY OWN MODULE -----
# Greeting: Hello Lakshmi
# Addition: 30
# Food Bill: 500

# ============================================================
# 3. MATH MODULE
# ============================================================
print("\n----- MATH MODULE -----")
number = 16
print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Absolute value:", math.fabs(-10))
print("Pi:", math.pi)
#-------------------------------------------------------------
# OUTPUT:
# ----- MATH MODULE -----
# Square root: 4.0
# Power: 8.0
# Ceiling: 5
# Floor: 4
# Absolute value: 10.0
# Pi: 3.141592653589793

# ============================================================
# 4. RANDOM MODULE
# ============================================================
import random
print("\n----- RANDOM MODULE -----")
foods = ["Biryani", "Pizza", "Burger", "Dosa"]
print("Random food:", random.choice(foods))
print("Random number:", random.randint(1, 10))
#-------------------------------------------------------------
# OUTPUT:
# ----- RANDOM MODULE -----
# Random food: Dosa
# Random number: 6

# ============================================================
# 5. DATETIME MODULE
# ============================================================
import datetime
print("\n----- DATETIME MODULE -----")
current_date = datetime.date.today()
print("Today's date:", current_date)
current_time = datetime.datetime.now()
print("Current date and time:", current_time)
#-------------------------------------------------------------
# OUTPUT:
# ----- DATETIME MODULE -----
# Today's date: 2026-09-09
# Current date and time: 2026-09-09 11:30:25.123456

# ============================================================
# 6. DATETIME - CREATING A SPECIFIC DATE
# ============================================================
specific_date = datetime.date(2026, 12, 25)
print("\n----- SPECIFIC DATE -----")
print("Date:", specific_date)
print("Year:", specific_date.year)
print("Month:", specific_date.month)
print("Day:", specific_date.day)
#-------------------------------------------------------------
# OUTPUT:
# ----- SPECIFIC DATE -----
# Date: 2026-12-25
# Year: 2026
# Month: 12
# Day: 25

# ============================================================
# 7. OS MODULE
# ============================================================
import os
print("\n----- OS MODULE -----")
print("Current folder:")
print(os.getcwd())
#-------------------------------------------------------------
# OUTPUT:
# ----- OS MODULE -----
# Current folder:
# C:\Users\YourName\Desktop\Python

# ============================================================
# 8. PLATFORM MODULE
# ============================================================
import platform
print("\n----- PLATFORM MODULE -----")
print("Operating System:", platform.system())
print("Python Version:", platform.python_version())
#-------------------------------------------------------------
# OUTPUT:
# ----- PLATFORM MODULE -----
# Operating System: Windows
# Python Version: 3.12.4

# ============================================================
# 9. USING FROM TO IMPORT A SPECIFIC FUNCTION
# ============================================================
from math import sqrt
print("\n----- FROM IMPORT -----")
print("Square root of 81:", sqrt(81))
#-------------------------------------------------------------
# OUTPUT:
# ----- FROM IMPORT -----
# Square root of 81: 9.0

# ============================================================
# 10. USING AN ALIAS
# ============================================================
import math as m
print("\n----- MODULE ALIAS -----")
print("Square root of 100:", m.sqrt(100))
print("Pi:", m.pi)
#-------------------------------------------------------------
# OUTPUT:
# ----- MODULE ALIAS -----
# Square root of 100: 10.0
# Pi: 3.141592653589793
