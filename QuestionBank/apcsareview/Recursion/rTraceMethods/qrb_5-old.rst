.. mchoice:: qrb_5-old
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rTraceMethods
   :topics: Recursion/rTraceMethods
   :from_source: T
   :answer_a: 1
   :answer_b: 120
   :answer_c: 720
   :answer_d: 30
   :correct: c
   :feedback_a: This would be correct if it was factorial(0), but don't forget the recursive calls.
   :feedback_b: This would be correct if it was factorial(5), but this is factorial(6).
   :feedback_c: If you remember that factorial(5) was 120 then this is just 6 * 120 = 720.
   :feedback_d: It doesn't return 6 * 5 it returns 6 * factorial(5).

        Given the method defined below what does the following return: factorial(6)?

    .. code-block:: java
     :linenos:

     public static int factorial(int n)
     {
        if (n == 0)
           return 1;
        else
           return n * factorial(n-1);
     }