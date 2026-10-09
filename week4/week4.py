import turtle
# 1) Write a program that prints “We like Python's turtles!” 100 times.

# for i in range(100):
#     print("We like Python's turtles")


# 2)Write a program that uses a for loop to print
# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March
# etc

# months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# for i in months:
#     print("One of the months of the year is ",i)

# 3)Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
# a)Write a loop that prints each of the numbers on a new line.
# b)Write a loop that prints each number and its square on a new line.

# listOfNumbers = [12,10,32,3,66,17,42,99,28]
# print("List of numbers: ")
# for number in listOfNumbers:
#     print("Number is: ",number)
# print("\n")
# print("List of squares of numbers:")
# for number in listOfNumbers:
#     print("The number is: ",number,"Square of this number is: ",number**2)
#

# 4) Use for loops to make a turtle draw these regular polygons (regular means all sides the
# same lengths, all angles the same):
# -An equilateral triangle
# -A square
# -A hexagon (six sides)
# -An octagon (eight sides)

#def newLocation(x,y):
    # drawer.penup()
    # drawer.goto(x, y)
    # drawer.pendown()

#wn = turtle.Screen()
#drawer = turtle.Turtle()
#
# Equilateral Triangle
# for i in range(3):
#     drawer.forward(60)
#     drawer.left(120)
#
# newLocation(-40,0)
#
# #Square
# for i in range(4):
#     drawer.left(90)
#     drawer.forward(60)
#
# newLocation(-150,0)
#
# #Hexagon
# for i in range(6):
#     drawer.left(60)
#     drawer.forward(60)
#
# newLocation(-300,0)
# #Octagon
# for i in range(8):
#     drawer.left(45)
#     drawer.forward(60)
#
# wn.exitonclick()

# 5) Write a program that asks the user for the number of sides, the length of the side, the
# color, and the fill color of a regular polygon. The program should draw the polygon and then
# fill it in.
#
#
# sides=int(input("Enter the number of sides: "))
# lengthOfSides=int(input("Enter the length of the sides: "))
#
# wn = turtle.Screen()

# drawer.fillcolor("green")
# drawer.begin_fill()
# for i in range(sides):
#
#     drawer.left(360/sides)
#     drawer.forward(lengthOfSides)
# drawer.end_fill()
# wn.exitonclick()

# 6) A drunk pirate makes a random turn and then takes 100 steps forward, makes another
# random turn, takes another 100 steps, turns another random amount, etc. A social science
# student records the angle of each turn before the next 100 steps are taken. Her experimental
# data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print
# the current heading.
# wn = turtle.Screen()

# listOfData =[160, -43, 270, -97, -43, 200, -940, 17, -86]
# for i in range(9):
#     drawer.left(listOfData[i]%360)
#     drawer.forward(100)
# wn.exitonclick()

# wn = turtle.Screen()
# wn.bgcolor("black")
# drawer.color("white")
# for i in range(5):
#     drawer.forward(100)
#     drawer.right(144)
#
# # wn.exitonclick()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# drawer.color("blue")
#
# drawer.shape("turtle")
# drawer.stamp()
#
# drawer.penup()
#
# def stamper():
#     drawer.forward(80)
#     drawer.shape("classic")
#     drawer.pendown()
#     drawer.pensize(4)
#     drawer.forward(10)
#     drawer.penup()
#     drawer.forward(20)
#     drawer.shape("turtle")
#     drawer.stamp()
#     drawer.backward(110)
#     drawer.left(30)
#
# for i in range(12):
#     stamper()
#
# wn.exitonclick()

# 9) A sprite is a simple spider shaped thing with n legs coming out from a center point. The
# angle between each leg is 360 / n degrees.
# Write a program to draw a sprite where the number of legs is provided by the user.


# def drawLegs(lengcount):
#     for i in range(lengcount):
#         drawer.left(360/lengcount)
#         drawer.penup()
#         drawer.forward(60)
#         drawer.pendown()
#         drawer.forward(60)
#         drawer.backward(60)
#         drawer.penup()
#         drawer.backward(60)
#         drawer.pendown()
#
# legCount=int(input("enter the number of legs: "))
# drawer = turtle.Turtle()
# wn=turtle.Screen()
# wn.bgcolor("gray")
#
#
#
# drawer.color("white")
# drawer.fillcolor("black")
# drawer.begin_fill()
# drawer.circle(60)
# drawer.penup()
# drawer.end_fill()
# drawer.goto(0,60)
# drawLegs(legCount)
#
#
#
# wn.exitonclick()


