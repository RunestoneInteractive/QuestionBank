.. activecode::  ch10ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatTurtles
    :subchapter: ch10_exercises
    :topics: CSPRepeatTurtles/ch10_exercises
    :from_source: T
    :nocodelens:

    from turtle import *
    from sys import *               # use the system library
    setExecutionLimit(50000)        #let this take up to 50 seconds
    space = Screen()
    zoe = Turtle()
    zoe.setheading(90)
    zoe.penup()

    for repeats in range(20):
        zoe.stamp()
        zoe.forward(10)
        zoe.right(18)
        for sides in range(4):
          zoe.stamp()
          zoe.forward(50)
          zoe.right(90)