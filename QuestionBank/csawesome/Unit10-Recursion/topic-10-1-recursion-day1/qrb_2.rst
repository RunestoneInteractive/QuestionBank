.. mchoice:: qrb_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: topic-10-1-recursion-day1
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :practice: T
   :answer_a: Yes
   :answer_b: No
   :correct: a
   :feedback_a: Yes, any method that contains at least one call to the same method is recursive.
   :feedback_b: Look again.  Check if the method contains a call to itself.
   :pct_on_first: 0.86125
   :total_students_attempting: 1600
   :num_students_correct: 1599.0
   :mean_clicks_to_correct: 1.1444652908

   Is the following method recursive?
   
    .. code-block:: java
      :linenos:
   
      public static int mystery2(int x)
      {
         if (x == 1) return 1;
         else return x + mystery2(x-1);
      }