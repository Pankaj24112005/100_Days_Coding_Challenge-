# 07_file_handeling.py
# Day 7 – File Handling in Python

# 1. Writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is Day 7 of Python File Handling.\n")
file.write("Learning how to write data into files.\n")
file.close()

# 2. Reading from a file
file = open("sample.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# 3. Appending to a file
file = open("sample.txt", "a")
file.write("This line is appended to the file.\n")
file.close()

# 4. Reading file line by line
file = open("sample.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()

# 5. Using with statement (recommended way)
with open("sample_with.txt", "w") as f:
    f.write("This file is created using with statement.\n")

with open("sample_with.txt", "r") as f:
    print("Content from sample_with.txt:")
    print(f.read())

# 6. Handling file not found error
try:
    with open("not_found.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
