#Natisha Blossom
#July 8, 2025
#P4LAB1b
#Creating initials with python turtle program

import turtle

turtle.shape("turtle")

#Draw first initial
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.pensize(width=3)
turtle.pencolor("blue")
turtle.setheading(90)
turtle.forward(150)
turtle.setheading(-45)
turtle.goto(-100,0)
turtle.setheading(90)
turtle.goto(-100,150)

#Draw second initial
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)
turtle.pendown()
turtle.pensize(width=3)
turtle.pencolor("red")
turtle.forward(150)

turtle.penup()
turtle.goto(0,150)
turtle.setheading(0)
turtle.pendown()
turtle.circle(-40,180)

turtle.penup()
turtle.goto(0,75)
turtle.setheading(0)
turtle.pendown()
turtle.circle(-40,180)
