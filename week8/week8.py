import turtle
import math


# Write a function which is given an exam mark, and it returns a string — the grade for
# that mark — according to this scheme:

def gradeMarkers():

    grade : float = float(input("Enter grade: "))


    if grade < 60: return "F"
    elif grade < 70: return "D"
    elif grade < 80: return "C"
    elif grade < 90: return "B"
    elif grade < 100: return "A"
    else: return

# print(gradeMarkers())

#  Modify the turtle bar chart program from the previous chapter so that the bar for any
# value of 200 or more is filled with red, values between [100 and 200) are filled yellow,
# and bars representing values less than 100 are filled green

xy = [48,117,200,240,160,260,220,-50,100,-250]

def drawbarchart(variables,length):
    wn = turtle.Screen()
    tess = turtle.Turtle()
    wn.bgcolor("lightgreen")
    tess.color("blue")

    for i in range(len(variables)):
        charlength=length
        tess.left(90)
        if(abs(variables[i])<100): tess.fillcolor("green")
        elif(abs(variables[i])<200): tess.fillcolor("yellow")
        else: tess.fillcolor("red")


        tess.begin_fill()
        if(variables[i]<=0):

            tess.write(variables[i])
        tess.forward(variables[i])
        tess.right(90)
        if(variables[i]>=0):
            tess.write(variables[i])
        tess.forward(charlength/(len(variables)+1)) #Constant width
        tess.right(90)
        tess.forward(variables[i])
        tess.left(90)
        tess.end_fill()
    wn.exitonclick()
# drawbarchart(xy,300)

# Write a function findHypot. The function will be given the length of two sides of a
# right-angled triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5
# will return the square root, or use sqrt from the math module)

def findHypot(length1:float,length2:float):
    hypot =  math.sqrt((length1**2)+(length2**2))
    return hypot
print(findHypot(6,8))