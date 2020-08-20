.. mchoice:: qle_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: Exercises
   :topics: Unit4-Iteration/Exercises
   :from_source: T
   :practice: T
   :answer_a: 9
   :answer_b: 7
   :answer_c: 6
   :answer_d: 10
   :correct: c
   :feedback_a: This would be true if i started at 0.
   :feedback_b: Note that it stops when i is 9.
   :feedback_c: Since i starts at 3 and the last time through the loop it is 8 the loop executes 8 - 3 + 1 times = 6 times.
   :feedback_d: This would be true if i started at 0 and ended when i was 10.  Does it?
   :pct_on_first: 0.7268399854
   :total_students_attempting: 2731
   :num_students_correct: 2703.0
   :mean_clicks_to_correct: 1.4195338513

   How many times does the following method print a ``*``?
   
   .. code-block:: java
   
     for (int i = 3; i < 9; i++)
     {
        System.out.print("*");
     }