.. mchoice:: qln_6_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-5-loop-analysis
   :topics: Unit4-Iteration/topic-4-5-loop-analysis
   :from_source: F
   :practice: T
   :answer_a: A rectangle of 9 rows and 5 stars per row.
   :answer_b: A rectangle of 6 rows and 6 stars per row.
   :answer_c: A rectangle of 7 rows and 5 stars per row.
   :answer_d: A rectangle of 7 rows and 6 stars per row.
   :correct: d
   :feedback_a: Did you notice what i was initialized to?
   :feedback_b: It would print 6 rows if it was <code>i < 9</code>.
   :feedback_c: It would print 5 stars per row if it was <code>j > 1</code>.
   :feedback_d: The outer loop executes 9 - 3 + 1 = 7 times and the inner 6 - 1 + 1 = 6 times.

   What does the following print?

   .. code-block:: java

     for (int i = 3; i <= 9; i++)
     {
        for (int j = 6; j > 0; j--)
        {
            System.out.print("*");
        }
        System.out.println();
     }