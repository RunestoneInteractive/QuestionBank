.. mchoice:: ePost_7_17
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPAbilitySummary
   :subchapter: Exercises
   :topics: CSPAbilitySummary/Exercises
   :from_source: T
   :answer_a: Error
   :answer_b: Error and 250.0 on the next line
   :answer_c: 250.0
   :answer_d: 1000 / 4
   :answer_e: Error and 250 on the next line
   :correct: c
   :feedback_a: This would be true if x was initialized to 0.
   :feedback_b: This would be true if the if and else statements weren't there.
   :feedback_c: Since x is initialized to 4 it will print the result of 1000 divided by 4 which is 250.0.
   :feedback_d: This would be true if it was print ("1000 / x") instead.
   :feedback_e: This would be true if the if and else statements weren't there and if 1000 / 4 gave an integer result.

   What is the output from the program below?

   ::

      x = 4
      if x == 0:
          print ("Error")
      else:
          print (1000 / x)