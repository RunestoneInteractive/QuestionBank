.. activecode:: td_avoid_collision_answer
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPTurtleDecisions
   :subchapter: collisions
   :topics: CSPTurtleDecisions/collisions
   :from_source: T
   :nocodelens:

   from turtle import *
   space = Screen()
   jaz = Turtle()
   jaz.shape('turtle')
   mia = Turtle()
   mia.shape('turtle')
   mia.color('red')
   mia.penup()
   mia.goto(100,0)
   mia.pendown()
   mia.right(180)
   for x in range(20):
       jaz.forward(10)
       mia.forward(10)
       if (mia.xcor() - jaz.xcor() < 40 and mia.ycor() - jaz.ycor() < 10):
           jaz.right(45)
           mia.right(45)