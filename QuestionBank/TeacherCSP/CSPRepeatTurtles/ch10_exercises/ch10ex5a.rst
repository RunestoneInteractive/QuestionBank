.. activecode::  ch10ex5a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    from turtle import *    # use the turtle library
    space = Screen()        # create a turtle space
    will = Turtle()                 # create a turtle named will
    will.setheading(90)     # point due north
    for sides in range(5):  # repeat the indented lines 5 times
        will.forward(100)           # move forward by 100 units
        will.right(72)              # turn by 72 degrees