.. mchoice:: qrh_2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/rHardMC
   :from_source: T
   :practice: T
   :answer_a: 5
   :answer_b: 4
   :answer_c: 6
   :answer_d: 7
   :answer_e: The method never returns due to infinite recursion.
   :correct: a
   :feedback_a: The first time the method is called, <code>i</code> is not equal to 0, so the method makes a recursive call to itself, with the value of 82/3 which equals 27 due to integer division.  This is still not equal to 0, so the method calls itself with the first parameter equal to 9, then 3, then 1. Finally, the method is called with the first parameter of 1/3 which equals 0 due to integer division which throws away any decimal part. Each method call adds 1 to the result, except for the final call when <code>i</code> is equal to 0.
   :feedback_b: Each time the method is called when <code>i</code> is not equal to 0, the return value is incremented. This happens 5 times, with <code>i</code> equal to 81, 27, 9, 3, and 1.
   :feedback_c: The return value is not incremented the last time the method is called, when <code>i</code> is equal to 0.
   :feedback_d: The method only executes 6 times, with the return value incremented each time <code>i</code> is not equal to zero
   :feedback_e: Infinite recursion would happen if the method never reached its base case where <code>i</code> is equal to 0. This would be true if the division could result in a constantly shrinking fraction, but integer division truncates the fractional portion of the division.

   Given the following method declaration, what will ``redo(82, 3)`` return?

   .. code-block:: java

      public static int redo(int i, int j)
      {
         if (i==0)
            return 0;
         else
            return redo(i/j, j)+1;
      }