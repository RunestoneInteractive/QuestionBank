.. activecode:: td_avoid_collision
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPTurtleDecisions
   :subchapter: collisions
   :topics: CSPTurtleDecisions/collisions
   :from_source: T
   :tour_1: "Structural Tour"; 1-2: td4-line1-2; 3-6: td4-line3-6; 7: td4-line7; 8-11: td4-line8-11; 12: td4-line12; 13-14: td4-line13-14; 15-17: td4-line15-17;
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
       if (mia.xcor() - jaz.xcor() < 40):
               jaz.right(45)
               mia.right(45)