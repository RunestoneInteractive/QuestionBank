.. parsonsprob:: 14_3_2_vert_stripes
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPTurtleDecisions
   :subchapter: oddEven
   :topics: CSPTurtleDecisions/oddEven
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.1376404494
   :total_students_attempting: 356
   :num_students_correct: 295.0
   :mean_clicks_to_correct: 8.4881355932

   The following program should draw vertical color stipes alternating between red and black, but the code is mixed up.  Drag the block from left to right and place them in the correct order with the correct indention.
   -----
   from turtle import *
   space = Screen()
   height = space.window_height()
   =====
   maxY = height / 2
   sue = Turtle()
   sue.pensize(10)
   sue.left(90)
   =====
   for index in range(5):
   =====
       sue.penup()
   =====
       if index % 2 == 0:
   =====
           sue.color('red')
   =====
       else:
   =====
           sue.color('black')
   =====
       sue.goto(index * 10, -1 * maxY)
       sue.pendown()
       sue.forward(height)