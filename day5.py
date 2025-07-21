#day5 of 30 days python challenge 
#if else condition statement in python

a =int(input("enter your age :"))
if a>18:
    print("you can vote")
else:
    print("you can't vote")

#elfi statement in python

a1 = int(input("enter the number :"))
if a1<0 :
    print("the number is negative")
elif a1==0:
    print("the number is zero")
else :
    print("the number is positive")

#nested if-else statement

a2 = int(input("enter the number :"))
if a2<0 :
    print("the number is negative")
elif (a2>0):
    if a2<=10:
        print("the number is betweeen 1-10")
    elif(a2 > 10 and a2 <=20):
        print("the number is between 11-20")
    else:
        print("the number is greater than 20")
    
else:
    print("the number is zero")