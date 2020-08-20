.. mchoice:: qtnt4_20
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 12
   :answer_b: 27
   :answer_c: 81
   :answer_d: 243
   :answer_e: This method will result in an infinite loop.
   :correct: c
   :feedback_a: This would be correct if the else statement returned 3 + the recursive call. The value returned by the recursive call is multiplied by 3.
   :feedback_b: This method calculates 3 ^ num. 3 ^ 4 is not equal to 27. Check your tracing and try again.
   :feedback_c: This method calculates 3 ^ num. It goes through the recursive calls until num reaches 1, then 3 is multiplied by itself (num) times. The method has been called four times, and 3 ^ 4 is 81.
   :feedback_d: This method calculates 3 ^ num. 3 ^ 4 is not equal to 243. Check your tracing and try again.
   :feedback_e: This method will end properly. If num is less than or equal to 1, a value of 3 will be returned.


   Consider the method ``threes``. What is returned as a result of ``threes(4)``?

   .. code-block:: java

     public int threes (int n)
     {
         if (n <= 1)
             return 3;

         else
             return 3 * threes(n - 1);
     }