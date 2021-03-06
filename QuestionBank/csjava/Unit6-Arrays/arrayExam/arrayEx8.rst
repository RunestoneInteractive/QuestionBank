.. mchoice:: arrayEx8
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/arrayExam
   :from_source: T
   :practice: T
   :answer_a: <code>for (int j=0 ; j < x.length; j++)</code>
   :answer_b: <code>for (int j=0 ; j < x.length - 1; j++)</code>
   :answer_c: <code>for (int j=i+1; j < x.length; j++)</code>
   :answer_d: <code>for (int j=i+1; j < x.length - 1; j++)</code>
   :correct: c
   :feedback_a: The inner loop should start at the outer loop current position plus one to not double count inversions.
   :feedback_b: The inner loop should start at the outer loop current position plus one to not double count inversions.
   :feedback_c: This correctly starts at the outer loop current index plus one and loops through the rest of the array.
   :feedback_d: This misses checking the last value in the array since it is <code>j < x.length-1</code>.

   If any two numbers in an array of integers, not necessarily consecutive numbers in the array, are out of order (i.e. the number that occurs first in the array is larger than the number that occurs second), then that is called an inversion. For example, consider an array “x” that has the values {1, 4, 3, 2}.  Then there are three inversions since 4 is greater than both 3 and 2 and 3 is greater than 2.  Which of the following can be used to replace the missing code so that the code correctly counts the number of inversions?

   .. code-block:: java


      int inversionCount = 0;
      for (int i=0 ; i < x.length - 1 ; i++)
      {
         // missing code goes here
         {
            if (x[i] > x[j])
               inversionCount++;
         }
      }