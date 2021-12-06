"""
Program Name: TIY 7.4-7.7
Program Purpose: Input statements
Date Written:12-3-21
Programmer: Miguel Wills
"""
# 7.4 Pizza toppings

pizza = input("What type of toppings do you want?")
pizza = str(pizza)
while pizza != ('quit'):
    print("Okay, I'll add", pizza, "to your pizza")

