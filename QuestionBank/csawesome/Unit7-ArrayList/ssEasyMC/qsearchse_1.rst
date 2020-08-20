.. mchoice:: qsearchse_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssEasyMC
   :topics: Unit7-ArrayList/ssEasyMC
   :from_source: T
   :practice: T
   :answer_a: -1
   :answer_b: 0
   :answer_c: 1
   :answer_d: 2
   :answer_e: 50
   :correct: d
   :feedback_a: This value is returned if the target is not in the list since this is a sequential search.
   :feedback_b: This would be true if the target was 90 since this is a sequential search.
   :feedback_c: This would be true if the target was -30 since this is a sequential search.
   :feedback_d: This is a sequential search that returns the index where the target appears in the elements list
   :feedback_e: A sequential search returns the index, not the value.  What is the index of the 50?
   :pct_on_first: 0.5653594771
   :total_students_attempting: 1224
   :num_students_correct: 1177.0
   :mean_clicks_to_correct: 1.8258283772

   What would the following code return from mystery([90, -30, 50], 50)?
   
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