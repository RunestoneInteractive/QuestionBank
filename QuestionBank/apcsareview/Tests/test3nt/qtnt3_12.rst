.. mchoice:: qtnt3_12
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: 4
   :answer_b: 5
   :answer_c: 0
   :answer_d: 13
   :answer_e: 14
   :correct: e
   :feedback_a: Trace the recursive call and the return statements.
   :feedback_b: Examine the recursive call and the return statements. This method adds the values of the digits in a number; it does not find the number of digits.
   :feedback_c: Examine the return statements. Although the last digit of the number is 0, 0 is returned to the previous calls, where it is added to the other digits.
   :feedback_d: Try tracing the recursive calls again.
   :feedback_e: The method divides the number by 10 until it reaches the first dight. Then, it adds the values of all of the digits together.

   The method ``numFun`` is below. What is returned as a result of ``numFun(21560)``?

   .. code-block:: java

      public static int numFun(int num)
      {
           if (num / 10 == 0)
                return num;

           else
                return (num % 10) + numFun(num / 10);
      }