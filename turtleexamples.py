import turtle
import random

# from turtle import *
# color('black', 'red')
# speed(20)
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     speed(50)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


# t=turtle.Turtle()
# t.getscreen().bgcolor("#000000")
# t.color("blue","blue")
# t.speed(300)

# def draw_star (turtle_obj ,size):
#     for _ in range(5):
#         turtle_obj.forward(size)
#         turtle_obj.left(216)

# for _ in range(100):
#     x,y= random.randint(-300,300),random.randint(-300,300)

#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.begin_fill()
#     draw_star(t,random.randint(5,25))
#     t.end_fill()
# turtle.done()


# turtle.getscreen().onclick(turtle.goto)

# def draw_star(x,y):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()

#     turtle.color("black","pink")
#     turtle.begin_fill()

#     for _ in range(36):
#         turtle.forward(150)
#         turtle.left(170)

#     turtle.end_fill()

# turtle.getscreen().onclick(draw_star)
# turtle.speed(300)
# draw_star(0,0)
# turtle.done()

colors=["red","blue","orange","green","purple","yellow"]
turtle.speed(1000)
turtle.bgcolor("black")

for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(x//100+1)
    turtle.forward(x)
    turtle.left(59)

turtle.done()