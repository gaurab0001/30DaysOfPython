# Day 25: Inheritance and Method Overriding

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

r = Rectangle(5, 3)
c = Circle(4)

print("Rectangle area:", r.area())  # 15
print("Circle area:", c.area())     # 50.24
