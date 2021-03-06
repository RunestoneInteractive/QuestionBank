.. mchoice:: qsearchse_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: ssEasyMC
   :topics: Unit7-ArrayList/ssEasyMC
   :from_source: T
   :practice: T
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :correct: b
   :feedback_a: This would be true if we were looking for 23.
   :feedback_b: It first compares 23 at index 2 (5 / 2 is 2) to 2.  The second time it compares the 2 at index 0 (1 / 2 = 0) to 2 and returns 0.
   :feedback_c: This would be true if we were looking for 10.
   :pct_on_first: 0.4432296047
   :total_students_attempting: 1189
   :num_students_correct: 1127.0
   :mean_clicks_to_correct: 1.6592724046

   Consider the ``binarySearch`` method below.  How many times would the while loop execute if you first do int[] arr = {2, 10, 23, 31, 55, 86} and then call  binarySearch(arr,2)?
   
   .. code-block:: java
   
      public static int binarySearch(int[] elements, int target) {
         int left = 0;
         int right = elements.length - 1;
         while (left <= right)
         {
            int middle = (left + right) / 2;
            if (target < elements[middle])
            {
               right = middle - 1;
            }
            else if (target > elements[middle])
            {
               left = middle + 1;
            }
            else {
               return middle;
            }
          }
          return -1;
      }