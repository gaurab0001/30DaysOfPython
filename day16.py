#day16 of 30 days python challenge 
#Topic - using "else" statement with for loop and while loop.

#  FOR LOOP: Searching an item in a list
items = ["laptop", "keyboard", "mouse", "charger", "bottle"]
search_item = "phone"

for item in items:
    print(f"Checking: {item}")
    if item == search_item:
        print("Item found!")
        break
else:
    print("Item not found in the list.\n")

# WHILE LOOP: Simulating login attempts
correct_password = "gaurab123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print(" Login successful!")
        break
    else:
        print(" Incorrect password.")
        attempts += 1
else:
    print(" Account locked due to too many failed attempts.")