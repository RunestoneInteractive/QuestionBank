.. mchoice:: qce_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: Exercises
   :topics: Unit3-If-Statements/Exercises
   :from_source: F
   :practice: T
   :answer_a: first case
   :answer_b: second case
   :correct: b
   :feedback_a: This will print if x is greater than or equal 3 and y is less than or equal 2.  In this case x is greater than 3 so the first condition is true, but the second condition is false.
   :feedback_b: This will print if x is less than 3 or y is greater than 2.

   What is printed when the following code executes and x equals 4 and y equals 3?

   .. code-block:: java

     if (!(x < 3 || y > 2))
        System.out.println("first case");
     else
        System.out.println("second case");