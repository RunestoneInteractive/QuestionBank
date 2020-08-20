.. activecode::  ch6ex9a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def square(turtle, size):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)

    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle screen
    malik = Turtle()        # create a turtle named malik
    square(malik,50)       # draw a square with malik