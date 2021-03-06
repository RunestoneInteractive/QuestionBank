.. mchoice:: qamed_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: Exercises
   :topics: Unit7-Arrays/Exercises
   :from_source: F
   :practice: T
   :answer_a: Returns the index of the largest value in array <code>arr</code>.
   :answer_b: Returns the index of the first element in array <code>arr</code> whose value is greater than <code>arr[loc]</code>.
   :answer_c: Returns the index of the last element in array <code>arr</code> whose value is greater than <code>arr[loc]</code>.
   :answer_d: Returns the largest value in array <code>arr</code>.
   :answer_e: Returns the index of the largest value in the second half of array <code>arr</code>.
   :correct: a
   :feedback_a: This code sets <code>loc</code> to the middle of the array and then loops through all the array elements.  If the value at the current index is greater than the value at <code>loc</code> then it changes <code>loc</code> to the current index.  It returns <code>loc</code>, which is the index of the largest value in the array.
   :feedback_b: This would be true if there was a <code>return loc</code> after <code>loc = k</code> in the <code>if</code> block.
   :feedback_c: This would be true if it returned <code>loc</code> after setting <code>loc = k</code> and if it started at the end of the array and looped toward the beginning of the array.
   :feedback_d: It returns the <i>index</i> to the largest value in array <code>arr</code>, not the largest value.
   :feedback_e: <code>k</code> loops from 0 to <code>arr.length - 1</code>.  So it checks all of the elements in the array.

   Consider the following field ``arr`` and method ``checkArray``.  Which of the following best describes what ``checkArray`` returns?

   .. code-block:: java

     private int[] arr;

     // precondition: arr.length != 0
     public int checkArray()
     {
         int loc = arr.length / 2;
         for (int k = 0; k < arr.length; k++)
         {
             if (arr[k] > arr[loc])
             {
                 loc = k;
             }
         }
         return loc;
     }