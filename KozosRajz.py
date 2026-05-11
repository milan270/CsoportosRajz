import turtle
turtle.speed(0)
i = 0

while i < 4:
    turtle.color("brown")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill()
    i += 1
i = 0

while i < 12:
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(60)
    turtle.right(30)
    turtle.end_fill()
    i+ = 1
turtle.done()
