# Day 05: Functions and Lambda Functions
# 100 Days of Coding Challenge
# Topic: Functions in Python

# --------------------------------------------------
# 1. Simple function without parameters
def greet():
    print("Welcome to Python Functions!")

greet()

# --------------------------------------------------
# 2. Function with parameters
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)

# --------------------------------------------------
# 3. Function with return value
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication Result:", result)

# --------------------------------------------------
# 4. Function to check even or odd
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number 7 is:", is_even(7))

# --------------------------------------------------
# 5. Lambda function (single argument)
square = lambda x: x * x
print("Square of 6:", square(6))

# --------------------------------------------------
# 6. Lambda function (multiple arguments)
sum_lambda = lambda a, b: a + b
print("Lambda Sum:", sum_lambda(15, 25))

# --------------------------------------------------
# 7. Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)

# --------------------------------------------------
# 8. Lambda with filter()
nums = [5, 10, 15, 20, 25]
greater_than_10 = list(filter(lambda x: x > 10, nums))
print("Numbers greater than 10:", greater_than_10)

# --------------------------------------------------
# End of Day 05
print("Day 05 completed successfully!")
