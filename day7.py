#day7 of 30days python challenge
#match case statement in python

a = int(input("enter the number:"))
match a:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

#ry using match-case with strings like "yes", "no", etc.

answer = input("will you going collage tomorrow?")

match answer:
    case "yes":
        print("Okay, let's meet at college tomorrow.")
    case "maybe":
        print("I'll wait for your confirmation.")   
    case "no":
        print("Let’s meet the day after tomorrow at college.")    
