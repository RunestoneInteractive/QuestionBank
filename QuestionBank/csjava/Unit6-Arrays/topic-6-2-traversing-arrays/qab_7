.. mchoice:: qab_7
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :practice: T
   :answer_a: -1
   :answer_b: 1
   :answer_c: 2
   :answer_d: You will get an out of bounds error.
   :correct: d
   :feedback_a: The method will only return -1 if no value in the array is less than the passed value.
   :feedback_b: Check the starting index.   Is it correct?
   :feedback_c: Check the starting index.   Is it correct?
   :feedback_d: You can not start the index at the length of the array.  You must start at the length of the array minus one.  This is a common mistake.

   Given the following code segment (which is identical to the method above) what will be returned when you execute: getIndexOfLastElementSmallerThanTarget(values, 7);

   .. code-block:: java

      int[ ] values = {-20, -15, 2, 8, 16, 33};

      public static int getIndexOfLastElementSmallerThanTarget(int[] values, int compare)
      {
         for (int i = values.length; i >=0; i--)
         {
            if (values[i] < compare)
               return i;
         }
         return -1; // to show none found
      }