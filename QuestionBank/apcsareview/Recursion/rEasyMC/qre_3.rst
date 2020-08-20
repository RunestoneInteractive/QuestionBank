.. mchoice:: qre_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rEasyMC
   :topics: Recursion/rEasyMC
   :from_source: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: c
   :feedback_a: Look at line 7 more closely.
   :feedback_b: Many recursive methods only have one recursive call.  But, this one has two.
   :feedback_c: Line 7 has two calls to <code>fibonacci</code>.
   :feedback_d: There are not 3 calls to <code>fibonacci</code>.

   How many recursive calls does the following method contain?

   .. code-block:: java
      :linenos:

      public static int fibonacci(int n)
      {
         if (n == 0)
            return 0;
         else if (n == 1)
            return 1;
         else return fibonacci(n-1) + fibonacci(n-2);
          }