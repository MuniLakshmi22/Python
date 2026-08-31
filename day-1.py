hotel_name = input("Enter hotel name: ")
food_item = input("Enter food item: ")
is_available = input("Is the food item available? (yes/no): ")

if is_available.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: "))

    total = quantity * price_per_item
    tax = total * 0.05
    final_amount = total + tax

    print("Hotel Name:", hotel_name)
    print("Food Item:", food_item)
    print("Food Available:", is_available)
    print("Quantity:", quantity)
    print("Price Per Item:", price_per_item)
    print("Total:", total)
    print("Tax:", tax)
    print("Final Amount:", final_amount)

else:
    print("Hotel Name:", hotel_name)
    print("Food Item:", food_item)
    print("Food Item is Not Available")