.. activecode::  ams_assign6_q3
    :author: Allison Schullo
    :difficulty: 0.0
    :basecourse: StudentCSP
    :chapter: CSPNameNames
    :subchapter: Exercises
    :topics: CSPNameNames/Exercises
    :from_source: F
    :nocodelens:

    Change the code to take 3 parameters, a turtle, a size that tells it how far to go, and an angle it tells the turtle to turn.
    ~~~~
    def move(turtle):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    from turtle import *
    space = Screen()
    t = Turtle()
    move(t, 100, 90)