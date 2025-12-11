"""
Muhammad Muhamedjonov, 10.15.2025, 
LAB 6, Drawing tridecagon L System, random stuff
"""

import turtle
import random
import tridecagonTurtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-TP-FT++P-PT-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'T':
            x = int(aTurtle.xcor())
            y = int(aTurtle.ycor())
            sz = max(4, int(distance * 6))
            tridecagonTurtle.tridecagonTurtle(sz, x, y, aTurtle)
        elif cmd == 'P':
            nx = random.randrange(-80, 80)
            ny = random.randrange(-80, 80)
            aTurtle.penup()
            aTurtle.goto(aTurtle.xcor() + nx, aTurtle.ycor() + ny)
            aTurtle.pendown()

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

main()
