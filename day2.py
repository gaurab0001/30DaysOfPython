#day2 of 30days python challenge
#taking input and using typecasting

a = input("enter any number : ")
print("the number is " +a)

name = input("enter your name :")
age = input("enter your age : ")
print("hello",name+"now you are",age,"years old")

age=int(age)
print("in 5 years, you will be", age+5)

x = input("enter first number :")
y = input("enter second number: ")
print(x+y)    # this always return integer
print(int(x)+int(y))  # this convert string into number

pi = 3.14
print("pi as a string:",str(pi))


# checking the number if it is odd or even

number = input("Enter a number: ")
number = int(number)

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")



