.. mchoice:: nested1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-4-nested-loops
   :topics: Unit4-Iteration/topic-4-4-nested-loops
   :from_source: T
   :practice: T
   :answer_a: A rectangle of 7 rows with 5 stars per row.
   :answer_b: A rectangle of 7 rows with 4 stars per row.
   :answer_c: A rectangle of 6 rows with 5 stars per row.
   :answer_d: A rectangle of 6 rows with 4 stars per row.
   :correct: c
   :feedback_a: This would be true if i was initialized to 0.
   :feedback_b: This would be true if i was initialized to 0 and the inner loop continued while <code>y < 5</code>.
   :feedback_c: The outer loop runs from 1 up to 7 but not including 7 so there are 6 rows and the inner loop runs 1 to 5 times including 5 so there are 5 columns.
   :feedback_d: This would be true if the inner loop continued while <code>y < 5</code>.
   :pct_on_first: 0.4899854862
   :total_students_attempting: 3445
   :num_students_correct: 3422.0
   :mean_clicks_to_correct: 1.8208649912

   What does the following code print?
   
   .. code-block:: java
   
     for (int i = 1; i < 7; i++)
     {
         for (int y = 1; y <= 5; y++)
         {
             System.out.print("*");
         }
         System.out.println();
     }