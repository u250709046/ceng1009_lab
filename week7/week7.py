import turtle
import math
from operator import truediv


# 1) Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to
# and including n. So sumTo(10) would be 1+2+3...+10 which would return the value
# 55. Use the equation (n * (n + 1)) / 2.


def sumTo(n):
    return n*(n+1)/2
#print(sumTo(10))

# 2) Extend the star function to draw an n pointed star. (Hint: n must be an odd number
# greater or equal to 3).

def draw_npoint_star(n):
    tess = turtle.Turtle()
    wn = turtle.Screen()
    if n%2 ==1 and n>=3:
        for i in range(n):
            tess.forward(50)
            tess.left(180-(180/n))
            wn.exitonclick()
    else:
        print("The value of n is invalid.")

# draw_npoint_star(2)

# 3) Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and
# including n. This time use the accumulator pattern.

def sumToWithAccumulator(n):
    sum =0
    for i in range(n+1):
        sum +=i;

    return sum
# print(sumToWithAccumulator(20))

# 4) Write a function called mySqrt that will approximate the square root of a number, call
# it n, by using Newton’s algorithm. Newton’s approach is an iterative guessing
# algorithm where the initial guess is n/2 and each subsequent guess is computed
# using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).

def mySqrt(n):
    guess =n/2
    for i in range(5):
        guess = (1/2) * (guess + n/guess)

    return guess
# print(mySqrt(100))

# 5) Write a function called fancySquare that will draw a square with fancy corners
# (sprites on the corners). You should implement and use the drawSprite function from
# above. For an even more interesting look, how about adding small triangles to the
# ends of the sprite legs.

def fancysqure():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    wn.bgcolor("black")
    tess.color("white")
    tess.fillcolor("red")

    def drawtriangle():
        for i in range(3):
            tess.right(30)
            tess.forward(20)
            tess.left(150)

    def drawsprite():
        for i in range(8):
            tess.forward(15)
            tess.begin_fill()
            drawtriangle()
            tess.backward(15)
            tess.left(360/8)
            tess.end_fill()
    def drawsquare():
        for i in range(4):
            tess.forward(100)
            drawsprite()
            tess.left(90)
    drawsquare()

    wn.exitonclick()

fancysqure()

# 6) Write a function that takes a number and returns whether it is positive, negative, or
# zero.
def iswhat(n):
    if n>0:
        return "positive"
    if n<0:
        return "negative"
    else:
        return "zero"



# print(iswhat(int(input("Enter a number"))))

xy = [48,117,200,240,160,260,220]

def drawbarchart(variables,length):
    wn = turtle.Screen()
    tess = turtle.Turtle()
    wn.bgcolor("lightgreen")
    tess.color("blue")

    for i in range(len(variables)):
        charlength=length
        tess.left(90)
        tess.begin_fill()
        tess.fillcolor("red")
        tess.forward(variables[i])
        tess.right(90)
        tess.write(variables[i])
        tess.forward(charlength/(len(variables)+1)) #Constant width
        tess.right(90)
        tess.forward(variables[i])
        tess.left(90)
        tess.end_fill()
    wn.exitonclick()
# drawbarchart(xy,250)