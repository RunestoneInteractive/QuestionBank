.. activecode::  ch10ex11a
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
    jose = Turtle()
    jose.shape("turtle")
    jose.penup()
    for size in range(10):
        jose.forward(50)
        jose.stamp()
        jose.forward(-50)
        jose.right(36)