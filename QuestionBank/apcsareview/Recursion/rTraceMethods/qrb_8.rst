.. mchoice:: qrb_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Recursion
   :subchapter: rTraceMethods
   :topics: Recursion/rTraceMethods
   :from_source: T
   :answer_a: 12344321
   :answer_b: 1234
   :answer_c: 4321
   :answer_d: 43211234
   :answer_e: 32144123
   :correct: d
   :feedback_a: Remember that 1234 % 10 returns the rightmost digit.
   :feedback_b: There are two calls that print something in this method.
   :feedback_c: There are two calls that print something in this method.
   :feedback_d: This method prints the right most digit and then removes the rightmost digit for the recursive call.  It prints both before and after the recursive call.
   :feedback_e: Since 1234 % 10 returns the rightmost digit, the first thing printed is 4.

        Given the method defined below what does the following print: mystery(1234)?

    .. code-block:: java
     :linenos:

     public static void mystery (int x) {
        System.out.print(x % 10);

        if ((x / 10) != 0) {
           mystery(x / 10);
        }
        System.out.print(x % 10);
     }