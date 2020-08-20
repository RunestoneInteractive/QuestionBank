.. activecode::  ch6ex7a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPNameNames
    :subchapter: ch6_exercises
    :topics: CSPNameNames/ch6_exercises
    :from_source: T
    :nocodelens:

    def square(turtle,size):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)


    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle screen (space)
    malik = Turtle()        # create a turtle named malik
    square(malik, 100)      # draw a square of size 100
    square(malik, 75)       # draw a square of size 75
    square(malik, 50)       # draw a square of size 50
    square(malik, 25)       # draw a square of size 25