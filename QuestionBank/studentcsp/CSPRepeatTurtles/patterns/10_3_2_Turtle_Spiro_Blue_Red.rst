.. parsonsprob:: 10_3_2_Turtle_Spiro_Blue_Red
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPRepeatTurtles
   :subchapter: patterns
   :topics: CSPRepeatTurtles/patterns
   :from_source: T
   :numbered: left
   :adaptive:

   There is a way of arranging the statements below such that this image is created. <img src="../_static/RedTrianglesBlueCircle.png" width="200" align="left" hspace="10" vspace="5" /> The turtle will draw many triangles. Move the needed pieces of the program from the left into the space on the right.  Indent lines as needed.
   -----
   from turtle import *
   from sys import *
   setExecutionLimit(50000)
   =====
   wn = Screen()
   mateo = Turtle()
   mateo.setheading(90)
   =====
   for repeats in range(20):
   =====
   for repeats in range(20) #distractor
   =====
       mateo.color("blue")
       mateo.forward(10)
       mateo.left(18)

   =====
       for sides in range(3):
   =====
       for sides in range(3) #distractor
   =====
           mateo.color("red")
           mateo.forward(50)
           mateo.right(120)
   =====
           mateo.color("red")
           mateo.forward(50)
           mateo.right(60) #distractor