.. parsonsprob:: 5_1_1_Turtle_L
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: names4turtles
   :topics: CSPNameTurtles/names4turtles
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.2588300221
   :total_students_attempting: 1812
   :num_students_correct: 1568.0
   :mean_clicks_to_correct: 6.9457908163

   The following program uses a turtle to draw a capital L as shown to the left, <img src="../_static/TurtleL4.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  The turtle should turn to face south, draw a line that is 150 pixels long, then turn to face east, and draw a line that is 75 pixels long.  We have added a compass to the picture to indicate the directions north, south, west, and east. <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  There may be additional blocks that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.  </p>
   -----
   from turtle import *
   =====
   from turtle Import * #paired
   =====
   space = Screen()
   =====
   space = screen() #paired
   =====
   ella = Turtle()
   =====
   ella.right(90)
   =====
   ella.turn(90) #paired
   =====
   ella.forward(150)
   =====
   ella.left(90)
   =====
   ella.forward(75)
   =====
   ella.go(75) #paired