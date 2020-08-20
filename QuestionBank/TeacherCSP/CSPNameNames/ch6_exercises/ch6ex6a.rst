.. activecode::  ch6ex6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def move(turtle, distance, angle):
        turtle.forward(distance)
        turtle.right(angle)
        turtle.forward(distance)
        turtle.right(angle)
        turtle.forward(distance)
        turtle.right(angle)
        turtle.forward(distance)
        turtle.right(angle)

    from turtle import *
    space = Screen()
    t = Turtle()
    move(t, 100, 90)