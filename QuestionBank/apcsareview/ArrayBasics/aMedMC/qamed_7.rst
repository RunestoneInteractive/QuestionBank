.. mchoice:: qamed_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: aMedMC
   :topics: ArrayBasics/aMedMC
   :from_source: T
   :answer_a: k - 1
   :answer_b: k + 1
   :answer_c: k
   :answer_d: 1
   :answer_e: 0
   :correct: a
   :feedback_a: This loop will start at 1 and continue until <code>k</code> is reached as long as <code>arr[i] < someValue</code> is true.  The last time the loop executes, <code>i</code> will equal <code>k-1</code>, if the condition is always true.  The number of times a loop executes is equal to the largest value when the loop executes minus the smallest value plus one.  In this case that is <code>(k - 1) - 1 + 1</code> which equals <code>k - 1</code>.
   :feedback_b: This would be true if <code>arr[i] < someValue</code> was always true and the loop started at 0 instead of 1 and continued while it was less than or equal to <code>k</code>.
   :feedback_c: This would be true if <code>arr[i] < someValue</code> was always true and the loop started at 0 instead of 1.
   :feedback_d: This would be the case if only one element in the array would fulfill the condition that <code>arr[i] < someValue</code>.
   :feedback_e: This is the minimum number of times that <code>HELLO</code> could be executed.  This would be true if <code>k</code> was less than <code>i</code> initially.

   Consider the following code. What is the *maximum* amount of times that ``HELLO`` could possibly be printed?

   .. code-block:: java

      for (int i = 1; i < k; i++)
      {
         if (arr[i] < someValue)
         {
           System.out.print("HELLO")
         }
      }