# Day 9 of 30DaysOfPython
# Topic: Function with parameter + f-string + if-else

def greet_user(name, hour):
    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    print(f"{greeting}, {name}! Hope you're doing well.")

# User input
name = input("Enter your name: ")
hour = int(input("Enter the hour (0 to 23): "))

greet_user(name, hour)

