.. mchoice:: qle_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: lEasyMC
   :topics: LoopBasics/lEasyMC
   :from_source: T
   :answer_a: 7
   :answer_b: 8
   :answer_c: 9
   :correct: c
   :feedback_a: This would be true if i started at 1 and ended when it reached 8.
   :feedback_b: This would be true if the loop ended when i reached 8.
   :feedback_c: This loop starts with i = 0 and continues till it reaches 9 so (9 - 0 = 9).

   How many times does the following method print a ``*``?

   .. code-block:: java

     for (int i = 0; i <= 8; i++)
     {
        System.out.print("*");
     }