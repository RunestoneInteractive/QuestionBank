.. mchoice:: vis_mc_1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :correct: d
   :answer_a: 8, 7, 6, 5, 4
   :answer_b: 8, 6, 5, 4
   :answer_c: 8, 6, 5
   :answer_d: 8, 6
   :feedback_a: It will not print the 7 due to the continue
   :feedback_b: It will not print the 5 due to the break
   :feedback_c: It will not print the 5 due to the break
   :feedback_d: It will only print 8 and 6.  The break will stop the loop.
   :pct_on_first: 0.2713178295
   :total_students_attempting: 129
   :num_students_correct: 129.0
   :mean_clicks_to_correct: 2.4418604651

   What will the following code print?
   
   .. code-block: python
   
      x = 8
      while x > 3:
          if x == 5:
              break
          if x == 7:
              x = x - 1
              continue
          print(x)
          x = x - 1