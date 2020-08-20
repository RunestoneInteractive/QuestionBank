.. mchoice:: qrb_5-new
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: topic-10-1-recursion-day1
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :practice: T
   :answer_a: yes
   :answer_b: no
   :correct: b
   :feedback_a: Where is the call to the same method?
   :feedback_b: There is no call to the same method, so it is not recursive. This uses iteration instead.
   :pct_on_first: 0.8694792353
   :total_students_attempting: 1517
   :num_students_correct: 1513.0
   :mean_clicks_to_correct: 1.1341705221

   Is the following method recursive?
   
    .. code-block:: java
      :linenos:
   
      public static int bunnyEars(int bunnies)
      {
         int total = 0;
         for (int i = 0; i < bunnies; i++)
         {
            total = total + 2;
         }
         return total;
      }