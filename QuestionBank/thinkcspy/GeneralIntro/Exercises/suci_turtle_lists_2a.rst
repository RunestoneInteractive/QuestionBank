.. actex:: suci_turtle_lists_2a
   :author: peter suci
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the program. Modify it so that it draws one more square filled with blue
   ~~~~
   import turtle
   for color in ("blue","red"):
       turtle.begin_fill()
       turtle.color(color)
       for n in range(0,3):
          turtle.forward(50)
          turtle.left(90)
       turtle.end_fill()
       turtle.penup()
       turtle.forward(70)
       turtle.pendown()