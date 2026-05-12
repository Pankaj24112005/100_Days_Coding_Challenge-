# Day 13: Strings in Python

# 1. String Creation
name = "Pankaj"
language = 'Python'
sentence = """Python is easy
and powerful"""

print(name)
print(language)
print(sentence)

print("-" * 40)

# 2. String Indexing
word = "Programming"
print("First character:", word[0])
print("Last character:", word[-1])

print("-" * 40)

# 3. String Slicing
print("Slice [0:6]:", word[0:6])
print("Slice [3:]:", word[3:])
print("Slice [:5]:", word[:5])
print("Reverse string:", word[::-1])

print("-" * 40)

# 4. String Methods
text = "  hello python world  "

print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Stripped text:", text.strip())
print("Replaced text:", text.replace("python", "AI"))
print("Split text:", text.split())

print("-" * 40)

# 5. String Concatenation
first = "Hello"
second = "World"
result = first + " " + second
print("Concatenated string:", result)

print("-" * 40)

# 6. String Formatting
name = "Pankaj"
age = 20

print(f"My name is {name} and I am {age} years old.")

print("-" * 40)

# 7. String Immutability
msg = "Hello"
# msg[0] = "h"  # This will cause an error
print("Strings are immutable in Python")

print("-" * 40)

# 8. Membership Operators
print("Is 'Py' in language?", "Py" in language)
print("Is 'Java' not in language?", "Java" not in language)
