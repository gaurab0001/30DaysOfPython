# Day 15 of 30 Days Python Challenge
# Topic: Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Gaurab",
    "age": 20,
    "course": "BCA",
    "semester": 4
}

print("Name:", student["name"])

# Adding and updating values
student["age"] = 21
student["language"] = "Python"

# Removing a key-value pair
student.pop("semester")

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
