# ------------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# ------------------------------------------------------------

a = 10
b = 3
print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

# ------------------------------------------------------------
# 2. COMPARISON OPERATORS
# ------------------------------------------------------------

a = 10
b = 5
print("\nComparison Operators")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

# ------------------------------------------------------------
# 3. ASSIGNMENT OPERATORS
# ------------------------------------------------------------

x = 10
print("\nAssignment Operators")
print("Initial:", x)
x += 5
print("After +=:", x)
x -= 3
print("After -=:", x)
x *= 2
print("After *=:", x)
x /= 4
print("After /=:", x)
x %= 4
print("After %=:", x)

# ------------------------------------------------------------
# 4. LOGICAL OPERATORS
# ------------------------------------------------------------

age = 25
is_student = True
print("\nLogical Operators")
print("AND:", age > 18 and is_student)
print("OR:", age < 18 or is_student)
print("NOT:", not is_student)

# ------------------------------------------------------------
# 5. MEMBERSHIP OPERATORS
# ------------------------------------------------------------

foods = ["Biryani", "Pizza", "Burger", "Dosa"]
print("\nMembership Operators")
print("Pizza in foods:", "Pizza" in foods)
print("Rice in foods:", "Rice" in foods)
print("Burger not in foods:", "Burger" not in foods)
print("Cake not in foods:", "Cake" not in foods)

# ------------------------------------------------------------
# 6. IDENTITY OPERATORS
# ------------------------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("\nIdentity Operators")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)