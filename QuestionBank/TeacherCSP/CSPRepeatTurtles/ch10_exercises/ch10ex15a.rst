.. activecode::  ch10ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    def drawRectangle(turtle,length,width):
        for i in [1,2]:
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)

    from turtle import *
    space = Screen()
    carlos = Turtle()
    drawRectangle(carlos,50,100)