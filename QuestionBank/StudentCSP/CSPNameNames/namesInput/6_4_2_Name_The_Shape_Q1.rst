.. mchoice:: 6_4_2_Name_The_Shape_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: namesInput
   :topics: CSPNameNames/namesInput
   :from_source: T
   :practice: T
   :answer_a: square
   :answer_b: rectangle
   :answer_c: triangle
   :correct: b
   :feedback_a: Check the 2nd and 4th forwards.  How much do they move forward by?
   :feedback_b: This will draw a rectangle with two sides with the specified size and two sides half that size.  Copy this code into the area above and run it.
   :feedback_c: A triangle has 3 sides.
   :pct_on_first: 0.8008213552
   :total_students_attempting: 1461
   :num_students_correct: 1457.0
   :mean_clicks_to_correct: 1.245024022

   What shape would the following code draw?
   
   ::
   
     def mystery(turtle,size):
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size / 2)
         turtle.right(90)
         turtle.forward(size)
         turtle.right(90)
         turtle.forward(size / 2)
         turtle.right(90)
   
     from turtle import *       # use the turtle library
     space = Screen()           # create a turtle screen (space)
     malik = Turtle()           # create a turtle named malik
     mystery(malik, 100)        # draw something with size = 100