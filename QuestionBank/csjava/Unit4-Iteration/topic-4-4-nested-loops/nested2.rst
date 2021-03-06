.. mchoice:: nested2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-4-nested-loops
   :topics: Unit4-Iteration/topic-4-4-nested-loops
   :from_source: F
   :practice: T
   :answer_a: A rectangle of 4 rows with 3 star per row.
   :answer_b: A rectangle of 5 rows with 3 stars per row.
   :answer_c: A rectangle of 4 rows with 1 star per row.
   :answer_d: The loops have errors.
   :correct: b
   :feedback_a: This would be true if i was initialized to 1 or ended at 4.
   :feedback_b: Yes, the outer loop runs from 0 up to 5 but not including 5 so there are 5 rows and the inner loop runs from 3 down to 1 so 3 times.
   :feedback_c: The inner loop runs 3 times when j is 3, 2, and then 1, so there are 3 stars per row.
   :feedback_d: Try the code in an Active Code window and you will see that it does run.

   What does the following code print?

   .. code-block:: java

     for (int i = 0; i < 5; i++)
     {
         for (int j = 3; j >= 1; j--)
         {
             System.out.print("*");
         }
         System.out.println();
     }