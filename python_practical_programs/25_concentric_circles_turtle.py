import turtle

screen = turtle.Screen()
screen.title("Concentric Circles")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)

for radius in range(30, 181, 30):
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)

pen.hideturtle()
screen.mainloop()
