#day10 - 30 days python challenge 
#topicc- revice that i learn last 9 days

name = input("enter your name :")
age = int(input("enter yout age :"))

def check_age(name,age):
    if age < 18 :
        print(f"{name},you are minor.")
    else:
        print(f"{name}, you ar major.")

check_age(name,age)
  

day = int(input("enter the day:"))

match day:
    case 1: 
        print("💥 Monday - Chest Day ")
    case 2:
        print("💪 Tuesday - Back Day ")
    case 3:
        print("🔥 Wednesday - Cardio + Core ")
    case 4:
        print("🏋️ Thursday - Shoulders & Traps ")
    case 5:
        print("⚡ Friday - Arms (Biceps & Triceps) ")
    case 6:
        print("🦵 Saturday - Leg Day + Stretching ")
    case 7:
        print("😌 Sunday - Rest & Recovery ")
    case _:
        print("❌ Invalid day number. Choose between 1-7")
  

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

def add(a,b):
    return a+b
def sub(a,b):  
    return a-b
def mul(a,b):
    return a*b

print(f"addition{add(num1,num2)}")
print(f"subtraction{sub(num1,num2)}")   
print(f"multiplication{mul(num1,num2)}")