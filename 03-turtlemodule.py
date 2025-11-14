import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

# t.rt() #instead of t.right()
# t.fd() #instead of t.forward()
# t.lt() #instead of t.left()
# t.bk() #instead of t.backward()

t.goto(50,50)

t.home()

####rectangle
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

######circle
t.circle(60)

#######dot
t.dot(20)

######BACKGROUND
turtle.bgcolor("blue")

#######title
turtle.title("My Turtle Program")

#######shapearrow
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

#####pensize
t.pensize(5)
t.forward(100)

t.shapesize(3,3,3)
t.fillcolor("red")

t.color("green", "red")

####fillshape
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

####shape
t.shape("turtle")
t.shape("arrow")
t.shape("circle")

###colorcircle
t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(90)
t.end_fill()

#####another way color circle
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()

#####paraller lines
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

t.undo()

t.clear()

t.reset()

t.stamp()
t.fd(100)
t.stamp()
t.fd(100)

####two circles
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

#####square with for
for i in range(4):
    t.fd(100)
    t.rt(90)

######while circle
n=10
while n <= 40:
    t.circle(n)
    n = n+10

#####input
n=10
while n <= 40:
    t.circle(n)
    n = n+10

u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)
else:
    print("Okay")




