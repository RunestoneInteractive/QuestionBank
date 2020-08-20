.. mchoice:: qtnt3_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: arr[i][j] = ans[i];
   :answer_b: ans[i] += arr[i][j];
   :answer_c: ans[i ][j] += arr[i][j];
   :answer_d: ans[i] = arr[i][j];
   :answer_e: arr[i][j] += ans[i];
   :correct: b
   :feedback_a: In Java, assignments work from right to left. This answer assigns the value of ans[i] in the 1-D array to the value of the 2-D array. Instead, we want to add the values of the row i in the 2-D array and assign this sum to ans[i] in the 1-D array.
   :feedback_b: In order to return the right array, the value at ans[i] must contain the sums of every element in row i of the 2-D array. The second for-loop adds the value of every element in row i of the 2-D array and assigns these values to ans[i].
   :feedback_c: Notice that ans is a 1-D array, not a 2-D array. There cannot be two indexes for an element of ans, because ans is only a 1-D array.
   :feedback_d: This line reassigns the value of arr[i][j] to ans[i], but it does not sum all the values in the row. This line would return an array with the value in the last column of each row.
   :feedback_e: Remember that assignment works from right to left in Java. This line adds the value of ans[i] in the 1-D array to the value of arr[i][j] in the 2-D array. The 2-D array should not be modified by this method.

   The method ``rowSums`` returns an array of integers. Each element of the array holds the sum of the corresponding row of a 2-D matrix. Which line correctly fills in ``\* to be determined *\`` in ``rowSums``?

   .. code-block:: java

      public int[] rowSums(int[][] arr)
      {
          int[] ans = new int[arr.length];

          for (int i = 0; i < arr.length; i++)
          {
              for (int j = 0; j < arr[0].length; j++)
              {
                      /* to be determined */
              }
          }

          return ans;
      }