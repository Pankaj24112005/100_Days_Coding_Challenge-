# Python Operators with examples

print("=== PYTHON OPERATORS ===\n")

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)
print()

# 2. Comparison Operators
x = 5
y = 8
print("Comparison Operators:")
print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)
print()

# 3. Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q :", p and q)
print("p or q  :", p or q)
print("not p   :", not p)
print()

# 4. Assignment Operators
n = 10
print("Assignment Operators:")
n += 5
print("n += 5 ->", n)
n -= 3
print("n -= 3 ->", n)
n *= 2
print("n *= 2 ->", n)
n /= 4
print("n /= 4 ->", n)
print()

# 5. Bitwise Operators
m = 6   # 110
k = 3   # 011
print("Bitwise Operators:")
print("m & k :", m & k)
print("m | k :", m | k)
print("m ^ k :", m ^ k)
print("~m    :", ~m)
print("m << 1:", m << 1)
print("m >> 1:", m >> 1)
print()

# 6. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in my_list :", 3 in my_list)
print("10 not in my_list :", 10 not in my_list)
print()

# 7. Identity Operators
a = 10
b = 10
print("Identity Operators:")
print("a is b     :", a is b)
print("a is not b :", a is not b)
print()

print("=== END OF OPERATORS ===")
