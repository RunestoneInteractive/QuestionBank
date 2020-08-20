.. activecode::  ch10ex4a
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
    liz = Turtle()
    liz.setheading(90)
    for sides in range(8):
        liz.forward(50)
        liz.right(45)