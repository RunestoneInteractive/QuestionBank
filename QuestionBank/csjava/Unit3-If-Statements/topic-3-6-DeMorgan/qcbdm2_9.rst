.. mchoice:: qcbdm2_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: F
   :practice: T
   :answer_a: first case
   :answer_b: second case
   :correct: a
   :feedback_a: This will be printed if x is greater than or equal to 3 or y is less than or equal to 2.  In this case x is greater than 3 so the first condition is true.
   :feedback_b: This will be printed if x is less than 3 and y is greater than 2.

   What is printed when the following code executes and x equals 4 and y equals 3?

   .. code-block:: java

     int x = 4, y = 3;
     if (!(x < 3 && y > 2))
     {
        System.out.println("first case");
     }
     else
     {
        System.out.println("second case");
     }