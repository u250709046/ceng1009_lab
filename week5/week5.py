import random
import turtle
import math

# 1) Use a for statement to print 10 random numbers


# for i in range(10):
#     print(random.random())

# 2) Repeat the above exercise but this time print 10 random numbers between 25 and
# 35, inclusive.
#
# for i in range(10):
#     print(random.randint(25,35))

# 3) The Pythagorean Theorem tells us that the length of the hypotenuse of a right
# triangle is related to the lengths of the other two sides. Look through the “math”
# module and see if you can find a function that will compute this relationship for you.
# Once you find it, write a short program to try it out

# lenght1 = 6
# lenght2 = 8
# hypotenus = math.hypot(lenght1, lenght2)
# print(hypotenus)

# 4) Write a function areaOfCircle(r) which returns the area of a circle of radius r. Make
# sure you use the math module in your solution

# def areaOfCircle(radius:int):
#     area = math.pi * (radius ** 2)
#     print("Area of the circle with radius:",radius,"is: ", area)
#
# areaOfCircle(5)

# 5) Write a non-fruitful function to draw a five pointed star, where the length of each side
# is 100 units.

# def draw_Star():
#     dr = turtle.Turtle()
#     wn = turtle.Screen()
#     wn.bgcolor("black")
#     dr.color("white")
#     dr.pensize(5)
#
#     for i in range(5):
#         dr.forward(100)
#         dr.right(144)
#
#     wn.exitonclick()
#
#
# draw_Star()


# 6) Use the drawsquare function we wrote in this chapter in a program to draw the image
# shown below. Assume each side is 20 units. (Hint: notice that the turtle has already
# moved away from the ending point of the last square when the program ends.)
dr = turtle.Turtle()
wn = turtle.Screen()
def draw_Square(sides,x,y):

    wn.bgcolor("lightgreen")

    dr.color("hotpink")

    dr.penup()
    dr.goto(x,y)
    dr.pendown()

    for i in range(4):
        dr.forward(sides)
        dr.left(90)

# draw_Square()


# 7) Use the drawsquare function we wrote in this chapter in a program to draw the image
# shown below. Assume each side is 20 units. (Hint: notice that the turtle has already
# moved away from the ending point of the last square when the program ends.

for i in range(1,5):
    draw_Square(20*i,-10*i,-10*i)

wn.exitonclick()