.. mchoice:: qa2dm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: a2dMedMC
   :topics: Unit8-2DArray/a2dMedMC
   :from_source: T
   :practice: T
   :answer_a: { {2 3 3}, {1 2 3}, {1 1 2}, {1 1 1}}
   :answer_b: { {2 1 1}, {3 2 1}, {3 3 2}, {3 3 3}}
   :answer_c: { {2 1 1 1}, {3 2 1 1}, {3 3 2 1}}
   :answer_d: { {2 3 3 3}, {1 2 3 3}, {1 1 2 3}}
   :answer_e: { {1 1 1 1}, {2 2 2 2}, {3 3 3 3}}
   :correct: b
   :feedback_a: This woud be true if the code put a 3 in the array when the row index is less than the column index and a 2 in the array when the row and column index are the same, and a 1 in the array when the row index is greater than the column index.
   :feedback_b: This code will put a 1 in the array when the row index is less than the column index and a 2 in the array when the row and column index are the same, and a 3 in the array when the row index is greater than the column index.
   :feedback_c: This code creates a 2D array with 4 rows and 3 columns so this can't be right.
   :feedback_d: This code creates a 2D array with 4 rows and 3 columns so this can't be right.
   :feedback_e: This code creates a 2D array with 4 rows and 3 columns so this can't be right.
   :pct_on_first: 0.435380385
   :total_students_attempting: 1091
   :num_students_correct: 1067.0
   :mean_clicks_to_correct: 2.2455482662

   What are the contents of ``mat`` after the following code segment has been executed?
   
   .. code-block:: java
   
      int [][] mat = new int [4][3];
      for (int row = 0; row < mat.length; row++) {
         for (int col = 0; col < mat[0].length; col++) {
            if (row < col)
               mat[row][col] = 1;
            else if (row == col)
               mat[row][col] = 2;
            else
               mat[row][col] = 3; } }