.. activecode::  ch6ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def coloredSquare(turtle, distance, angle, color1, color2, color3, color4):
            turtle.color(color1)
            turtle.forward(distance)
            turtle.left(angle)
            turtle.color(color2)
            turtle.forward(distance)
            turtle.left(angle)
            turtle.color(color3)
            turtle.forward(distance)
            turtle.left(angle)
            turtle.color(color4)
            turtle.forward(distance)

    from turtle import *
    space = Screen()
    t = Turtle()
    coloredSquare(t, 100, 90, "blue", "red", "green", "yellow")