.. mchoice:: qaeasy_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: Exercises
   :topics: Unit6-Arrays/Exercises
   :from_source: T
   :practice: T
   :answer_a: 17.5
   :answer_b: 30.0
   :answer_c: 130
   :answer_d: 32
   :answer_e: 32.5
   :correct: e
   :feedback_a: This would be true if the loop stopped at <code>arr.length - 1</code>.
   :feedback_b: This would be true if the loop started at 1 instead of 0.
   :feedback_c: This would be true if it returned <code>output</code> rather than <code>output / arr.length</code>
   :feedback_d: This would be true if <code>output</code> was declared to be an int rather than a double.
   :feedback_e: This sums all the values in the array and then returns the sum divided by the number of items in the array.  This is the average.
   :pct_on_first: 0.4729788154
   :total_students_attempting: 2313
   :num_students_correct: 2282.0
   :mean_clicks_to_correct: 2.0249780894

   What is returned from ``mystery`` when it is passed ``{10, 30, 30, 60}``?
   
   .. code-block:: java
   
      public static double mystery(int[] arr)
      {
         double output = 0;
         for (int i = 0; i < arr.length; i++)
         {
            output = output + arr[i];
         }
         return output / arr.length;
      }