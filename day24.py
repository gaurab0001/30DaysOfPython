# Day 24: My Python Intro using Class

class AboutMe:
    def __init__(self, name, age, course, goal):
        self.name = name
        self.age = age
        self.course = course
        self.goal = goal

    def intro(self):
        print(f"Hey, I'm {self.name}")
        print(f"I'm {self.age} years old and pursuing {self.course}.")
        print(f"My goal is: {self.goal}")

me = AboutMe("Gaurab Tiwary", 20, "BCA", "To become a skilled Python developer")
me.intro()
