import turtle

# Screen conditions
s = turtle.Screen()
s.bgcolor("#424141")
s.setup(width=600, height=550)
s.title("My logo")

# Drawing conditions
a = turtle.Turtle()
a.pensize(5)
a.shape("classic")

# Circle
a.penup()
a.goto(0, -160)
a.pendown()
a.begin_fill()
a.color("white")
a.circle(180, 360)
a.end_fill()
a.penup()

# I
a.pensize(3)
a.goto(-90, -100)
a.begin_fill()
a.color("black")
a.pendown()
a.pencolor("black")
a.left(90)
a.forward(240)
a.right(90)
a.forward(20)
a.right(90)
a.forward(240)
a.right(90)
a.forward(20)
a.penup()
a.end_fill()
a.right(90)

# G
a.goto(90, 75)
a.begin_fill()
a.pendown()
a.circle(50, 180)
a.forward(105)
a.circle(50, 180)
a.forward(25)
a.left(90)
a.forward(50)
a.right(90)
a.forward(20)
a.right(90)
a.forward(70)
a.right(90)
a.forward(49)
a.circle(-70, 180)
a.forward(110)
a.circle(-70, 180)
a.right(90)
a.forward(20)
a.end_fill()
a.penup()

# Black frame around logo
a.goto(0, -160)
a.pendown()
a.circle(-180, 360)

a.hideturtle()
turtle.done()