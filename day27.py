# Day 27: Understanding == vs is

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same values)
print(a is b)   # False (different memory)
print(a is c)   # True (same object)
