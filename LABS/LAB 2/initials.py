import turtle

wn = turtle.Screen()
wn.bgcolor("red")
alex = turtle.Turtle()


alex.pensize(6)
alex.speed(2) 

alex.penup()
alex.goto(-100, 0)
alex.pendown()

alex.left(90)   
alex.forward(70)
alex.right(135)   
alex.forward(40)   
alex.left(90)   
alex.forward(40)  
alex.right(135)
alex.forward(70)

alex.penup()
alex.setheading(0)
alex.forward(60)
alex.pendown()

alex.pensize(6)
alex.speed(2) 

alex.left(90)   
alex.forward(70)
alex.right(135)   
alex.forward(40)   
alex.left(90)   
alex.forward(40)  
alex.right(135)
alex.forward(70)

wn.exitonclick()