.. parsonsprob:: 10_2_2_Triangle
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatTurtles
   :subchapter: turtleGeom
   :topics: CSPRepeatTurtles/turtleGeom
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses a turtle to draw a triangle as shown to the left, <img src="../_static/TurtleTriangle.png" width="150" align="left" hspace="10" vspace="5"/> but the lines are mixed up.  The program should do all necessary set-up and create the turtle.  After that, iterate (loop) 3 times, and each time through the loop the turtle should go forward 100 pixels, and then turn left 120 degrees.<br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order with the correct indention.  There may be additional blocks that are not needed in a correct solution.  Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   =====
   space = screen() #paired
   =====
   marie = Turtle()
   =====
   # repeat 3 times
   for i in range(3):
   =====
   # repeat 3 times
   for i in range(3) #paired
   =====
       marie.forward(100)
   =====
       marie.forward(100 #paired
   =====
       marie.left(120)
   =====
       marie.turn(120) #paired