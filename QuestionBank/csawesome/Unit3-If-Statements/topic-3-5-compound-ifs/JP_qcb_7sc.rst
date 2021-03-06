.. mchoice:: JP_qcb_7sc
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
   :correct: a
   :feedback_a: Since x is equal to zero the first expression in the complex conditional will be true and the (y / x) == 3 won't be evaluated, so it won't cause a divide by zero error.  It will print "first case".
   :feedback_b: Since x is equal to zero the first part of the complex conditional is true so it will print first case.
   :feedback_c: You won't get an error because of short circuit evaluation.  The (y / x) == 3 won't be evaluated since the first expression is true and an or is used.
   :pct_on_first: 0.6964285714
   :total_students_attempting: 56
   :num_students_correct: 55.0
   :mean_clicks_to_correct: 1.4181818182

   What is printed when the following code executes and x has been set to zero and y is set to 3?
   
   .. code-block:: java
   
     if (x == 0 || (y / x) == 3)
     {
        System.out.println("first case");
     }
     else
     {
        System.out.println("second case");
     }