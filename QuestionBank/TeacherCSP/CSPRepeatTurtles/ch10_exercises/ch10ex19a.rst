.. activecode::  ch10ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    def drawPolygon(turtle,numSides):
        angle = 360 / numSides
        for x in range(numSides):
            turtle.forward(25)
            turtle.right(angle)

    from turtle import *
    space = Screen()
    carlos = Turtle()
    drawPolygon(carlos,7)
    carlos.forward(100)
    drawPolygon(carlos,9)