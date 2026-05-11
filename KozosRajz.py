#milan: fa lomb
#lorant fa torzs hatter
import turtle

i = 0



turtle.speed(0)



turtle.begin_fill()
while i < 4:
    turtle.color("brown")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    i += 1

    turtle.end_fill()


turtle.done()
