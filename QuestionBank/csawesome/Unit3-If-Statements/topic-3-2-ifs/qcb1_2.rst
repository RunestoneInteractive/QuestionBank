.. mchoice:: qcb1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :practice: T
   :answer_a: 3
   :answer_b: 6
   :answer_c: 0
   :answer_d: 4
   :answer_e: The code will not compile
   :correct: c
   :feedback_a: x is changed by the if statements.
   :feedback_b: What happens when x is greater than 2 and then greater than 4? Do both if statements.
   :feedback_c: If x is greater than 2, it's always doubled, and then that result is always greater than 4, so it's set to 0 in the second if statement.
   :feedback_d: x is changed by the if statements.
   :feedback_e: This code will compile.
   :pct_on_first: 0.3751849503
   :total_students_attempting: 4731
   :num_students_correct: 4690.0
   :mean_clicks_to_correct: 2.1228144989

   Consider the following code segment. What is printed as a result of executing the code segment?
   
   .. code-block:: java
   
     int x = 3;
     if (x > 2)
     {
         x = x * 2;
     }
     if (x > 4)
     {
        x = 0;
     }
     System.out.print(x);