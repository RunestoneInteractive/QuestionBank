.. activecode::  ch14ex9q
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
     if (mia.xcor() - jaz.xcor() < 40):
     jaz.right(45)
     mia.right(45)