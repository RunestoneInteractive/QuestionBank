.. parsonsprob:: 5_2_1_DrawZ
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameTurtles
   :subchapter: TurtlePractice
   :topics: CSPNameTurtles/TurtlePractice
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses a turtle to draw a capital Z as shown in the picture to the left of this text, <img src="../_static/DrawZ.png" width="200" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  Then it should draw the lines for the Z in the order shown by the numbers on the picture.  <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  There may be extra blocks that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   from turtle Import * #paired
   =====
   space = Screen()
   =====
   space = screen() #paired
   =====
   alex = Turtle()
   =====
   alex = turtle() #paired
   =====
   alex.forward(50)
   alex.right(120)
   =====
   alex.forward(50)
   alex.turn(120) #paired
   =====
   alex.forward(100)
   =====
   alex.left(120)
   =====
   alex.forward(50)