.. activecode::  ch14ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPTurtleDecisions
    :subchapter: ch14_exercises
    :topics: CSPTurtleDecisions/ch14_exercises
    :from_source: T
    :nocodelens:

    def turtleLoop(jaz,mia):
        for x in range(20):
            jaz.forward(10)
            mia.forward(10)
            if (mia.xcor() - jaz.xcor() < 30):
                jaz.backward(50)
                mia.backward(50)
                jaz.right(45)
                mia.left(45)

    def turtleDraw(jaz, mia):
        jaz.shape('turtle')
        mia.shape('turtle')
        mia.color('red')
        mia.penup()
        mia.goto(100,0)
        mia.pendown()
        mia.right(180)
        turtleLoop(jaz,mia)

    from turtle import *
    space = Screen()
    jaz = Turtle()
    mia = Turtle()
    turtleDraw(jaz,mia)