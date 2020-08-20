.. mchoice:: ePost_3_20
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPAbilitySummary
   :subchapter: Exercises
   :topics: CSPAbilitySummary/Exercises
   :from_source: T
   :answer_a: [-5, 5, 0]  [3, 1, 3, 5]
   :answer_b: [10, 5, 0]  [3, 1, 3, 100]
   :answer_c: [-5, 5, 0]  [3, 1, 3, 100]
   :answer_d: [10, -5, 0]  [3, 1, 3, 100]
   :answer_e: [10, -5, 0]  [3, 1, 3, 5]
   :correct: d
   :feedback_a: This would be true if the first index in an array was 1 not 0.
   :feedback_b: This would be true if it was a[1] = 5 not a[1] = -5
   :feedback_c: This would be true if it was a[0] = -5.
   :feedback_d: The value of a at index 1 is changed to -5.  The variable val is set to 0.  Then the value of a is printed.  Then b is set to [3,1,3,0].  Then the value at index 3 in b is set to 100.  Then it prints the value of b.
   :feedback_e: This would be true if it was var = a[1] before a[1] was changed.

   What is the output from the program below?

   ::

      a = [10,5,0]
      a[1] = -5
      val = a[2]
      print (a)
      b = [3,1,3,val]
      b[3] = 100
      print (b)