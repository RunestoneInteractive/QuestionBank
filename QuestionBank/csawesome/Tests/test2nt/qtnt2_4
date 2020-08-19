.. mchoice:: qtnt2_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: II and III only
   :answer_d: I and II only
   :answer_e: III only
   :correct: b
   :feedback_a: I correctly creates the 7 x 9 matrix, but every value in the matrix remains 0.
   :feedback_b: II correctly creates and fills the matrix with multiples of 2.
   :feedback_c: II is correct, but III does not fill every space correctly. Only diagonal spaces are filled, so most of the spaces are still filled with 0 at the end of the loop. Notice that every time the while loop cycles, the values of row and col both increase.
   :feedback_d: II is correct, but I does not fill the matrix.
   :feedback_e: III does not fill every space correctly. Only spaces lying on the diagonal are filled because the row and column index change at the same time, and the values are incorrect. Most of the spaces remain filled with 0. Notice that every time the while loop cycles, the values of row and col both increase.
   :pct_on_first: 0.3722627737
   :total_students_attempting: 137
   :num_students_correct: 133.0
   :mean_clicks_to_correct: 2.015037594

   Which of the following code segments creates a 7 x 9 array of integers and fills every space in the array with multiples of two (not including the value 0)?
   
   .. code-block:: java
   
      I.   int[][] arr = new int [7][9];
   
      II.  int[][] arr = new int [7][9];
           int count = 1;
   
           for(int i = 0; i < arr.length; i++)
           {
              for(int j = 0; j < arr[0].length; j++)
              {
                 arr[i][j] = count * 2;
                 count++;
              }
           }
   
      III. int[][] arr = new int [7][9];
           int count = 1;
           int row = 0;
           int col = 0;
   
           while (row < arr.length && col < arr[0].length)
           {
              arr[row][col] = count * 2;
              row++;
              col++;
              count++;
           }