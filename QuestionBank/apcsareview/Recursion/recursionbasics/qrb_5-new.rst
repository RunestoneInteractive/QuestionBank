.. mchoice:: qrb_5-new
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: recursionbasics
   :topics: Recursion/recursionbasics
   :from_source: T
   :answer_a: yes
   :answer_b: no
   :correct: b
   :feedback_a: Where is the call to the same method?
   :feedback_b: There is no call to the same method, so it is not recursive.

   Is the following method recursive?

    .. code-block:: java
      :linenos:

      public static int bunnyEars(int bunnies)
      {
         int total = 0;
         for (int i = 0; i < bunnies; i++)
         {
            total = total + 2;
         }
         return total;
      }