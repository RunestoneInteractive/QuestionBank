.. mchoice:: qtnt4_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 720
   :answer_b: 120
   :answer_c: 24
   :answer_d: 15
   :answer_e: This method results in an infinite loop.
   :correct: b
   :feedback_a: This is the value returned for mysteryNum(6). Try tracing the recursive calls again.
   :feedback_b: This method calculates n! (n factorial) by subtracting 1 from n until n equals 1. Then, it works through the calls, multiplying each value of n by the previous values. 5 * 4 * 3 * 2 * 1 equals 120.
   :feedback_c: This is the value returned for mysteryNum(4). Trace the calls again.
   :feedback_d: Notice the recursive call. This would be correct if the code added n to the value returned by the recursive call. Instead, the returned value is multiplied by n.
   :feedback_e: Notice the precondition for the method. Because every value will be greater than 1, the method will always reach its base case.
   :pct_on_first: 0.59375
   :total_students_attempting: 96
   :num_students_correct: 93.0
   :mean_clicks_to_correct: 1.7741935484

   The ``mysteryNum`` method is shown below. What is returned as a result of ``mysteryNum(5)``?
   
   .. code-block:: java
   
      /** Precondition: all values of n are greater than 1 **/
      public int mysteryNum (int n)
      {
          if (n == 1)
              return 1;
   
          else
              return n * mysteryNum(n - 1);
      }