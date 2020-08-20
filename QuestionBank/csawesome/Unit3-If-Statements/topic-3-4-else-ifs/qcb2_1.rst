.. mchoice:: qcb2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-4-else-ifs
   :topics: Unit3-If-Statements/topic-3-4-else-ifs
   :from_source: F
   :answer_a: x is negative
   :answer_b: x is zero
   :answer_c: x is positive
   :correct: a
   :feedback_a: When x is equal to -5 the condition of x < 0 is true.
   :feedback_b: This will only print if x has been set to 0.  Has it?
   :feedback_c: This will only print if x is greater than zero.  Is it?
   :pct_on_first: 0.8961038961
   :total_students_attempting: 77
   :num_students_correct: 77.0
   :mean_clicks_to_correct: 1.1948051948

   What does the following code print when x has been set to -5?
   
   .. code-block:: java
   
     if (x < 0) System.out.println("x is negative");
     else if (x == 0) System.out.println("x is zero");
     else System.out.println("x is positive");