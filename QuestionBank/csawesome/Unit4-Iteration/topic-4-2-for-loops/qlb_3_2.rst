.. mchoice:: qlb_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-2-for-loops
   :topics: Unit4-Iteration/topic-4-2-for-loops
   :from_source: T
   :practice: T
   :answer_a: 3 4 5 6 7 8
   :answer_b: 0 1 2 3 4 5 6 7 8 9
   :answer_c: 1 2 3 4 5 6 7 8 9 10
   :answer_d: 1 3 5 7 9
   :correct: c
   :feedback_a: What is i set to in the initialization area?
   :feedback_b: What is i set to in the initialization area?
   :feedback_c: The value of i starts at 1 and this loop will execute until i equals 11.  The last time through the loop the value of i is 10.
   :feedback_d: This loop changes i by 1 each time in the change area.
   :pct_on_first: 0.8388340159
   :total_students_attempting: 4151
   :num_students_correct: 4129.0
   :mean_clicks_to_correct: 1.262533301

   What does the following code print?
   
   .. code-block:: java
   
     for (int i = 1; i <= 10; i++)
     {
        System.out.print(i + " ");
     }