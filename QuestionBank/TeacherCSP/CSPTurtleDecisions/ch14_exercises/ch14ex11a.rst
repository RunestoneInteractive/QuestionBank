.. activecode::  ch14ex11a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPTurtleDecisions
    :subchapter: ch14_exercises
    :topics: CSPTurtleDecisions/ch14_exercises
    :from_source: T
    :nocodelens:

    from turtle import *
    space = Screen()
    jose = Turtle()
    jose.shape("turtle")
    jose.penup()
    for size in range(10):
        if (size % 3 == 0):
            jose.color('blue')
        elif (size % 3 == 1):
            jose.color('yellow')
        else:
            jose.color('gray')
        jose.forward(50)
        jose.stamp()
        jose.forward(-50)
        jose.right(36)