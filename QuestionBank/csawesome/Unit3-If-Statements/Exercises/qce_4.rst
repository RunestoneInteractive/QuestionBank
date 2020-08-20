.. mchoice:: qce_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: Exercises
   :topics: Unit3-If-Statements/Exercises
   :from_source: T
   :practice: T
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't divide by zero.
   :correct: c
   :feedback_a: This will print if either of the two conditions are true.  The first isn't true but the second will cause an error.
   :feedback_b: This will print if both of the conditions are false.  But, an error will occur when testing the second condition.
   :feedback_c: The first condition will be false so the second one will be executed and lead to an error since you can't divide by zero.
   :pct_on_first: 0.533616188
   :total_students_attempting: 3064
   :num_students_correct: 3036.0
   :mean_clicks_to_correct: 1.65085639

   What is printed when the following code executes and x has been set to zero and y is set to 3?
   
   .. code-block:: java
   
     if (x > 0 || (y / x) == 3)
        System.out.println("first case");
     else
        System.out.println("second case");