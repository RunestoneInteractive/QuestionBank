.. activecode::  ch6ex6q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPNameNames
    :subchapter: Exercises
    :topics: CSPNameNames/Exercises
    :from_source: T
    :nocodelens:

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