.. mchoice:: qtnt2_12
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: II and III
   :answer_e: I, II, and III
   :correct: d
   :feedback_a: I will find the sum of all the values in the matrix, but it does not find the sum of a specific row.
   :feedback_b: II is correct, but III is also correct. This method can be completed by using a while loop or a for loop.
   :feedback_c: III is correct, but II is also correct. This method can be completed by using a for loop or a while loop.
   :feedback_d: II and III both correctly add the values in the specified row.
   :feedback_e: II and III are correct, but I adds every value in the matrix, not just the specified row.
   :pct_on_first: 0.5028248588
   :total_students_attempting: 177
   :num_students_correct: 175.0
   :mean_clicks_to_correct: 1.7142857143

   You are trying to write a method ``sumRow`` that finds the sum of the values in a specified row of a 2-D matrix. Which of the following code segments could replace ``/* to be determined */`` to make the code work correctly?
   
   .. code-block:: java
   
      public int sumRow (int row, int[][] values)
      {
         int sum = 0;
   
         /* to be determined */
   
         return sum;
      }
   
      //I.
      for (int[] rowValues : values)
      {
         for (int x : rowValues)
         {
            sum += x;
         }
      }
   
      //II.
      for (int i = 0; i < values[0].length;i++)
      {
         sum += values[row][i];
      }
   
      //III.
      int col = 0;
      while (col < values[0].length)
      {
         sum += values[row][col];
         col++;
      }