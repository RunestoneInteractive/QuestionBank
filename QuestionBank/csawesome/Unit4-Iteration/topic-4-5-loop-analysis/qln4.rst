.. mchoice:: qln4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-5-loop-analysis
   :topics: Unit4-Iteration/topic-4-5-loop-analysis
   :from_source: T
   :practice: T
   :answer_a: 15
   :answer_b: 12
   :answer_c: 10
   :answer_d: 8
   :correct: a
   :feedback_a: The outer loop executes 4-0+1=5 times and the inner loop 2-0+1=3, so hi is printed 5*3 = 15 times
   :feedback_b: The outer loop runs 5 times for i = 0, 1, 2, 3, 4.
   :feedback_c: The inner loop runs 3 times for j = 0, 1, 2.
   :feedback_d: The outer loop runs 5 times for i = 0, 1, 2, 3, 4.
   :pct_on_first: 0.4671589584
   :total_students_attempting: 2573
   :num_students_correct: 2540.0
   :mean_clicks_to_correct: 2.0905511811

   Consider the following code segment. How many times is the string "Hi!" printed as a result of executing the code segment?
   
   .. code-block:: java
   
       int i = 0;
       while (i <= 4)
       {
         for (int j = 0; j < 3; j++)
         {
           System.out.println("Hi!");
         }
         i++;
       }