import colorgram
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)
import random



# def get_colors(file,num_colors):
#     lists = colorgram.extract(file,num_colors)
#     colors = []
#     for color in lists:
#         colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#     return colors

colors = [ (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15)]


timmy = Turtle()
timmy.penup()
timmy.pensize(15)
timmy.speed(0)
timmy.hideturtle()
timmy.setx(-200)
timmy.sety(-200)




def draw_dot():
    timmy.pendown()
    org_heading = timmy.heading()
    timmy.color(random.choice(colors))
    for i in range(360//15):
        timmy.circle(1)
        timmy.setheading(timmy.heading()+14)

    timmy.setheading(org_heading)
    timmy.penup()

def draw_dot_line(dots):
    for i in range(dots):
        draw_dot()
        timmy.forward(45)

def draw_dotbox(rows, dots):

    x = timmy.xcor()
    for i in range(rows):
        draw_dot_line(dots)
        timmy.setx(x)
        timmy.sety(timmy.ycor()+45)

draw_dotbox(11,11)

screen = Screen()
screen.exitonclick()
