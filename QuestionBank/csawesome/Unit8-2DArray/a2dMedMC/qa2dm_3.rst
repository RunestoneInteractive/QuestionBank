.. mchoice:: qa2dm_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: a2dMedMC
   :topics: Unit8-2DArray/a2dMedMC
   :from_source: T
   :practice: T
   :answer_a: 4
   :answer_b: 6
   :answer_c: 9
   :answer_d: 10
   :answer_e: 20
   :correct: c
   :feedback_a: This would be correct if it was adding up all the values in the first row.  Does it?
   :feedback_b: This would be correct if it was adding up all the values in column 0.
   :feedback_c: This adds all the values in column 1 starting with the one in the last row (row 3).
   :feedback_d: This would be correct if it was adding up all the values in the second row.
   :feedback_e: This would be correct if it was adding up all the values in the last row.
   :pct_on_first: 0.5548266167
   :total_students_attempting: 1067
   :num_students_correct: 1044.0
   :mean_clicks_to_correct: 1.9051724138

   Given the following code segment, what is the value of sum after this code executes?
   
   .. code-block:: java
   
      int[][] m = { {1,1,1,1},{1,2,3,4},{2,2,2,2},{2,4,6,8}};
   
      int sum = 0;
      for (int k = 0; k < m.length; k++) {
          sum = sum + m[m.length-1-k][1];
      }