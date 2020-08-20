.. mchoice:: cswt1_q19
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :answer_a: A polygon with n sides
   :answer_b: A circle
   :answer_c: The letter H
   :answer_d: A right triangle
   :correct: a
   :rando: 
   :pct_on_first: 1.0
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.0

   What shape does the following function draw? Assume t is a turtle; n and length are integers::
   
      def mystery(t, n, length) :
          angle = 360/n
          for i in range(n) :
              t.forward(length)
              t.left(angle)