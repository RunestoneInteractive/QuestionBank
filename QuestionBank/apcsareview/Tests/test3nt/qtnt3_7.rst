.. mchoice:: qtnt3_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and III only
   :answer_e: I, II, and III
   :correct: e
   :feedback_a: I is correct, but II and III are correct as well. This task can be accomplished by using a for loop or a while loop.
   :feedback_b: II is correct, but I and III are correct as well. This task can be accomplished by using a for loop or a while loop.
   :feedback_c: III is correct, but I and II are correct as well. Even though i increments by 1 after each passing of the loop in I and II, i * 10 is printed.
   :feedback_d: I and III are correct, but II is correct as well. This task can be accomplished using a for loop or a while loop.
   :feedback_e: Each of these loops will print out multiples of 10 from 0 to 100, starting at 0 and ending at 10.

   Which of these loops will print multiples of 10, from 0 to 100 inclusive?

   .. code-block:: java

      I. for (int i = 0; i < 11; i++)
         {
            System.out.print(i * 10 + " ");
         }

      II. int i = 0;

          while (i <= 10)
          {
             System.out.print(i * 10 + " ");
             i++;
          }

      III. for (int i = 0; i <= 100; i += 10)
           {
              System.out.print(i + " ");
           }