.. activecode::  ch6ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def triangle(turtle, size):
        turtle.left(60)
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)

    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle screen
    malik = Turtle()        # create a turtle named malik
    triangle(malik, 100)    # draw a triangle with malik