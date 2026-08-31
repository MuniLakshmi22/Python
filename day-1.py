# ============================================================
# PYTHON DAY 1 - HOTEL FOOD ORDER
# Topics: Python basics, Variables, Data Types, Type Conversion,
#         Input and Output


print("Hello Python")


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


hotel_name = "Sunrise Hotel"
quantity = 2
price = 250.50
is_available = True

print(type(hotel_name))
print(type(quantity))
print(type(price))
print(type(is_available))


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


print("Hotel Name:", hotel_name)
print("Food Item:", food_item)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", is_available)


hotel_name = input("Enter hotel name: ")
food_item = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price
tax = total * 0.05
final_amount = total + tax

print()
print("----- HOTEL FOOD BILL -----")
print("Hotel Name:", hotel_name)
print("Food Item:", food_item)
print("Quantity:", quantity)
print("Price Per Item:", price)
print("Total:", total)
print("Tax:", tax)
print("Final Amount:", final_amount)