# ============================================================
# PYTHON DAY 1 - HOTEL FOOD ORDER
# Topics: Python basics, Variables, Data Types, Type Conversion,
#         Input and Output


# ------------------------------------------------------------
# 1. WHAT IS PYTHON?
# ------------------------------------------------------------
# Python is a high-level, interpreted programming language.
# It is simple, readable and easy to learn.
#
# Python is commonly used for:
# - Web development
# - Data Science
# - Artificial Intelligence / Machine Learning
# - Automation
# - Backend development
# - Testing

print("Hello Python")


# ------------------------------------------------------------
# 2. VARIABLES
# ------------------------------------------------------------
# A variable is a name used to store a value.
#
# Syntax:
# variable_name = value

hotel_name = "Sunrise Hotel"
food_item = "Chicken Biryani"
quantity = 2
price = 250.50
is_available = True

print(hotel_name)
print(food_item)
print(quantity)
print(price)
print(is_available)


# ------------------------------------------------------------
# 3. DATA TYPES
# ------------------------------------------------------------
# int   -> Whole numbers
# float -> Decimal numbers
# str   -> Text
# bool  -> True or False

hotel_name = "Sunrise Hotel"
quantity = 2
price = 250.50
is_available = True

print(type(hotel_name))
print(type(quantity))
print(type(price))
print(type(is_available))


# ------------------------------------------------------------
# 4. TYPE CONVERSION
# ------------------------------------------------------------
# Type conversion means changing one data type into another.
#
# int()   -> Integer
# float() -> Float
# str()   -> String
# bool()  -> Boolean


quantity_text = "2"
quantity_number = int(quantity_text)

print(quantity_number)
print(type(quantity_number))


price_text = "250.50"
price_number = float(price_text)

print(price_number)
print(type(price_number))


quantity_text = str(quantity_number)

print(quantity_text)
print(type(quantity_text))


# ------------------------------------------------------------
# 5. OUTPUT - print()
# ------------------------------------------------------------

print("Hotel Name:", hotel_name)
print("Food Item:", food_item)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", is_available)


# ------------------------------------------------------------
# 6. INPUT - input()
# ------------------------------------------------------------
# input() is used to take information from the user.
#
# input() always returns the entered value as a string.
#
# int(input()) converts input into an integer.
# float(input()) converts input into a float.


# ============================================================
# HOTEL FOOD ORDER
# ============================================================

hotel_name = input("Enter hotel name: ")
food_item = input("Enter food item: ")
availability = input("Is the food item available? (yes/no): ")


# ------------------------------------------------------------
# CHECK FOOD AVAILABILITY
# ------------------------------------------------------------

if availability.lower() == "yes":

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    total = quantity * price
    tax = total * 0.05
    final_amount = total + tax

    print()
    print("----- HOTEL FOOD BILL -----")
    print("Hotel Name:", hotel_name)
    print("Food Item:", food_item)
    print("Availability:", "Available")
    print("Quantity:", quantity)
    print("Price Per Item:", price)
    print("Total:", total)
    print("Tax:", tax)
    print("Final Amount:", final_amount)

else:

    print()
    print("----- HOTEL FOOD -----")
    print("Hotel Name:", hotel_name)
    print("Food Item:", food_item)
    print("Food Item is Not Available")


# ============================================================
# FINAL PRACTICE
# ============================================================
# Enter:
# - Hotel name
# - Food item
# - Availability
# - Quantity
# - Price
#
# If the food is available:
# Calculate total, tax and final amount.
#
# If the food is not available:
# Display "Food Item is Not Available".
# ============================================================