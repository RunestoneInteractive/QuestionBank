.. activecode::  ch10ex8a
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
    hi = Turtle()

    for i in range(15):
        hi.forward(40)
        hi.left(24)