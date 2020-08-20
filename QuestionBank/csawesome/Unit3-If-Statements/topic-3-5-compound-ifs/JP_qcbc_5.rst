.. mchoice:: JP_qcbc_5
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: F
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't divide by zero.
   :correct: b
   :feedback_a: first case will only print if x is greater than 0 and it is not.
   :feedback_b: second case will print if x is less than or equal to zero or if y divided by x is not equal to 3.
   :feedback_c: Since the first condition is false when x is equal to zero the second condition won't execute.  Execution moves to the else.
   :pct_on_first: 0.6346153846
   :total_students_attempting: 52
   :num_students_correct: 48.0
   :mean_clicks_to_correct: 1.3541666667

   What is printed when the following code executes and x has been set to 0 and y to -7?
   
   .. code-block:: java
   
     if (x > 0 && (y / x) == 3.0)
     {
        System.out.println("first case");
     }
     else
     {
        System.out.println("second case");
     }