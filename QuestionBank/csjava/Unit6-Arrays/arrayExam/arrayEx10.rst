.. mchoice:: arrayEx10
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/arrayExam
   :from_source: T
   :practice: T
   :answer_a: {4, 3, 0, 0}
   :answer_b: {4, 1, 3, 0}
   :answer_c: {2, 4, 3, 0}
   :answer_d: {2, 4, 1, 3}
   :correct: a
   :feedback_a: This copies the value from array1[a1] to array2[a2] but only if the value at array1[a1] is greater than or equal to 2.  So it copies the 4 and 3.  Notice that a2 starts at 0 and a1 starts at 1.
   :feedback_b: This would be true except that a2 is only incremented if the copy occurs.
   :feedback_c: Walk through the very first iteration of the loop and notice that after the first iteration the first value in array2 is 4.
   :feedback_d: This would be true if we were asking for the values in array1.

   After the following code executes what are the values in ``array2``?

   .. code-block:: java

      int[] array1 = {2, 4, 1, 3};
      int[] array2 = {0, 0, 0, 0};
      int a2 = 0;
      for (int a1=1; a1 < array1.length; a1++)
      {
         if (array1[a1] >= 2)
         {
            array2[a2] = array1[a1];
            a2++;
         }
      }