.. mchoice:: qrm_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rMedMC
   :topics: Unit10-Recursion/rMedMC
   :from_source: T
   :practice: T
   :answer_a: 8
   :answer_b: 3
   :answer_c: There is no result because of infinite recursion.
   :answer_d: 5
   :answer_e: 0
   :correct: d
   :feedback_a: This would be true if it was <code>f(6)</code> not <code>f(5)</code>.
   :feedback_b: This would be true if it was <code>f(4)</code> not <code>f(5)</code>.
   :feedback_c: This method will stop when <code>n</code> equals <code>0</code> or <code>1</code>.
   :feedback_d: This is the Fibonacci method which returns <code>0</code> for <code>0</code> and <code>1</code> for <code>1</code> and <code>Fibonacci(n-1) + Fibonacci(n-2)</code> for the rest of the numbers.
   :feedback_e: This would be true if it was <code>f(0)</code> not <code>f(5)</code>.
   :pct_on_first: 0.3788187373
   :total_students_attempting: 491
   :num_students_correct: 484.0
   :mean_clicks_to_correct: 2.097107438

   Given the following method declaration, what value is returned as the result of the call ``f(5)``?
   
   .. code-block:: java
      :linenos:
   
      public static int f(int n)
      {
         if (n == 0)
            return 0;
         else if (n == 1)
            return 1;
         else return f(n-1) + f(n-2);
      }