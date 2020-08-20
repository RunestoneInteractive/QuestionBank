.. mchoice:: qce_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: Exercises
   :topics: Unit3-If-Statements/Exercises
   :from_source: T
   :practice: T
   :answer_a: x is negative
   :answer_b: x is zero
   :answer_c: x is positive
   :correct: c
   :feedback_a: This will only print if x has been set to a number less than zero. Has it?
   :feedback_b: This will only print if x has been set to 0.  Has it?
   :feedback_c: The first condition is false and x is not equal to zero so the else will execute.
   :pct_on_first: 0.8151440834
   :total_students_attempting: 3262
   :num_students_correct: 3245.0
   :mean_clicks_to_correct: 1.2739599384

   What does the following code print when x has been set to 187?
   
   .. code-block:: java
   
     if (x < 0)
     {
        System.out.println("x is negative");
     }
     else if (x == 0)
     {
         System.out.println("x is zero");
     }
     else
     {
         System.out.println("x is positive");
     }