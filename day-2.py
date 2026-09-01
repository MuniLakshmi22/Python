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

#-------------------------------------------------------
#output
#------------------------------------------------------
Arithmetic Operators
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Modulus: 1
Floor Division: 3
Power: 1000

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

#-----------------------------------------------------------
#output
#-----------------------------------------------------------
Comparison Operators
Equal: False
Not Equal: True
Greater Than: True
Less Than: False
Greater Than or Equal: True
Less Than or Equal: False

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

#------------------------------------------------------------
#output
#------------------------------------------------------------
Assignment Operators
Initial: 10
After +=: 15
After -=: 12
After *=: 24
After /=: 6.0
After %=: 2.0

# ------------------------------------------------------------
# 4. LOGICAL OPERATORS
# ------------------------------------------------------------

age = 25
is_student = True
print("\nLogical Operators")
print("AND:", age > 18 and is_student)
print("OR:", age < 18 or is_student)
print("NOT:", not is_student)

#------------------------------------------------------------
#output
#------------------------------------------------------------
Logical Operators
AND: True
OR: True
NOT: False

# ------------------------------------------------------------
# 5. MEMBERSHIP OPERATORS
# ------------------------------------------------------------

foods = ["Biryani", "Pizza", "Burger", "Dosa"]
print("\nMembership Operators")
print("Pizza in foods:", "Pizza" in foods)
print("Rice in foods:", "Rice" in foods)
print("Burger not in foods:", "Burger" not in foods)
print("Cake not in foods:", "Cake" not in foods)

#------------------------------------------------------------
#output
#-----------------------------------------------------------
Membership Operators
Pizza in foods: True
Rice in foods: False
Burger not in foods: False
Cake not in foods: True

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

#-----------------------------------------------------------
#output
#-----------------------------------------------------------
Identity Operators
a is b: True
a is c: False
a is not c: True
