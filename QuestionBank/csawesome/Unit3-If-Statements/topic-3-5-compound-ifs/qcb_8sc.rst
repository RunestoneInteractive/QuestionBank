.. mchoice:: qcb_8sc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: F
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't use a negative index with substring.
   :correct: b
   :feedback_a: Since x is negative the complex conditional will be false and the second condition won't execute. Remember that with <code>&&</code> both parts of the condition must be true for the complex conditional to be true.  Using a negative substring index won't cause an error since that code will only be executed if x is greater than or equal to zero.
   :feedback_b: Since x is negative the second part of the complex conditional won't even execute so the else will be executed.
   :feedback_c: This would be true if it wasn't using short circuit evaluation, but it is.
   :pct_on_first: 0.76
   :total_students_attempting: 75
   :num_students_correct: 75.0
   :mean_clicks_to_correct: 1.36

   What is printed when the following code executes and x has been set to negative 1?
   
   .. code-block:: java
   
     String message = "help";
     if (x >= 0 && message.substring(x).equals("help") System.out.println("first case");
     else System.out.println("second case");