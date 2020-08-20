.. mchoice:: 8_3_2_NegativeCounter
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: whileCount
   :topics: CSPWhileAndForLoops/whileCount
   :from_source: T
   :practice: T
   :answer_a: 5 4 3 2 1
   :answer_b: -5 -4 -3 -2 -1
   :answer_c: -4 -3 -2 -1 0
   :correct: c
   :feedback_a: If x starts at -5 how can the first value printed be 5?
   :feedback_b: This would be true if the print statement was before we incremented x.
   :feedback_c: The value of x is incremented before it is printed so the first value printed is -4.
   :pct_on_first: 0.4455151964
   :total_students_attempting: 1349
   :num_students_correct: 1343.0
   :mean_clicks_to_correct: 1.7170513775

   What does the following code print?
   
   ::
   
      output = ""
      x = -5
      while x < 0:
          x = x + 1
          output = output + str(x) + " "
      print(output)