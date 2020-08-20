.. mchoice:: qsb_8-new
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-7-string-methods
   :topics: Unit2-Using-Objects/topic-2-7-string-methods
   :from_source: T
   :practice: T
   :answer_a: positive (> 0)
   :answer_b: 0
   :answer_c: negative (< 0)
   :correct: a
   :feedback_a: H is after B in the alphabet so s1 is greater than s2.
   :feedback_b: The method compareTo will only return 0 if the strings have the same characters in the same order.
   :feedback_c: This would be true if it was s2.compareTo(s1)
   :pct_on_first: 0.379338014
   :total_students_attempting: 4985
   :num_students_correct: 4951.0
   :mean_clicks_to_correct: 1.8545748334

   What is the value of answer after the following code executes?
   
   .. code-block:: java
   
     String s1 = "Hi";
     String s2 = "Bye";
     int answer = s1.compareTo(s2);