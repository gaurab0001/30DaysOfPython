#day17 of 30 days python challenge 
#Topic - Exploring exception handeling .

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
finally:
    print("Thank you for using the calculator .")
