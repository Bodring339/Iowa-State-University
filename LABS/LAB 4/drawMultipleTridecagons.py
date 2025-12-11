"""
Muhammad Muhamedjonov, 01.10.2025, 
LAB 4, code of drawing few regular tridecagons in python using turtle, functions
"""

import turtle
import math

def tridecagonTurtle(s, t):
     alfa = float(11 * 180 / 13)
     d = 180 - alfa
     f = d / 2
     t.pensize(3)
     t.speed(2) 
     t.right(f)
     t.forward(s)
     for i in range(12):
         t.right(d)
         t.forward(s)

def main():
    s = int(input("s: "))
    x = int(input("x: "))
    y = int(input("y: "))
    nr = int(input("nr: "))
    sr = int(input("sr: "))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("purple")
    r = s / (2*math.sin(math.pi/13)) * 2
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(nr):
        tridecagonTurtle(s, t)
        t.setheading(0)
        t.penup()
        t.forward(r + sr)
        t.pendown()

    wn.exitonclick()

if __name__ == "__main__":
    main()
