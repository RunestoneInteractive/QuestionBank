.. mchoice:: qtnt3_18
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: System.out.print(arr[x] + " ");
   :answer_b: System.out.print(x + " ");
   :answer_c: System.out.print(x.toString() + " ");
   :answer_d: System.out.print(row[x] + " ");
   :answer_e: System.out.print(row.get(x) + " ");
   :correct: b
   :feedback_a: x refers to a String object, not an index in the array. x can be printed directly, because the second for-loop individually selects Strings in each row of the array.
   :feedback_b: This method uses two for-each loops. The variable x refers to a single String located in the array, so only x needs to be printed. This method will loop through the entire 2-D array, printing out all the names in the matrix.
   :feedback_c: This will compile without error, but the toString is unnecessary. x is already a String and can be printed directly.
   :feedback_d: x refers to a String object, not an index in the array row. x can be printed directly.
   :feedback_e: x is a String, not an index.

   The method ``printNames`` is located below. It prints out all the names in a 2-D matrix. Which of the following correctly replaces ``/* to be determined */`` to make the method work as intended?

   .. code-block:: java

      public void printNames (String[][] arr)
      {
           for (String[] row : arr)
           {
               for (String x : row)
               {
                   /* to be determined */
               }

               System.out.println();
           }
      }