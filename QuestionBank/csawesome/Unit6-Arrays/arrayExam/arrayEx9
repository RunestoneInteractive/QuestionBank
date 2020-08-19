.. mchoice:: arrayEx9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: arrayExam
   :topics: Unit6-Arrays/arrayExam
   :from_source: T
   :practice: T
   :answer_a: A
   :answer_b: B
   :answer_c: C
   :answer_d: D
   :correct: b
   :feedback_a: This increments a2 before copying the value into array2 and so puts it in the wrong place.
   :feedback_b: This will copy all the even values in array1 to array2 and put them in the same position as they were in array1.
   :feedback_c: This will cause an out of bounds error.
   :feedback_d: This increments a2 before copying the value into array2 and so puts it in the wrong place.
   :pct_on_first: 0.5444234405
   :total_students_attempting: 1058
   :num_students_correct: 699.0
   :mean_clicks_to_correct: 1.2718168813

   Which of the following correctly copies all the even numbers from ``array1`` to ``array2`` in the same order as they are in ``array1`` without any errors?  Assume that ``array2`` is large enough for all the copied values.
   
   .. code-block:: java
   
      A.
      int a2 = 0;
      for (int a1=0 ; a1 < array1.length ; a1++)
      {
         // if array1[a1] is even
         if (array1[a1] % 2 == 0)
         {
            // array1[a1] is even,
            // so copy it
            a2++;
            array2[a2] = array1[a1];
         }
      }
   
      B.
      int a2 = 0;
      for (int a1=0 ; a1 < array1.length ; a1++)
      {
         // if array1[a1] is even
         if (array1[a1] % 2 == 0)
         {
            // array1[a1] is even,
            // so copy it
            array2[a2] = array1[a1];
            a2++;
         }
      }
   
      C.
      int a2 = 0;
      for ( int a1=0 ; a1 <= array1.length ; a1++)
      {
         // if array1[a1] is even
         if (array1[a1] % 2 == 0)
         {
            // array1[a1] is even,
            // so copy it
            array2[a2] = array1[a1];
            a2++;
         }
      }
   
      D.
      int a2 = 0;
      for (int a1=0 ; a1 <= array1.length ; a1++)
      {
         // if array1[a1] is even
         if (array1[a1] % 2 == 0)
         {
            // array1[a1] is even,
            // so copy it
            a2++;
            array2[a2] = array1[a1];
         }
      }