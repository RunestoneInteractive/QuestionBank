.. parsonsprob:: 14_3_2_vert_stripes
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPTurtleDecisions
   :subchapter: oddEven
   :topics: CSPTurtleDecisions/oddEven
   :from_source: T
   :numbered: left
   :adaptive:

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