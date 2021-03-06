.. mchoice:: qtnt4_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II only
   :answer_e: I and III only
   :correct: d
   :feedback_a: This loop is correct, but the loop in II is also correct. This method may be completed using a for loop or a while loop.
   :feedback_b: This loop is correct, but the loop in I is also correct. This method may be completed using a for loop or a while loop.
   :feedback_c: This method cannot be completed using a for-each loop. The for-each loop only loops through elements of a collection like a list or array.
   :feedback_d: Both of these loops multiply num by itself exactly ten times.
   :feedback_e: This method cannot be completed using a for-each loop. The format of a for-each loop requires a list or array to be completed.

   You want to write a method that multiplies an integer ``num`` by itself exactly 10 times. Which of the following loops could you use?

   .. code-block:: java

      // I.
      int total = 1;
      for (int i = 0; i < 10; i++)
      {
          total = total * num;
      }

      // II.
      int count = 0;
      int total = 1;

      while (count < 10)
      {
          count++;
          total = total * num;
      }

      // III.
      int total = 1;
      for (int i : 10)
      {
          total = total * num;
      }