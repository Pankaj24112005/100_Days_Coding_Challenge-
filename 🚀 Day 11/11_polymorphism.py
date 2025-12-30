# Day 11: Polymorphism in Python

# Polymorphism with functions
print("=== Function Polymorphism ===")

def add(a, b, c=0):
    return a + b + c

print(add(2, 3))
print(add(2, 3, 4))


# Polymorphism with classes (Method Overriding)
print("\n=== Method Overriding ===")

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()


# Polymorphism with built-in functions
print("\n=== Built-in Function Polymorphism ===")

print(len("Python"))
print(len([1, 2, 3, 4, 5]))


# Polymorphism with operators
print("\n=== Operator Polymorphism ===")

print(10 + 5)
print("Hello " + "World")
print([1, 2] + [3, 4])
