.. activecode::  ch10ex6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    from turtle import *
    space = Screen()
    mia = Turtle()
    mia.setheading(90)
    for sides in range(6):
        mia.forward(40)
        mia.right(60)