.. activecode::  ch10ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    def drawStampSquare(turtle,size):
        turtle.penup()
        turtle.shape("turtle")
        for sides in range(4):      # repeat the indented lines 4 times
            turtle.forward(size)    # move forward by 100 units
            turtle.stamp()
            turtle.right(90)        # turn by 90 degrees

    from turtle import *
    space = Screen()
    carlos = Turtle()
    drawStampSquare(carlos,50)