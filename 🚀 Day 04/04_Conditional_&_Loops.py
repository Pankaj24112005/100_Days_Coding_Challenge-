# Conditional Statements

age = 20

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# if-elif-else example

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# for loop example

print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# while loop example

count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# break example

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# continue example

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# pass example

for i in range(3):
    pass

print("Program executed successfully")

