.. actex:: suci_turtle_house_1
   :author: peter suci
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the program then modify it so that the door is 20 units on each side.
   ~~~~
   import turtle
   for n in range(0,4):
      turtle.forward(50)
      turtle.left(90)
   turtle.penup()
   turtle.goto(10,30)
   turtle.pendown()
   for n in range(0,4):
      turtle.forward(10)
      turtle.left(90)
   turtle.penup()
   turtle.goto(30,30)
   turtle.pendown()
   for n in range(0,4):
      turtle.forward(10)
      turtle.left(90)
   turtle.penup()
   turtle.goto(20,0)
   turtle.pendown()
   for n in range(0,4):
      turtle.forward(15)
      turtle.left(90)
   turtle.penup()
   turtle.goto(0,50)
   turtle.pendown()
   for n in range(0,3):
      turtle.forward(50)
      turtle.left(120)