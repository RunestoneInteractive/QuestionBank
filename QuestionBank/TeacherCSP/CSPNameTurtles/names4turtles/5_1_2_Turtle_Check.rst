.. parsonsprob:: 5_1_2_Turtle_Check
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameTurtles
   :subchapter: names4turtles
   :topics: CSPNameTurtles/names4turtles
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses a turtle to draw a checkmark as shown to the left, <img src="../_static/checkMark.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  The turtle should turn to face southeast, draw a line that is 75 pixels long, then turn to face northeast, and draw a line that is 150 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east.  Northeast is between north and east. Southeast is between south and east. <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  There may be additional blocks that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.  </p>
   -----
   from turtle import *
   =====
   space = Screen()
   =====
   maria = Turtle()
   =====
   maria = Turtle #paired
   =====
   maria.right(45)
   =====
   maria.left(45) #paired
   =====
   maria.forward(75)
   =====
   maria.Forward(75) #paired
   =====
   maria.left(90)
   =====
   maria.right(90) #paired
   =====
   maria.forward(150)