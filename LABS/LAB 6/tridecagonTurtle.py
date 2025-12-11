"""
Muhammad Muhamedjonov, 09.23.2025, 
LAB 3, code of drawing regular tridecagon in python using turtle, functions
URL: https://en.wikipedia.org/wiki/Tridecagon
Author: N/A
Date posted: N/A (Page was last edited on 21 September 2025, at 05:43 (UTC))
"""

import turtle

def tridecagonTurtle(s, x, y, t):
     alfa = float(11 * 180 / 13)
     d = 180 - alfa
     f = d / 2
     t.pensize(1)
     t.speed(2) 
     t.penup()
     t.goto(x, y)
     t.pendown()
     t.right(f)
     t.forward(s)
     for i in range(12):
         t.right(d)
         t.forward(s)

def main():
    s = int(input("s: "))
    x = int(input("x: "))
    y = int(input("y: "))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("purple")
    tridecagonTurtle(s, x, y, t)
    wn.exitonclick()

if __name__ == "__main__":
    main()
