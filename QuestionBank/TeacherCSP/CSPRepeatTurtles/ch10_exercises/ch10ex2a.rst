.. activecode::  ch10ex2a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    from turtle import *      # use the turtle library
    space = Screen()          # create a turtle space
    alisha = Turtle()         # create a turtle named alisha
    alisha.setheading(90)     # point due north
    for sides in [1,2,3]:     # repeat the indented lines 3 times
        alisha.forward(100)
        alisha.right(120)