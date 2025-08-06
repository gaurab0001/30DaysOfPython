#day19 of 30 days python challenge 
#Topic -  Minimal KBC Game

print("Welcome to Kaun Banega Crorepati!\n")

questions = [
    ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1],
    ["Red Planet is?", "Jupiter", "Mars", "Venus", "Saturn", 2],
    ["Who painted the Mona Lisa?", "Leonardo", "Picasso", "Van Gogh", "M.F. Hussain", 1]
]

prize = [1000, 5000, 10000]
total = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQ{i+1}. {q[0]}")
    print(f"1. {q[1]}  2. {q[2]}  3. {q[3]}  4. {q[4]}")
    
    ans = int(input("Enter your answer (1-4): "))

    if ans == q[5]:
        print(" Correct!")
        total += prize[i]
    else:
        print(" Wrong! Game Over.")
        break

print(f"\nYou won ₹{total} in total. Thanks for playing!")
