.. activecode::  ch10ex7a
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
    marie = Turtle()

    # repeat 3 times
    for i in range(3):
        marie.forward(100)
        marie.left(120)