.. mchoice:: qtnt1_14
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: I
   :answer_b: II
   :answer_c: III
   :answer_d: IV
   :answer_e: An ArrayIndexOutOfBoundsException will be thrown.
   :correct: c
   :feedback_a: Since the inside for loop starts with t = 0  and continues while t < i (and i begins at 0) it will not be print out every single element of the 4x4 matrix.
   :feedback_b: This anwser is not correct because our inside for loop will start with t = 0 and loop while t < i and, as such, the entire first row of our matrix will be ignored, since both t and i = 0 and t is not less than i.
   :feedback_c: When i = 0, the inner for loop does not get executed and the entire first row of the matrix is ignored. When i = 1 t goes from 0 to 0 and the element matrix[1][0] will be printed out. Similarly, when i = 2 we will print out elements matrix[2][0] and matrix[2][1]. Finally, when i = 3, we will print out matrix[3][0], matrix[3][1] and matrix[3][2].
   :feedback_d: This would be the correct anwser if we kept incrementing i by one (the outer for loop) but the inner for variable t would always be 0. We would get the first element of each row.
   :feedback_e: We will not get an index out of bounds exception since we made sure to increment i only until the max length of the array and the other variable we use to index, t, will only increase while it is still less than i.

   Suppose that the following method takes in a two dimensional array called ``matrix``. After the method call ``printMatrix(matrix)`` what will the output be? Possible options are listed below the method definition.

   .. code-block:: java

      /* assume that matrix has the following values */
      7654
      3210
      4567
      0123

      public static void printMatrix(int[][] matrix)
      {
        for (int i = 0; i < matrix.length; i++)
        {

          for (t = 0; t < i; t++)
          {
            System.out.println(matrix[i][t]);
          }
          System.out.println();
        }
      }

      Possible output:

      I.
      7654
      3210
      4567
      0123

      II.
      7
      32
      456
      0123

      III.
      3
      45
      012

      IV.
      7
      3
      4
      0