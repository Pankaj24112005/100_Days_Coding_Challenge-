# Day 14 – Tuples in Python

# Creating tuples
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (10,)  # single-element tuple
tuple4 = (1, "Python", 3.14, True)

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
print("Single element tuple:", tuple3)
print("Mixed tuple:", tuple4)

# Accessing elements
print("\nAccessing elements:")
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])
print("Slicing (1:3):", tuple1[1:3])

# Nested tuple
nested_tuple = (1, 2, (3, 4, 5))
print("\nNested tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])

# Tuple immutability
print("\nTuples are immutable (cannot be changed)")
# tuple1[0] = 100  # This will raise an error

# Tuple packing and unpacking
packed_tuple = 10, 20, 30
a, b, c = packed_tuple
print("\nPacked tuple:", packed_tuple)
print("Unpacked values:", a, b, c)

# Tuple methods
numbers = (1, 2, 2, 3, 4, 2)
print("\nTuple methods:")
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))

# Tuple vs List
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("\nList:", my_list)
print("Tuple:", my_tuple)

# Use case example
coordinates = (18.5204, 73.8567)
print("\nCoordinates (latitude, longitude):", coordinates)

print("\nDay 14 Tuples practice completed ")
