.. mchoice:: qtnt4_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: arr[i][j]
   :answer_b: arr[0][0]
   :answer_c: 0
   :answer_d: -1
   :answer_e: 1
   :correct: b
   :feedback_a: Notice where min is set in the code. At the time that min is set, i and j have not been delcared and cannot be used. This choice will create a compile-time error.
   :feedback_b: Using the first value in the array guarantees that the correct minimum value will be found and returned, regardless of the range of numbers in the array.
   :feedback_c: Setting min equal to 0 might find the minimum value in some cases. However, if every number in the array is positive, then min will remain 0 and it will not find the minimum value in the array.
   :feedback_d: If min is set to -1, the method would only work correctly if there was a value in the array that was equal to or smaller than -1. If all of the values in the array are greater than -1, then the correct minimum value will not be found.
   :feedback_e: This value would only work correctly if there was a value in the array that was less than 1. If the array is filled with positive numbers, 1 will remain the minimum and the correct minimum may not be found.

   Consider the method ``minVal``, shown below. ``minVal`` compares every value in the given array to ``min`` to find the smallest value, which is then returned. At the beginning of the code, ``min`` is set to 1. Which of the following is the best value to set ``min`` so that the method will compile and work as intended?

   .. code-block:: java

     public int minVal (int[][] arr)
     {
         int min = 1;

         for (int i = 0; i < arr.length; i++)
         {
             for (int j = 0; j < arr[0].length; j++)
             {
                 if (arr[i][j] < min)
                     min = arr[i][j];
             }
         }

         return min;
     }