.. activecode::  ch6ex12q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    from turtle import *
    space = Screen()
    t = Turtle()
    t2 = Turtle()
    turtleDrawing(t, t2, 100, 45)

    turtleDrawing def(turtle, turtle2, distance, angle)
            turtle.left(angle)
            turtle2.right(angle)
            turtle.forward(turtle2)
            turtle2.forward(turtle)
            return distance