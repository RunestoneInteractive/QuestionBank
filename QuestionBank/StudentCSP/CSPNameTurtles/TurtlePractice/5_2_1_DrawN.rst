.. parsonsprob:: 5_2_1_DrawN
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: TurtlePractice
   :topics: CSPNameTurtles/TurtlePractice
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.3847926267
   :total_students_attempting: 1302
   :num_students_correct: 1216.0
   :mean_clicks_to_correct: 3.3100328947

   The following program uses a turtle to draw a capital N as shown in the picture to the left of this text, <img src="../_static/DrawN4.png" width="200" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Remember that the turtle starts off facing east when it is created.  Then it should draw the lines for the N in the order shown by the numbers on the picture.  <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order. There may be some extra blocks that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   =====
   ella = Turtle()
   =====
   ella = Turtle #paired
   =====
   ella.left(90)
   ella.forward(100)
   =====
   ella.right(90)
   ella.forward(100) #paired
   =====
   ella.right(150)
   ella.forward(116)
   =====
   ella.left(150)
   ella.forward(116) #paired
   =====
   ella.left(150)
   =====
   ella.forward(100)
   =====
   ella.Forward(100) #paired