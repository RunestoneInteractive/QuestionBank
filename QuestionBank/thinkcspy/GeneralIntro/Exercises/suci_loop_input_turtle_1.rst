.. actex:: suci_loop_input_turtle_1
   :author: peter suci
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the code. Then write the rest of the code needed to have turtle draw a square with a side length specified by the user.
   ~~~~
   import turtle
   side_length = int(input("enter side length"))
   for n in range(0,4):
       turtle.forward(side_length)
       # one more line is needed here to have it draw a square