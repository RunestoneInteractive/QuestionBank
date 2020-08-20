.. activecode::  ch10ex13a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens

    def drawSquare(turtle,size):
        for sides in [1,2,3,4]:     # repeat the indented lines 4 times
            turtle.forward(size)    # move forward by 100 units
            turtle.right(90)        # turn by 90 degrees

    from turtle import *    # use the turtle library
    space = Screen()                # create a turtle space
    alisha = Turtle()               # create a turtle named alisha
    drawSquare(alisha,50)