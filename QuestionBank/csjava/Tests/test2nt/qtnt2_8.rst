.. mchoice:: qtnt2_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: y is greater than 1
   :answer_b: y is less than or equal to 0
   :answer_c: y is greater than x
   :answer_d: all of the above
   :answer_e: none of the above
   :correct: b
   :feedback_a: Eventually, the recursive calls will reach the base case, where y is greater than or equal to x. If y is greater than 1, multiplying by 10 will increase y and y will remain positive.
   :feedback_b: If y is less than or equal to 0, multiplying by 10 will not make the value greater than x. The base case will never be reached, and the method will continue running until the computer runs out of memory.
   :feedback_c: If y is greater than x, the method will reach its base case on the first pass of the method.
   :feedback_d: Not all of the statements are correct. If y is greater than x or if y is greater than 1, the method will eventually reach its base case and end.
   :feedback_e: One of the statements is correct. If y is less than or equal to 0, multiplying by 10 will not make y become greater than x.

   Consider the following method ``mystery``. Assuming x is an integer greater than 1, in which case does ``mystery`` result in an infinite loop?

   .. code-block:: java

      public int mystery(int x, int y)
      {
         if (x <= y)
             return x;
         else
             return mystery(x, y * 10);
      }