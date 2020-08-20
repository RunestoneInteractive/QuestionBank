.. mchoice:: cswt01_q19a
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :answer_a: A polygon with n sides
   :answer_b: A circle
   :answer_c: The letter H
   :answer_d: A right triangle
   :correct: a
   :random: 
   :pct_on_first: 0.696969697
   :total_students_attempting: 66
   :num_students_correct: 59.0
   :mean_clicks_to_correct: 1.2711864407

   19. What shape does the following function draw? Assume t is a turtle; n and length are integers.::
   
      def mystery(t, n, length) :
          angle = 360/n
          for i in range(n) :
              t.forward(length)
              t.left(angle)