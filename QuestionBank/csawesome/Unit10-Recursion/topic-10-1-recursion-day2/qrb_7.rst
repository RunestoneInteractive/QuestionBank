.. mchoice:: qrb_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: topic-10-1-recursion-day2
   :topics: Unit10-Recursion/topic-10-1-recursion-day2
   :from_source: T
   :practice: T
   :answer_a: 12
   :answer_b: 81
   :answer_c: 64
   :answer_d: 27
   :answer_e: 243
   :correct: b
   :feedback_a: This would be correct if it added instead of multiplied.
   :feedback_b: This calculates a to nth power.
   :feedback_c: This would be correct if it was 4 to the 3rd instead of 3 to the 4th power.
   :feedback_d: This would be correct if returned 1 instead of a in the base case.
   :feedback_e: This would be correct if it was 3 to the 5th.
   :pct_on_first: 0.5127388535
   :total_students_attempting: 1256
   :num_students_correct: 1252.0
   :mean_clicks_to_correct: 1.9896166134

        Given the method defined below what does the following print: mystery(4,3)?
   
    .. code-block:: java
     :linenos:
   
     public static int mystery(int n, int a)
     {
       if (n == 1) return a;
       return a * mystery(n-1,a);
     }