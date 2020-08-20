.. activecode::  ch10ex10a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    def square(aTurtle):
        for sides in range(4):
            aTurtle.forward(100)
            aTurtle.right(90)

    from turtle import *
    space = Screen()
    t = Turtle()

    square(t)
    t.left(90)
    t.forward(50)
    square(t)