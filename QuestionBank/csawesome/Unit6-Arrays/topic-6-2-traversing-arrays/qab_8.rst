.. mchoice:: qab_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :practice: T
   :answer_a: {-40, -30, 4, 16, 32, 66}
   :answer_b: {-40, -30, 4, 8, 16, 32}
   :answer_c: {-20, -15, 2, 16, 32, 66}
   :answer_d: {-20, -15, 2, 8, 16, 33}
   :correct: c
   :feedback_a: This would true if it looped through the whole array.  Does it?
   :feedback_b: This would be true if it looped from the beginning to the middle.  Does it?
   :feedback_c: It loops from the middle to the end doubling each value. Since there are 6 elements it will start at index 3.
   :feedback_d: This would be true if array elements didn't change, but they do.
   :pct_on_first: 0.5403442711
   :total_students_attempting: 3718
   :num_students_correct: 3683.0
   :mean_clicks_to_correct: 1.8083084442

   Given the following values of a and the method doubleLast what will the values of a be after you execute: doubleLast()?
   
   .. code-block:: java
   
      private int[ ] a = {-20, -15, 2, 8, 16, 33};
   
      public void doubleLast()
      {
   
         for (int i = a.length / 2; i < a.length; i++)
         {
            a[i] = a[i] * 2;
         }
      }