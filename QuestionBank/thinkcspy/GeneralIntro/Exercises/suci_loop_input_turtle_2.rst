.. actex:: suci_loop_input_turtle_2
   :author: peter suci
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the code. Then modify the code so it will draw a hexagon (six sides)
   ~~~~
   import turtle
   side_length = int(input("enter side length"))
   for n in range(0,6):
       turtle.forward(side_length)
       turtle.left(90)