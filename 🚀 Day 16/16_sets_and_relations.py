# Day 16: Sets and Relations in Python
# Topic: Sets & Relations

# -----------------------------
# SETS IN PYTHON
# -----------------------------

# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

# Adding elements
set_a.add(10)
print("\nAfter adding 10 to Set A:", set_a)

# Removing elements
set_a.remove(2)
print("After removing 2 from Set A:", set_a)

# Set operations
print("\nUnion:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))
print("Symmetric Difference:", set_a.symmetric_difference(set_b))

# Membership test
print("\nIs 5 in Set A?", 5 in set_a)
print("Is 100 in Set B?", 100 in set_b)

# Removing duplicates using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\nOriginal List:", numbers)
print("Unique elements:", unique_numbers)


# -----------------------------
# RELATIONS IN PYTHON
# -----------------------------

# A relation is represented as a set of ordered pairs (tuples)

# Example: Relation R from A to B
A = {1, 2, 3}
B = {4, 5}

# Defining a relation
relation = {(1, 4), (2, 5), (3, 4)}

print("\nSet A:", A)
print("Set B:", B)
print("Relation R:", relation)

# Checking relation pairs
for pair in relation:
    print("Pair:", pair)

# Checking if a specific relation exists
check_pair = (2, 5)
print("\nIs (2,5) in relation?", check_pair in relation)

# Domain and Range of a relation
domain = {pair[0] for pair in relation}
range_set = {pair[1] for pair in relation}

print("Domain of Relation:", domain)
print("Range of Relation:", range_set)

print("\n--- Day 16 Completed: Sets & Relations ---")
