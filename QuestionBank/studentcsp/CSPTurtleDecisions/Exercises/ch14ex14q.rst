.. activecode::  ch14ex14q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPTurtleDecisions
    :subchapter: Exercises
    :topics: CSPTurtleDecisions/Exercises
    :from_source: T
    :nocodelens:

    from turtle import *
    space = Screen()
    jaz = Turtle()
    mia = Turtle()
    mia.color('red')
    mia.penup()
    mia.goto(100,0)
    mia.pendown()
    mia.right(180)
    for x in range(20):
        jaz.forward(10)
        mia.forward(10)
        if (mia.xcor() + jaz.xcor() > 40):
            jaz.right(45)
            mia.right(45)