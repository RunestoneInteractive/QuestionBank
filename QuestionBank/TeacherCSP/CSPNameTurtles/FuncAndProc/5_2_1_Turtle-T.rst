.. parsonsprob:: 5_2_1_Turtle-T
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameTurtles
   :subchapter: FuncAndProc
   :topics: CSPNameTurtles/FuncAndProc
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses a turtle to draw a capital T as shown to the left, <img src="../_static/TurtleT1.png" width="150" align="left" hspace="10" vspace="5"/> but the lines are mixed up.  The program should do all necessary set-up: import the turtle module, get the space to draw on, and create the turtle.  After that the turtle should draw the lines in the numbered order as shown in the picture on the left.<br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   jamal = Turtle()
   =====
   jamal.left(90)
   =====
   jamal.Left(90) #distractor
   =====
   jamal.forward(150)
   =====
   jamal.Forward(150) #distractor
   =====
   jamal.left(90)
   jamal.forward(50)
   =====
   jamal.right(180)
   =====
   jamal.turn(180) #distractor
   =====
   jamal.forward(100)
   =====
   jamal.forward(100 #distractor