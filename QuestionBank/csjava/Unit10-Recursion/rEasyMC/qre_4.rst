.. mchoice:: qre_4
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rEasyMC
   :from_source: T
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: b
   :feedback_a: Look for a call to the same method in the body of the method.
   :feedback_b: Line 6 has one call to <code>multiplyEvens</code>.
   :feedback_c: Where do you see 2 calls to <code>multiplyEvens</code>?
   :feedback_d: Where do you see 3 calls to <code>multiplyEvens</code>?

   How many recursive calls does the following method contain?

   .. code-block:: java
      :linenos:

      public static int multiplyEvens(int n)
      {
         if (n == 1) {
            return 2;
         } else {
            return 2 * n * multiplyEvens(n - 1);
         }
      }