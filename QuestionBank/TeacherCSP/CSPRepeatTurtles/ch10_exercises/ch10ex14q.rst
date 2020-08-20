.. activecode::  ch10ex14q
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
    tess = Turtle()
    tess.color("blue")
    tess.shape("turtle")


    for size in range(5, 60, 2):

        tess.forward(size)