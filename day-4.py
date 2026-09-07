# ============================================================
# PYTHON DAY 4 - DATA STRUCTURES
# ============================================================
# ============================================================
# 1. LISTS
# ============================================================
foods = ["Biryani", "Pizza", "Burger", "Dosa"]
print("LIST:")
print(foods)
#------------------------------------------------------------
#output
#['Biryani', 'Pizza', 'Burger', 'Dosa']
#------------------------------------------------------------

# Accessing list items
print("First Food:", foods[0])
print("Second Food:", foods[1])
#-----------------------------------------------------------
#output
#First Food: Biryani
#Second Food: Pizza
#----------------------------------------------------------

# Adding an item
foods.append("Fried Rice")
print("After append:", foods)
#----------------------------------------------------------
#output
#After append: ['Biryani', 'Pizza', 'Burger', 'Dosa', 'Fried Rice']
#-----------------------------------------------------------------

# Removing an item
foods.remove("Burger")
print("After remove:", foods)
#-----------------------------------------------------------------
#output
#After remove: ['Biryani', 'Pizza', 'Dosa', 'Fried Rice']
#-----------------------------------------------------------------

# Changing an item
foods[0] = "Chicken Biryani"
print("After changing:", foods)
#-----------------------------------------------------------------
#output
#After changing: ['Chicken Biryani', 'Pizza', 'Dosa', 'Fried Rice']
#-----------------------------------------------------------------

# List length
print("Number of foods:", len(foods))
#----------------------------------------------------------------
#output
#Number of foods: 4
#----------------------------------------------------------------

# ============================================================
# 2. TUPLES
# ============================================================

food_prices = (250, 180, 150, 100)
print("\nTUPLE:")
print(food_prices)
#---------------------------------------------------------------
#output
#TUPLE:
#(250, 180, 150, 100)
#--------------------------------------------------------------

# Accessing tuple items
print("First Price:", food_prices[0])
print("Second Price:", food_prices[1])
#------------------------------------------------------------
#output
#First Price: 250
#Second Price: 180
#-----------------------------------------------------------

# Tuple length
print("Number of prices:", len(food_prices))
#------------------------------------------------------------
#output
#Number of prices: 4
#------------------------------------------------------------

# ============================================================
# 3. SETS
# ============================================================

food_categories = {"Indian", "Chinese", "Italian", "Indian"}
print("\nSET:")
print(food_categories)
#----------------------------------------------------------
#output
#SET:
#{'Chinese', 'Italian', 'Indian'}
#---------------------------------------------------------

# Duplicate "Indian" is automatically removed.
# Adding an item
food_categories.add("Mexican")
print("After add:", food_categories)
#--------------------------------------------------------
#output
#After add: {'Chinese', 'Mexican', 'Italian', 'Indian'}
#--------------------------------------------------------

# Removing an item
food_categories.remove("Chinese")
print("After remove:", food_categories)
#--------------------------------------------------------
#output
#After remove: {'Mexican', 'Italian', 'Indian'}
#---------------------------------------------------------
# Checking membership
print("Is Italian available?", "Italian" in food_categories)
#----------------------------------------------------------
#output
#Is Italian available? True
#----------------------------------------------------------

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
#--------------------------------------------------------------
#output
#DICTIONARY:
#{'name': 'Chicken Biryani', 'price': 250, 'quantity': 2, 'category': 'Indian'}
#-----------------------------------------------------------------

# Accessing values
print("Food Name:", food["name"])
print("Price:", food["price"])
#-------------------------------------------------------------------
#output
#Food Name: Chicken Biryani
#Price: 250
#------------------------------------------------------------------

# Adding a new key
food["restaurant"] = "Sunrise Hotel"
print("After adding:", food)
#------------------------------------------------------------------
#output
#After adding: {'name': 'Chicken Biryani', 'price': 250, 'quantity': 2, 'category': 'Indian', 'restaurant': 'Sunrise Hotel'}
#------------------------------------------------------------------

# Updating a value
food["price"] = 280
print("After updating price:", food)
#-----------------------------------------------------------------
#output
#After updating price: {'name': 'Chicken Biryani', 'price': 280, 'quantity': 2, 'category': 'Indian', 'restaurant': 'Sunrise Hotel'}
#------------------------------------------------------------------

# Removing a key
food.pop("quantity")
print("After removing quantity:", food)
#------------------------------------------------------------------
#output
#After removing quantity: {'name': 'Chicken Biryani', 'price': 280, 'category': 'Indian', 'restaurant': 'Sunrise Hotel'}
#-------------------------------------------------------------------
# Dictionary keys
print("Keys:", food.keys())
#------------------------------------------------------------------
#output
#Keys: dict_keys(['name', 'price', 'category', 'restaurant'])
#------------------------------------------------------------------

# Dictionary values
print("Values:", food.values())
#-------------------------------------------------------------------
#output
#Values: dict_values(['Chicken Biryani', 280, 'Indian', 'Sunrise Hotel'])
#---------------------------------------------------------------------

# ============================================================
# 5. STRING METHODS
# ============================================================

food_name = "  chicken biryani  "
print("\nSTRING METHODS:")
#output
#STRING METHODS:
# upper()
print("Upper:", food_name.upper())
# output Upper:   CHICKEN BIRYANI 
# lower()
print("Lower:", food_name.lower())
#output Lower:   chicken biryani 
# strip()
print("Strip:", food_name.strip())
#output Strip: chicken biryani
# replace()
print("Replace:", food_name.replace("chicken", "mutton"))
#output Replace:   mutton biryani 
# title()
print("Title:", food_name.title())
#output Title:   Chicken Biryani  
# capitalize()
print("Capitalize:", food_name.capitalize())
#output Capitalize:   chicken biryani
# split()
sentence = "Biryani Pizza Burger"
print("Split:", sentence.split())
#output Split: ['Biryani', 'Pizza', 'Burger']
# startswith()
print("Starts with chicken:",
      food_name.strip().startswith("chicken"))
#output Starts with chicken: True
# endswith()
print("Ends with biryani:",
      food_name.strip().endswith("biryani"))
#output Ends with biryani: True
# find()
print("Position of biryani:",
      food_name.find("biryani"))
#output Position of biryani: 10
# count()
text = "biryani biryani pizza"
print("Biryani count:", text.count("biryani"))
#output Biryani count: 2

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
#---------------------------------------------------------------
#output 
#LIST COMPREHENSION:
#Normal list: [200, 400, 600, 800, 1000]
#---------------------------------------------------------------
# List comprehension:
double_prices = [price * 2 for price in prices]
print("Using comprehension:", double_prices)
#output Using comprehension: [200, 400, 600, 800, 1000]
# List comprehension with condition
expensive_prices = [price for price in prices if price >= 300]
print("Prices >= 300:", expensive_prices)
#output Prices >= 300: [300, 400, 500]

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
#----------------------------------------------------------------
#output
#DICTIONARY COMPREHENSION:
#Food Menu: {'Biryani': 250, 'Pizza': 200, 'Burger': 150}
#---------------------------------------------------------------
# Dictionary comprehension with condition
expensive_foods = {
    food: price
    for food, price in food_menu.items()
    if price >= 200
}
print("Foods with price >= 200:", expensive_foods)
#output Foods with price >= 200: {'Biryani': 250, 'Pizza': 200}
