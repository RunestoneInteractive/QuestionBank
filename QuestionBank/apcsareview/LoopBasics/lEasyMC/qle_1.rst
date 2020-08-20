.. mchoice:: qle_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: lEasyMC
   :topics: LoopBasics/lEasyMC
   :from_source: T
   :answer_a: 5 6 7 8 9
   :answer_b: 4 5 6 7 8 9 10 11 12
   :answer_c: 3 5 7 9 11
   :answer_d: 3 4 5 6 7 8 9 10 11 12
   :correct: d
   :feedback_a: What is i set to in the initialization area?
   :feedback_b: What is i set to in the initialization area?
   :feedback_c: This loop changes i by 1 each time in the change area.
   :feedback_d: The value of i starts at 3 and this loop will execute until i equals 12.  The last time through the loop the value of i is 12 at the begininng and then it will be incremented to 13 which stops the loop since 13 is not less than or equal to 12.

   What does the following code print?

   .. code-block:: java

     for (int i = 3; i <= 12; i++)
     {
        System.out.print(i + " ");
     }