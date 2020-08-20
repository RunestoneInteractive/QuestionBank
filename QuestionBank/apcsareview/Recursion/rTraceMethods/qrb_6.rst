.. mchoice:: qrb_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rTraceMethods
   :topics: Recursion/rTraceMethods
   :from_source: T
   :answer_a: 10
   :answer_b: 32
   :answer_c: 16
   :answer_d: 64
   :correct: b
   :feedback_a: This would be correct if it addition instead of multiplication.
   :feedback_b: This method calculates 2 raised to the nth power.
   :feedback_c: Check that you didn't miss one of the recursive calls.
   :feedback_d: This would be true if the call was mystery(6).

        Given the method defined below what does the following return: mystery(5)?

    .. code-block:: java
     :linenos:

     public static int mystery(int n)
     {
        if (n == 0)
           return 1;
        else
           return 2 * mystery (n - 1);
     }