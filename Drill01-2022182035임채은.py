import turtle

turtle.shape('turtle')

def pressW():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def pressS():
    turtle.setheading(-90)
    turtle.stamp()
    turtle.forward(50)

def pressA():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50) 

def pressD():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)

def esc():
     turtle.reset()       

turtle.onkey(pressW, 'w')
turtle.onkey(pressS, 's')
turtle.onkey(pressA, 'a')
turtle.onkey(pressD, 'd')
turtle.onkey(esc, 'Escape')
turtle.listen()
