.. mchoice:: qins_2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-6-sorting
   :from_source: T
   :answer_a: line 1
   :answer_b: line 2
   :answer_c: line 3
   :answer_d: line 4
   :answer_e: line 5
   :correct: a
   :feedback_a: It should loop through the entire array.
   :feedback_b: The value at the outer loop index should be stored in temp.
   :feedback_c: The possible index should be set to the outer loop index before the inner loop executes.
   :feedback_d: Loop while the possible index is greater than 0 and the temp value is less than the value at the possible index minus one.
   :feedback_e: Move the value at possible index minus one to the possible index (move to the right).

   This method should sort the numbers in the passed array into ascending order. But, it does not work. Which of the following lines is wrong?

   .. code-block:: java

      public static void insertionSort(int[] elements)
      {
        for (int j = 1; j < elements.length - 1; j++)                       // line 1
        {
           int temp = elements[j];                                          // line 2
           int possibleIndex = j;                                           // line 3
           while (possibleIndex > 0 && temp < elements[possibleIndex - 1])  // line 4
           {
              elements[possibleIndex] = elements[possibleIndex - 1];        // line 5
              possibleIndex--;
           }
           elements[possibleIndex] = temp;
        }
      }