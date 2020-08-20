.. parsonsprob:: 10_1_2_Rectangle
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatTurtles
   :subchapter: repeatturtles
   :topics: CSPRepeatTurtles/repeatturtles
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses a turtle to draw a rectangle as shown to the left, <img src="../_static/TurtleRect.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up and create the turtle.  After that, iterate (loop) 2 times, and each time through the loop the turtle should go forward 175 pixels, turn right 90 degrees, go forward 150 pixels, and turn right 90 degrees.<br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order with the correct indention.  There may be additional blocks that are not needed in a correct solution.   Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   from Turtle import * #paired
   =====
   space = Screen()
   carlos = Turtle()
   =====
   # repeat 2 times
   for i in [1,2]:
   =====
   # repeat 2 times
   for i in [1,2]  #paired
   =====
       carlos.forward(175)
   =====
       carlos.Forward(175) #paired
   =====
       carlos.right(90)
   =====
       carlos.forward(150)
       carlos.right(90)
   =====
       carlos.forward(150)
       carlos.turn(90) #paired