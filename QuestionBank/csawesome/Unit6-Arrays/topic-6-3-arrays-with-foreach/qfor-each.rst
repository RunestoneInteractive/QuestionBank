.. mchoice:: qfor-each
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-3-arrays-with-foreach
   :topics: Unit6-Arrays/topic-6-3-arrays-with-foreach
   :from_source: T
   :practice: T
   :pct_on_first: 0.3977955912
   :total_students_attempting: 2994
   :num_students_correct: 2956.0
   :mean_clicks_to_correct: 2.1376860622

   What is the output of the following code segment?
   
   .. code-block:: java
   
      int[ ] numbers = {44, 33, 22, 11};
      for (int num : numbers)
      {
          num *= 2;
      }
      for (int num : numbers)
      {
          System.out.print(num + " ");
      }
   
   - 44 33 22 11
   
     + The array is unchanged because the foreach loop cannot modify the array elements.
   
   - 46 35 24 13
   
     - Remember that the foreach loop cannot modify the array elements, but it also uses multiplication, not addition.
   
   - 88 66 44 22
   
     - Remember that the foreach loop cannot modify the array elements. Only the variable num will be doubled, not the original array values.
   
   - The code will not compile.
   
     - This code will compile.