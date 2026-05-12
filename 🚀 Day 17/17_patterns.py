# Day 17: Star Patterns in Python

n = 5

# 1. Right Triangle Pattern
print("Right Triangle Pattern")
for i in range(1, n + 1):
    print("*" * i)

print()

# 2. Inverted Right Triangle Pattern
print("Inverted Right Triangle Pattern")
for i in range(n, 0, -1):
    print("*" * i)

print()

# 3. Pyramid Pattern
print("Pyramid Pattern")
for i in range(n):
    spaces = n - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)

print()

# 4. Inverted Pyramid Pattern
print("Inverted Pyramid Pattern")
for i in range(n):
    spaces = i
    stars = 2 * (n - i) - 1
    print(" " * spaces + "*" * stars)

print()

# 5. Diamond Pattern
print("Diamond Pattern")

# upper part
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# lower part
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
