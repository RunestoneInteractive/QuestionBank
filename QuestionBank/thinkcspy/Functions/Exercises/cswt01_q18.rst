.. mchoice:: cswt01_q18
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :answer_a: An equilateral triangle
   :answer_b: a right triangle
   :answer_c: a parallelagram
   :answer_d: a star with three points
   :correct: a
   :random: 
   :pct_on_first: 0.8444444444
   :total_students_attempting: 45
   :num_students_correct: 45.0
   :mean_clicks_to_correct: 1.2

   What shape does the following code draw?::
   
      import turtle
      wn = turtle.Screen()
      janet = turtle.Turtle()
      janet.back(75)
      for i in range(3) :
          janet.forward(150)
          janet.left(120)