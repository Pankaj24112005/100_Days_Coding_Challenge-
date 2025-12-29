# 🚀 Day 6/100 – Lists & List Comprehensions in Python 🧠🐍

# -------------------------------
# 1. Creating Lists
# -------------------------------
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "mango"]

print("Numbers:", numbers)
print("Fruits:", fruits)


# -------------------------------
# 2. Accessing List Elements
# -------------------------------
print("First number:", numbers[0])
print("Last fruit:", fruits[-1])


# -------------------------------
# 3. List Operations
# -------------------------------
# append()
numbers.append(6)
print("After append:", numbers)

# insert()
numbers.insert(2, 99)
print("After insert:", numbers)

# remove()
numbers.remove(99)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)


# -------------------------------
# 4. Iterating Through a List
# -------------------------------
print("Iterating through numbers:")
for num in numbers:
    print(num)


# -------------------------------
# 5. List Slicing
# -------------------------------
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])


# -------------------------------
# 6. Nested Lists
# -------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Nested list (matrix):", matrix)
print("Element at row 2, column 3:", matrix[1][2])


# -------------------------------
# 7. List Comprehensions
# -------------------------------

# Squares of numbers
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# Even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Convert strings to uppercase
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)

# Filter numbers greater than 3
filtered_numbers = [x for x in numbers if x > 3]
print("Filtered numbers (>3):", filtered_numbers)


# -------------------------------
# End of Day 6
# -------------------------------
print("✅ Day 6 completed: Lists & List Comprehensions")
