.. parsonsprob:: 5_4_2_JandT
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameTurtles
   :subchapter: multTurtles
   :topics: CSPNameTurtles/multTurtles
   :from_source: T
   :numbered: left
   :adaptive:

   The following program has one turtle, "jamal", draw a capital L in blue and then another, "tina", draw a line to the west in orange as shown to the left, <img src="../_static/TwoTurtles1N.png" width="150" align="left" hspace="10" vspace="5" />.  The program should do all set-up, have "jamal" draw the L, and then have "tina" draw the line.   <br /><br /><p>Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   wn = Screen()
   =====
   jamal = Turtle()
   jamal.pensize(10)
   jamal.color("blue")
   =====
   jamal.right(90)
   jamal.forward(150)
   =====
   jamal.left(90)
   jamal.forward(150) #paired
   =====
   jamal.left(90)
   jamal.forward(75)
   =====
   jamal.right(90)
   jamal.forward(75) #paired
   =====
   tina = Turtle()
   tina.pensize(10)
   tina.color("orange")
   =====
   tina = Turtle()
   tina.pensize(10)
   tina.color(orange) #paired
   =====
   tina.left(180)
   tina.forward(75)