.. mchoice:: qch_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cHardMC
   :topics: Conditionals/cHardMC
   :from_source: T
   :answer_a: first
   :answer_b: first second
   :answer_c: first second third
   :answer_d: first third
   :answer_e: third
   :correct: d
   :feedback_a: This will print, but so will something else.
   :feedback_b: Are you sure about the "second"?  This only prints if y is less than 3, and while it was originally, it changes.
   :feedback_c: Are you sure about the "second"?  This only prints if y is less than 3, and while it was originally, it changes.
   :feedback_d: The first will print since x will be greater than 2 and the second won't print since y is equal to 3 and not less than it.  The third will always print.
   :feedback_e: This will print, but so will something else.

   What would the following print?

   .. code-block:: java

      int x = 3;
      int y = 2;
      if (x > 2) x++;
      if (y > 1) y++;
      if (x > 2) System.out.print("first ");
      if (y < 3) System.out.print("second ");
      System.out.print("third");