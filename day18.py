#day18 of 30 days python challenge 
#Topic - Exploring Raising Errors(Exception Handling) .

def divide(a ,b):
    if b==0:
        raise ZeroDivisionError("Error: Division by zero is not allowed")
    return a/b
try:
    num1 = int(input("enter the 1st number:"))
    num2 = int(input("enter the 2nd number:"))
    result = divide(num1,num2)
    print("result is :",result)
except ZeroDivisionError as e:
    print("Error:",e)

