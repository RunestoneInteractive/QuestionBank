.. mchoice:: qre_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rEasyMC
   :topics: Unit10-Recursion/rEasyMC
   :from_source: T
   :practice: T
   :answer_a: 1
   :answer_b: 3
   :answer_c: 4
   :answer_d: 5
   :answer_e: 6
   :correct: e
   :feedback_a: This is the method declaration.  Look for a call to the same method in the body of the method.
   :feedback_b: This is a conditional, not a method call.
   :feedback_c: This is a return statement, not a method call.
   :feedback_d: This is an else which is part of a conditional, not a method call.
   :feedback_e: This line contains a call to the same method which makes this method recursive.
   :pct_on_first: 0.8376753507
   :total_students_attempting: 499
   :num_students_correct: 496.0
   :mean_clicks_to_correct: 1.3629032258

   Which line has the recursive call?
   
   .. code-block:: java
      :linenos:
   
      public String starString(int n)
      {
         if (n == 0) {
            return "*";
         } else {
            return starString(n - 1) + starString(n - 1);
         }
      }