# Day 9 - Functions in Python

def welcome(name):
    print(f"Welcome to Python, {name}!")

welcome("Gaurab")

def intro(name, age):
    return f"Hi {name}, you are {age} years old!"

print(intro("Gaurab", 20))

# Write a function that checks if a number is even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(5))

