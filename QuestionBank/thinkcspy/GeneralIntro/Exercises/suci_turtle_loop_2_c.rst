.. actex:: suci_turtle_loop_2_c
   :author: peter suci
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run this program then modify it so it draws 2 squares that are twice the distance apart.
   ~~~~
   import turtle
   turtle.penup()
   turtle.goto(-180,0)
   turtle.pendown()
   side_length = 50
   move = 70
   for index_1 in range(0,2): #this loop tells it how many squares to draw
       turtle.penup()
       turtle.forward(move)
       turtle.pendown()
       for index_2 in range(0,4): #this loop draws the square
           turtle.forward(side_length)
           turtle.left(90)