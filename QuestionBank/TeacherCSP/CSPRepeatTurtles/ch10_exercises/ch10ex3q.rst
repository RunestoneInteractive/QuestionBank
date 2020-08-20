.. activecode::  ch10ex3q
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
     carlos = Turtle()

     # repeat 2 times
     for i in [1,2]:
         carlos.forward(175)
         carlos.right(90)
     carlos.forward(150)
     carlos.right(90)