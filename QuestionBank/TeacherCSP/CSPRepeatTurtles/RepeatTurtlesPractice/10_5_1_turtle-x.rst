.. parsonsprob:: 10_5_1_turtle-x
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatTurtles
   :subchapter: RepeatTurtlesPractice
   :topics: CSPRepeatTurtles/RepeatTurtlesPractice
   :from_source: T
   :numbered: left
   :adaptive:

   The following program uses the stamp method to create an X of turtle shapes as shown to the left, <img src="../_static/TurtleStampX.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up, create the turtle, set the shape to "turtle", and pick up the pen. Stamp the blue turtles before you stamp the green ones.   <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order with the correct indention.  Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   =====
   space = Screen()
   =====
   space = screen() #distractor
   =====
   nick = Turtle()
   nick.shape("turtle")
   =====
   nick.penup()
   =====
   nick.penUp() #distractor
   =====
   nick.goto(-150,-150)
   nick.left(45)
   =====
   nick.goto(-150,-150)
   nick.left(90) #distractor
   =====
   nick.color("blue")
   for num in range(15):
       nick.stamp()
       nick.forward(30)
   =====
   nick.goto(150,-150)
   nick.left(90)
   =====
   nick.goto(150,-150)
   nick.left(45) #distractor
   =====
   nick.color("green")
   for num in range(14):
   =====
       nick.stamp()
       nick.forward(30)