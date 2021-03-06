.. mchoice:: qrm_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit11-Recursion
   :subchapter: rMedMC
   :topics: Unit11-Recursion/rMedMC
   :from_source: T
   :practice: T
   :answer_a: 1
   :answer_b: 10
   :answer_c: 25
   :answer_d: 3125
   :answer_e: 15
   :correct: e
   :feedback_a: The value 1 will only be returned when the initial call to product is less than or equal to 1.
   :feedback_b: If you assume the purpose of the method is to compute <code>n * 2</code>, this is correct, but the product method does not do this. Be sure to trace the code to see what happens.
   :feedback_c: If you assume the purpose of the method is to compute <code>n * n</code> this is correct, but the product method does not do this. Be sure to trace the code to see what happens.
   :feedback_d: If you assume the purpose of the method is to compute <code>n ^ n</code>, this would be correct. But product does not do this. Be sure to trace the code to see what happens.
   :feedback_e: The result from <code>product(5)</code> is <code>5 * product(3)</code> which is 3 * product(1) which is <code>1</code> so the answer is <code>1 * 3 * 5 = 15</code>.

   Given the following method declaration, what value is returned as the result of the call ``product(5)``?

   .. code-block:: java
      :linenos:

      public static int product(int n)
      {
         if (n <= 1)
            return 1;
         else
            return n * product(n - 2);
      }