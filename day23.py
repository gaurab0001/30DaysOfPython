# Day 23 of 30 Days Python Challenge
# Topic: Classes and Objects

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

# Creating an object
student1 = Student("Gaurab", 20, "BCA")
student1.show_info()

