.. mchoice:: qlb_3_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-2-for-loops
   :topics: Unit4-Iteration/topic-4-2-for-loops
   :from_source: T
   :practice: T
   :answer_a: 3 4 5 6 7 8
   :answer_b: 0 1 2 3 4 5 6 7 8
   :answer_c: 8 8 8 8 8
   :answer_d: 3 4 5 6 7
   :correct: d
   :feedback_a: This loop starts with i equal to 3 but ends when i is equal to 8.
   :feedback_b: What is i set to in the initialization area?
   :feedback_c: This would be true if the for loop was missing the change part <code>(int i = 3; i < 8; )</code> but it does increment i in the change part <code>(int i = 3; i < 8; i++)</code>.
   :feedback_d: The value of i is set to 3 before the loop executes and the loop stops when i is equal to 8.  So the last time through the loop i is equal to 7.
   :pct_on_first: 0.6663475347
   :total_students_attempting: 4178
   :num_students_correct: 4151.0
   :mean_clicks_to_correct: 1.4986750181

   What does the following code print?
   
   .. code-block:: java
   
     for (int i = 3; i < 8; i++)
     {
        System.out.print(i + " ");
     }