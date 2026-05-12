"""
Day 18 - Number Patterns (Part 2)
"""

print("Pattern 1: Increasing Number Triangle")
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern 2: Repeated Number Pattern")
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

print("\nPattern 3: Floyd’s Number Triangle")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\nPattern 4: Reverse Number Pattern")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern 5: Right Aligned Number Pattern")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern 6: Palindrome Number Pattern")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
