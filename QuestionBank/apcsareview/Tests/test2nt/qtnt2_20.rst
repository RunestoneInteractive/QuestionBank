.. mchoice:: qtnt2_20
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: This method will work correctly for all arrays.
   :answer_b: The first value in the array is less than 0.
   :answer_c: The first value in the array is equal to 0.
   :answer_d: Every value in the array is greater than 0.
   :answer_e: Every value in the array is less than 0.
   :correct: e
   :feedback_a: This method will not work correctly for all arrays. Look at the starting value for maxVal, and how maxVal is compared to all the values of the array. What happens if every value in the array is less than maxVal?
   :feedback_b: Although this might present a problem if EVERY value in the array is less than 0, the compiler will move on to the next index without issue if the first value in the array is less than 0.
   :feedback_c: This will not present a problem, as the if-statement has not been met and the for-loop will simply continue to the second element.
   :feedback_d: If every value in the array is greater than 0, the method will work properly.
   :feedback_e: maxVal is set to zero, so if every number in the array is less than 0, the maxVal will remain 0. A better idea would be to set maxVal to the value of the first element in the array.


   Consider the method ``findMax``, which uses sequential search to find the index of the largest value of an array. In which case would ``findMax`` not work properly?


   .. code-block:: java

     public int findMax(int[] arr)
     {
        int maxVal = 0;
        int index = 0;

        for (int i = 0; i < arr.length; i++)
        {
           if (arr[i] > maxVal)
           {
              index = i;
              maxVal = arr[i];
           }
        }
        return index;
     }