.. activecode::  ch14ex13q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPTurtleDecisions
     :subchapter: Exercises
     :topics: CSPTurtleDecisions/Exercises
     :from_source: T
     :nocodelens:

     from turtle import *
     space = Screen()
     tess = Turtle()
     tess.shape("turtle")
     tess.penup()                  # ask tess to pick up her pen
     for size in range(5, 60, 2):  # start with size = 5 and grow by 2
         tess.stamp()                # leave an impression on the canvas
         tess.forward(size)          # move tess along
         tess.right(24)              # and turn her