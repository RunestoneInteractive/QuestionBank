.. mchoice:: qIndexOutOfBounds
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :practice: T

   Which of the following loop headers will cause an ArrayIndexOutOfBounds error while traversing the array scores?


   - for (int i = 0; i < scores.length; i++)

     - This loop will traverse the complete array.

   - for (int i = 1; i < scores.length; i++)

     - This loop will not cause an error even though it will not visit the element at index 0.

   - for (int i = 0; i <= scores.length; i++)

     + The index cannot be equal to scores.length, since (scores.length - 1) is the index of the last element.

   - for (int i = 0; scores.length > i; i++)

     - Although the ending condition looks strange, (scores.length > i) is equivalent to (i < scores.length).

   - for (int i = scores.length - 1; i >= 0; i++)

     + This will cause an error because i++ will continue to increment the index past the end of the array. It should be replaced with i-- to avoid this error.