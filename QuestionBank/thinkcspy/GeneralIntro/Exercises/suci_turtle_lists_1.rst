.. actex:: suci_turtle_lists_1
   :author: peter suci
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the program. Modify it so that it fills the squares with yellow and orange
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