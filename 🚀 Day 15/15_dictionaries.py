# Day 15: Dictionaries in Python

# 1. Creating a dictionary
student = {
    "name": "Pankaj",
    "age": 21,
    "course": "AI & Data Science"
}
print("Student Dictionary:", student)

# 2. Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# 3. Adding a new key-value pair
student["college"] = "Engineering College"
print("After adding college:", student)

# 4. Updating an existing value
student["age"] = 22
print("After updating age:", student)

# 5. Removing elements
student.pop("course")
print("After removing course:", student)

# 6. Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 7. Iterating through a dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# 8. Nested dictionary
students = {
    101: {"name": "Amit", "marks": 85},
    102: {"name": "Riya", "marks": 92},
    103: {"name": "Suresh", "marks": 78}
}

print("\nNested Dictionary:")
for roll, info in students.items():
    print("Roll No:", roll)
    for key, value in info.items():
        print(f"  {key}: {value}")

# 9. Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary Comprehension:", squares)

# 10. Checking key existence
if "name" in student:
    print("\nKey 'name' exists in student dictionary")

print("\nDay 15 Dictionary practice completed ")
