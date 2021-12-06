"""
Program Name: TIY 7.1-7.3
Program Purpose: Input statments
Date Written:12-3-21
Programmer: Miguel Wills
"""
car = input("What type of car do you want?")
car = str(car)
print("Let me see if I can find you a", car)


# This is now 7.2 code

Guest_amount = input("How many people are in your group?")
Guest_amount = int(Guest_amount)

if Guest_amount > 8 :
    print(f"\nYou will have to wait for a table to be ready.")
elif Guest_amount > 0:
    print(f"\nThe table is ready.")

number = input("Enter a number, and I'll tell you if it's a multiple of 10 or not: ")
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} is divisible by 10.")
else:
    print(f"\nThe number {number} isn't.")
