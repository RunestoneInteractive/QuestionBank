.. mchoice:: qrb_3
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :correct: b
   :feedback_a: Look again.  What is the value of n when this method returns a value, without doing a recursive call?
   :feedback_b: This method stops calling itself when n equals 1 (line 3).
   :feedback_c: Look for a return with a number after it.  When is this code executed?

   What is the value of n when this method stops calling itself (when it reaches the base case)?

    .. code-block:: java
      :linenos:

      public static int product(int n)
      {
         if(n == 1)
            return 1;
         else
            return n * product(n - 2);
      }