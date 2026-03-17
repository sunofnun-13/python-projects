# inputs
name = input("What is your name? ")
age = int(input("What is your age? "))

# if and else statement 
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# this code is a variation of the previous if-else code. It includes an additional condition to check if the age is between 13 and 17, which classifies the user as a teenager. If the age is 18 or above, it classifies the user as an adult, and if it's below 13, it classifies them as a child.
