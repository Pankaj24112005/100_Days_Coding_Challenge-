# Day 19: Alphabet Pattern Printing in Python

print("Pattern 1: Alphabet Square")
n = 4
for i in range(n):
    ch = ord('A')
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\nPattern 2: Increasing Alphabet Triangle")
n = 4
for i in range(1, n + 1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\nPattern 3: Continuous Alphabet Pattern")
n = 4
ch = ord('A')
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\nPattern 4: Same Alphabet Per Row")
n = 4
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()

print("\nPattern 5: Reverse Alphabet Triangle")
n = 4
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + n - i - 1), end=" ")
    print()
