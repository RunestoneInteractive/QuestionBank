.. parsonsprob:: 10_3_1_Turtle_Spiro
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatTurtles
   :subchapter: patterns
   :topics: CSPRepeatTurtles/patterns
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.1826923077
   :total_students_attempting: 728
   :num_students_correct: 664.0
   :mean_clicks_to_correct: 5.2063253012

   There is a way of arranging the statements below such that this image is created. <img src="../_static/BlueTrianglesRedCircle.png" width="200" align="left" hspace="10" vspace="5" /> The turtle will draw many triangles.  Move the needed pieces of the program from the left into the space on the right.  Indent lines as needed.
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
       mateo.color("red")
       mateo.forward(10)
       mateo.left(18)
   =====
       mateo.color("red")
       mateo.forward(10)
       mateo.left(12) #distractor
   =====
       for sides in range(3):
       =====
       for sides in range(4): #distractor
   =====
           mateo.color("blue")
           mateo.forward(50)
           mateo.right(120)