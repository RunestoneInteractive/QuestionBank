.. actex:: suci_turtle_loop_1
   :author: peter suci
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the program. Then modify it so that it draws 5 lines with spaces in between instead of 2.
   ~~~~
   import turtle
   for n in range(0,2):
       turtle.forward(20)
       turtle.penup()
       turtle.forward(10)
       turtle.pendown()