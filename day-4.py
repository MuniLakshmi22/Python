# ============================================================
# PYTHON DAY 4 - DATA STRUCTURES
# ============================================================
# ============================================================
# 1. LISTS
# ============================================================

foods = ["Biryani", "Pizza", "Burger", "Dosa"]
print("LIST:")
print(foods)

# Accessing list items
print("First Food:", foods[0])
print("Second Food:", foods[1])

# Adding an item
foods.append("Fried Rice")
print("After append:", foods)

# Removing an item
foods.remove("Burger")
print("After remove:", foods)

# Changing an item
foods[0] = "Chicken Biryani"
print("After changing:", foods)

# List length
print("Number of foods:", len(foods))


# ============================================================
# 2. TUPLES
# ============================================================

food_prices = (250, 180, 150, 100)
print("\nTUPLE:")
print(food_prices)

# Accessing tuple items
print("First Price:", food_prices[0])
print("Second Price:", food_prices[1])

# Tuple length
print("Number of prices:", len(food_prices))

# ============================================================
# 3. SETS
# ============================================================

food_categories = {"Indian", "Chinese", "Italian", "Indian"}
print("\nSET:")
print(food_categories)

# Duplicate "Indian" is automatically removed.
# Adding an item
food_categories.add("Mexican")
print("After add:", food_categories)

# Removing an item
food_categories.remove("Chinese")
print("After remove:", food_categories)

# Checking membership
print("Is Italian available?", "Italian" in food_categories)

# ============================================================
# 4. DICTIONARIES
# ============================================================

food = {
    "name": "Chicken Biryani",
    "price": 250,
    "quantity": 2,
    "category": "Indian"
}
print("\nDICTIONARY:")
print(food)

# Accessing values
print("Food Name:", food["name"])
print("Price:", food["price"])

# Adding a new key
food["restaurant"] = "Sunrise Hotel"
print("After adding:", food)

# Updating a value
food["price"] = 280
print("After updating price:", food)

# Removing a key
food.pop("quantity")
print("After removing quantity:", food)

# Dictionary keys
print("Keys:", food.keys())

# Dictionary values
print("Values:", food.values())

# ============================================================
# 5. STRING METHODS
# ============================================================

food_name = "  chicken biryani  "
print("\nSTRING METHODS:")
# upper()
print("Upper:", food_name.upper())

# lower()
print("Lower:", food_name.lower())

# strip()
print("Strip:", food_name.strip())

# replace()
print("Replace:", food_name.replace("chicken", "mutton"))

# title()
print("Title:", food_name.title())

# capitalize()
print("Capitalize:", food_name.capitalize())

# split()
sentence = "Biryani Pizza Burger"
print("Split:", sentence.split())

# startswith()
print("Starts with chicken:",
      food_name.strip().startswith("chicken"))

# endswith()
print("Ends with biryani:",
      food_name.strip().endswith("biryani"))

# find()
print("Position of biryani:",
      food_name.find("biryani"))
# count()
text = "biryani biryani pizza"
print("Biryani count:", text.count("biryani"))

# ============================================================
# 6. LIST COMPREHENSION
# ============================================================

prices = [100, 200, 300, 400, 500]

# Normal way:
double_prices = []
for price in prices:
    double_prices.append(price * 2)
print("\nLIST COMPREHENSION:")
print("Normal list:", double_prices)

# List comprehension:
double_prices = [price * 2 for price in prices]
print("Using comprehension:", double_prices)

# List comprehension with condition
expensive_prices = [price for price in prices if price >= 300]
print("Prices >= 300:", expensive_prices)

# ============================================================
# 7. DICTIONARY COMPREHENSION
# ============================================================

foods = ["Biryani", "Pizza", "Burger"]
prices = [250, 200, 150]

# Create dictionary using comprehension
food_menu = {
    food: price
    for food, price in zip(foods, prices)
}
print("\nDICTIONARY COMPREHENSION:")
print("Food Menu:", food_menu)

# Dictionary comprehension with condition
expensive_foods = {
    food: price
    for food, price in food_menu.items()
    if price >= 200
}
print("Foods with price >= 200:", expensive_foods)