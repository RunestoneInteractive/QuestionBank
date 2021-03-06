.. mchoice:: qamed_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: Exercises
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: {2, 6, 2, -1, -3}
   :answer_b: {-23, -21, -13, -3, 6}
   :answer_c: {10, 18, 19, 15, 6}
   :answer_d: This method results in an IndexOutOfBounds exception.
   :answer_e: {35, 33, 25, 15, 6}
   :correct: e
   :feedback_a: This would be correct if <code>data[k]</code> was modified in the for-loop. In this for-loop, <code>data[k - 1]</code> is the element that changes.
   :feedback_b: This would be correct if <code>data[k - 1]</code> was subtracted from <code>data[k]</code>. Notice that for every instance of the for-loop, <code>data[k]</code> and <code>data[k - 1]</code> are added together and <code>data[k - 1]</code> is set to that value.
   :feedback_c: This would be correct if the for-loop began at 1 and continued to <code>data.length - 1</code>. Notice the for-loop indexing.
   :feedback_d: The indexing of this method is correct. The for-loop begins at the last valid index and ends when <code>k</code> is equal to 0, and the method does not access any values other than the ones specified.
   :feedback_e: This method starts at the last valid index of the array and adds the value of the previous element to the element at index <code>k - 1</code>.
   :pct_on_first: 0.2595338983
   :total_students_attempting: 1888
   :num_students_correct: 1832.0
   :mean_clicks_to_correct: 2.614628821

   Consider the following method ``changeArray``. An array is created that contains ``{2, 8, 10, 9, 6}`` and is passed to ``changeArray``. What are the contents of the array after the ``changeArray`` method executes?
   
   .. code-block:: java
   
      public static void changeArray(int[] data)
      {
         for (int k = data.length - 1; k > 0; k--)
            data[k - 1] = data[k] + data[k - 1];
      }