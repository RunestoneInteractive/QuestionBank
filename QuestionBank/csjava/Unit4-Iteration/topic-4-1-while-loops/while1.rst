.. mchoice:: while1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-1-while-loops
   :topics: Unit4-Iteration/topic-4-1-while-loops
   :from_source: F
   :practice: T
   :answer_a: while (count == 10)
   :answer_b: while (count < 10)
   :answer_c: while (count <= 10)
   :answer_d: while (count > 10)
   :correct: c
   :feedback_a: This would not print out anything because count = 0 at the start of the loop, so it never equals 10.
   :feedback_b: This would print out 0 2 4 6 8. Try it in the Active Code window above.
   :feedback_c: Yes, try it in the Active Code window above.
   :feedback_d: This would not print out anything because count = 0 at the start of the loop, so it is not greater than 10.

   Consider the following code segment. Which of the following can be used as a replacement for the missing loop header so that the loop prints out "0 2 4 6 8 10"?

   .. code-block:: java

        int count = 0;
        /* missing loop header */
        {
            System.out.print(count + " ");
            count += 2;
        }