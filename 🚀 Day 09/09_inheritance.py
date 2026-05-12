# Day 9 - Object Oriented Programming
# Topic: Inheritance and Types of Inheritance

# ----------------------------
# 1. Single Inheritance
# ----------------------------
class Parent:
    def show_parent(self):
        print("This is the Parent class")


class Child(Parent):
    def show_child(self):
        print("This is the Child class")


obj1 = Child()
obj1.show_parent()
obj1.show_child()


# ----------------------------
# 2. Multiple Inheritance
# ----------------------------
class Father:
    def father_skill(self):
        print("Father's skill")


class Mother:
    def mother_skill(self):
        print("Mother's skill")


class Son(Father, Mother):
    def son_skill(self):
        print("Son's own skill")


obj2 = Son()
obj2.father_skill()
obj2.mother_skill()
obj2.son_skill()


# ----------------------------
# 3. Multilevel Inheritance
# ----------------------------
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")


class ParentLevel(Grandparent):
    def show_parent(self):
        print("Parent class")


class ChildLevel(ParentLevel):
    def show_child(self):
        print("Child class")


obj3 = ChildLevel()
obj3.show_grandparent()
obj3.show_parent()
obj3.show_child()


# ----------------------------
# 4. Hierarchical Inheritance
# ----------------------------
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog = Dog()
dog.speak()
dog.bark()

cat = Cat()
cat.speak()
cat.meow()


# ----------------------------
# 5. Hybrid Inheritance
# ----------------------------
class A:
    def method_a(self):
        print("Class A method")


class B(A):
    def method_b(self):
        print("Class B method")


class C(A):
    def method_c(self):
        print("Class C method")


class D(B, C):
    def method_d(self):
        print("Class D method")


obj4 = D()
obj4.method_a()
obj4.method_b()
obj4.method_c()
obj4.method_d()
