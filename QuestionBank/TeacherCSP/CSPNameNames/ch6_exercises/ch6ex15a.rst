.. activecode::  ch6ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def rectangle(turtle, width, height):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)

    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle screen
    malik = Turtle()        # create a turtle named malik
    rectangle(malik, 100, 80)    # draw a rectangle with malik