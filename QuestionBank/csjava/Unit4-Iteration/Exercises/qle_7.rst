.. mchoice:: qle_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: Exercises
   :topics: Unit4-Iteration/Exercises
   :from_source: F
   :practice: T
   :answer_a: 4
   :answer_b: 5
   :answer_c: 6
   :correct: b
   :feedback_a: This would be true if x started at 1 instead of 0.
   :feedback_b: The loop starts with x = 0 and ends when it reaches 5 so 5 - 0 = 5.
   :feedback_c: This would be true if the condition was x <= 5 instead of x = 5.

   How many times does the following method print a ``*``?

   .. code-block:: java

     for (int x = 0; x < 5; x++)
     {
        System.out.print("*");
     }