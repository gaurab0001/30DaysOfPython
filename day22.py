#day22 of 30 days python challenge 
#Topic - practice (what i was doing last week.)

# A simple function to greet users
def greet_users(*names):
    for i, name in enumerate(names, start=1):
        print(f"{i}. Hello, {name}!")
    else:
        print("Done greeting everyone ")

# A function to show user info
def user_info(**details):
    print("User Info:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Check voting eligibility using shorthand if-else
def check_voting(age):
    return "Can Vote" if age >= 18 else "Can't Vote"

# Set to avoid duplicate names
users = {"Gaurab", "Ankit", "Gaurab"}

# Call the functions
greet_users(*users)
user_info(name="Gaurab", age=20, course="BCA")
print("Voting Status:", check_voting(20))
