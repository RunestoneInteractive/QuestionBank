.. mchoice:: qcbc_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: F
   :practice: T
   :answer_a: first case
   :answer_b: second case
   :answer_c: You will get a error because you can't divide by zero.
   :correct: b
   :feedback_a: first case will only print if x is greater than 0 and it is not.
   :feedback_b: second case will print if x is less than or equal to zero or if y divided by x is not equal to 3.
   :feedback_c: Since the first condition is false when x is equal to zero the second condition won't execute.  Execution moves to the else.

   What is printed when the following code executes and x has been set to 0 and y to 3?

   .. code-block:: java

     if (x > 0 && (y / x) == 3)
     {
        System.out.println("first case");
     }
     else
     {
        System.out.println("second case");
     }