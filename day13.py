# day13 of 30 days python challenge 
#topic- Recursion in python

#factorial using recursion 
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} is: {factorial(num)}")