.. parsonsprob:: turtle-spiral-Parsons-adp
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatTurtles
   :subchapter: Exercises
   :topics: CSPRepeatTurtles/Exercises
   :from_source: F
   :numbered: left
   :adaptive:

   Put the code in order to draw a spiral of 'blue' turtle shapes without any lines between them.  Use a range that starts at 5 and ends before 60 and increments by 2 each time through the loop.  In the loop stamp the 'turtle' shape, go forward an increasing amount each time, and turn right 24 degrees. 
   -----
   from turtle import *   
   =====
   space = Screen()
   tess = Turtle()
   =====
   tess.color('blue')
   tess.shape("turtle")
   tess.penup()
   =====
   tess.color('blue')
   tess.shape("turtle")
   tess.penUp() #paired
   =====
   for num in range(5, 60, 2):
   =====
   for num in range(5, 60, 2) #paired
   =====
       tess.stamp()
   =====
       tess.stamp #paired
   =====
       tess.forward(num)
   =====
       tess.forward(100) #paired
   =====
       tess.right(24)