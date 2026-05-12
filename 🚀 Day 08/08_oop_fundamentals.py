# Day 8: Fundamentals of OOP in Python
# Topics: Class, Object, Constructor, Attributes

class Student:
    # Constructor
    def __init__(self, name, roll_no, branch):
        self.name = name        # Attribute
        self.roll_no = roll_no  # Attribute
        self.branch = branch    # Attribute

    def display_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)


# Creating objects of the class
student1 = Student("Pankaj", 101, "AI & DS")
student2 = Student("Rahul", 102, "Computer Engineering")

# Accessing object methods
student1.display_details()
print()
student2.display_details()
