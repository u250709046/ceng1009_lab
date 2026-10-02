import math

# 1)Write a program that will compute the area of a rectangle. Prompt the user to enter
#the width and height of the rectangle. Print a nice message with the answer
from secrets import choice

#
#print("Enter de width: ")
#width = float(input())
#print("Enter de height: ")
#height = float(input())
#area = (width * height)
#print("Area of the rectangle: ", area)



#2)Write a program that will compute MPG for a car. Prompt the user to enter the
#number of miles driven and the number of gallons used. Print a nice message with
#the answer.


# print("Enter the miles driven: ")
# miles = float(input())
# print("Enter the gallons used: ")
# gallons = float(input())
# gpm = miles / gallons
# print("The gallon usage is: ", gpm)

#3)Write a program that will convert degrees fahrenheit to degrees celsius.


# degree1 = float(input("Enter the degrees: "))
#
# choice = int(input("1) fahrenheit to celcius/2) celcius to fahrenheit: "))
#
# if choice == 1:
#     degree2 = (degree1-32)* 5/9
#     print("The degree is: ",degree2," celcius")
# if choice == 2:
#     degree2 = (degree1*(9/5))+32
#     print("The degree is: ",degree2," fahrenheit")

# 4)Write a Python program that:
# Takes two inputs from the user:
# The starting day of the vacation (an integer between 0 and 6, where 0 = Sunday, 1 =
# Monday, …, 6 = Saturday).
# The length of the vacation in days (integer).
# Converts the inputs to integers.
# Adds the vacation length to the starting day.
# Uses the modulus operator % 7 to find the day of the week when the vacation ends.
# Returns the result as an integer (0–6).

# days = ["Sunday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# startingDayOfVacation= int(input("Enter the starting day of the vacation: "))
# durationofVacation = int(input("Enter the duration of vacation: "))
#
# endingofVacation = (startingDayOfVacation + durationofVacation)%7
# print("The starting day to your job is: ",days[endingofVacation])

# 5)Write a program that calculates the circumference of a circle.
# 1. Prompt the user for the radius of the circle.
# 2. Calculate the circumference using the formula.
# C=2πr.
# 3. Display the result.

# radiusOfCircle = float(input("Enter the radius of circle: "))
# circumferenceOfCircle = 2 * math.pi * radiusOfCircle
# print(f"The circumference of the circle is :{circumferenceOfCircle:.2f}")

# 6)Write a program that calculates the user's age based on their birth year.
# 1. Prompt the user for their birth year.
# 2. Calculate their age (assuming the current year is 2024).
# 3. Display their age.

# birthYear=int(input("Enter birth year: "))
#
# if(birthYear>2024):
#     print("Invalid Year")
#     exit()
# else:
#     age = 2024-birthYear
#
# print(age)













