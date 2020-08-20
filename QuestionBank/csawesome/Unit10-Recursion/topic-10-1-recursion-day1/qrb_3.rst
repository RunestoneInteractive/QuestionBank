.. mchoice:: qrb_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: topic-10-1-recursion-day1
   :topics: Unit10-Recursion/topic-10-1-recursion-day1
   :from_source: T
   :practice: T
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :correct: b
   :feedback_a: Look again.  What is the value of n when this method returns a value, without doing a recursive call?
   :feedback_b: This method stops calling itself when n equals 1 (line 3).
   :feedback_c: Look for a return with a number after it.  When is this code executed?
   :pct_on_first: 0.859947644
   :total_students_attempting: 1528
   :num_students_correct: 1527.0
   :mean_clicks_to_correct: 1.1833660773

   What is the value of n when this method stops calling itself (when it reaches the base case)?
   
    .. code-block:: java
      :linenos:
   
      public static int product(int n)
      {
         if(n == 1)
            return 1;
         else
            return n * product(n - 2);
      }