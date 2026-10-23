import math
import turtle

wn = turtle.Screen()
drawer = turtle.Turtle()
drawer.speed(30)
# 1) Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which
# makes a turtle draw a regular polygon. When called with drawPoly(tess, 8, 50), it will
# draw a shape like this:

def draw_Poly(tess,sides,size):
    for i in range(sides):
        tess.forward(size)
        tess.left(360/sides)
#
# draw_Poly(drawer,8,50)
# wn.exitonclick()

# 2) Draw this pretty pattern.

def draw_pretty_pattern(alex,amount,sizes):
     for i in range(amount):
         for j in range(4):
            alex.forward(sizes)
            alex.left(90)
         alex.left(360/amount)
#draw_pretty_pattern(drawer,25,80)
# # wn.exitonclick()

# The two spirals in this picture differ only by the turn angle.Drawboth.

def spiral(alex,amount,sizes,angle):
    for i in range(amount*4):
        alex.forward(sizes*i)
        alex.right(angle)

# spiral(drawer,20,3,89)
# wn.exitonclick()

# 4) Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls
# drawPoly from the previous question to have its turtle draw a equilateral triangle

def drawEquitriangle(alex,size):
    draw_Poly(alex,3,size)

# drawEquitriangle(drawer,50)

def draw_star(alex,size):
    for i in range(5):
        drawer.left(144)
        drawer.forward(size)

def draw_fivestar(alex,size):
    for i in range(5):
        draw_star(drawer, 60)
        drawer.penup()
        drawer.forward()
        drawer.right(144)
        drawer.pendown()

#draw_fivestar(drawer,60)

# 6) Write a function called drawSprite that will draw a sprite. The function will need
# parameters for the turtle, the number of legs, and the length of the legs. Invoke the
# function to create a sprite with 15 legs of length 120

def drawSprite(alex,numOfLegs,sizeOfLegs):
    for i in range(numOfLegs):
        alex.dot(20)
        alex.forward(sizeOfLegs)
        alex.dot(20)
        alex.backward(sizeOfLegs)
        alex.left(360/numOfLegs)


drawSprite(drawer,10,100)


wn.exitonclick()