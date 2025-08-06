# Day 26: Using super() in Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It’s a {self.breed}.")

d = Dog("Rocky", "Labrador")
d.speak()
