.. mchoice:: qaeasy_6
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: {1, 3, -5, -2}
   :answer_b: {3, 9, -15, -6}
   :answer_c: {2, 6, -10, -4}
   :answer_d: The code will never stop executing due to an infinite loop
   :correct: b
   :feedback_a: This would be true if the contents of arrays could not be changed but they can.
   :feedback_b: This code multiplies each value in a by the passed amt which is 3 in this case.
   :feedback_c: This would be correct if we called multAll(2) instead of multAll(3).
   :feedback_d: The variable i starts at 0 and increments each time through the loop and stops when it equals the number of items in a.

   What are the values in a after multAll(3) executes?

   .. code-block:: java

     private int[ ] a = {1, 3, -5, -2};

     public void multAll(int amt)
     {
        int i = 0;
        while (i < a.length)
        {
           a[i] = a[i] * amt;
           i++;
        } // end while
     } // end method