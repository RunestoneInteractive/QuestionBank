.. mchoice:: qab_6
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :practice: T
   :answer_a: -1
   :answer_b: -15
   :answer_c: 1
   :answer_d: You will get an out of bounds error.
   :correct: c
   :feedback_a: The method will only return -1 if no value in the array is less than the passed value.
   :feedback_b: The method returns the index of the first item in the array that is less than the value, not the value.
   :feedback_c: Since the method loops from the back towards the front -15 is the last value in the array that is less than -13 and it is at index 1.
   :feedback_d: No, the method correctly starts the index at values.length - 1 and continues as long as i is greater than or equal to 0.

   Given the following code segment (which is identical to the method above) what will be returned when you execute: getIndexOfLastElementSmallerThanTarget(values,-13);

   .. code-block:: java

      private int[ ] values = {-20, -15, 2, 8, 16, 33};

      public static int getIndexOfLastElementSmallerThanTarget(int[ ] values, int compare)
      {
         for (int i = values.length - 1; i >=0; i--)
         {
            if (values[i] < compare)
               return i;
         }
         return -1; // to show none found
      }