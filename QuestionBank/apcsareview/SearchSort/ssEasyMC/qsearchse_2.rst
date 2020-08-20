.. mchoice:: qsearchse_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: SearchSort
   :subchapter: ssEasyMC
   :topics: SearchSort/ssEasyMC
   :from_source: T
   :answer_a: -1
   :answer_b: 0
   :answer_c: 1
   :answer_d: 2
   :answer_e: -20
   :correct: a
   :feedback_a: A sequential search returns -1 if the target value is not found in the list.
   :feedback_b: This would be true if the target was 90 since this is a sequential search.
   :feedback_c: This would be true if the target was -30 since this is a sequential search.
   :feedback_d: This would be true if the target was
   :feedback_e: A sequential search returns negative one when the value isn't found in the list.

   What would the following code return from mystery([90, -30, 50], -20)?

   .. code-block:: java

      public static int mystery(int[] elements, int target)
      {
        for (int j = 0; j < elements.length; j++)
        {
           if (elements[j] == target)
           {
              return j;
           }
       }
       return -1;
     }