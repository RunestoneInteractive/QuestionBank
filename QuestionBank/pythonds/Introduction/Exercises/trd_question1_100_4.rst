.. parsonsprob:: trd_question1_100_4
   :author: Majid Rouhani
   :difficulty: 1.0
   :basecourse: pythonds
   :chapter: Introduction
   :subchapter: Exercises
   :topics: Introduction/Exercises
   :from_source: F
   :pct_on_first: 0.1282051282
   :total_students_attempting: 39
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 6.125

   Construct a block of code that correctly implements the recursive function for calcuating the factorial.
   -----
   f factorial(n):
   rint("factorial has been called with n = " + str(n))
   f n == 1:
   return 1
   lse:
   res = n * factorial(n-1)
   print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
   return res	
   
   int(factorial(5))