.. parsonsprob:: 10_4_1_turtle-stamp
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatTurtles
   :subchapter: stamp
   :topics: CSPRepeatTurtles/stamp
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0809659091
   :total_students_attempting: 704
   :num_students_correct: 638.0
   :mean_clicks_to_correct: 5.84169279

   The following program uses the stamp method to create a line of turtle shapes as shown to the left, <img src="../_static/Turtle3Stamp.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up, create the turtle, set the shape to "turtle", and pick up the pen.  Then the turtle should repeat the following three times: go forward 50 pixels and leave a copy of the turtle at the current position.  <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order with the correct indention.  Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.</p>
   -----
   from turtle import *
   space = Screen()
   space.setup(400,400)
   =====
   nikea = Turtle()
   =====
   nikea.shape("turtle")
   =====
   nikea.shape(turtle) #paired
   =====
   nikea.penup()
   =====
   nikea.penUp() #paired
   =====
   for size in range(3):
   =====
   for size in range(3)  #paired
   =====
       nikea.forward(50)
   =====
       nikea.stamp()
   =====
       nikea.stamp #paired