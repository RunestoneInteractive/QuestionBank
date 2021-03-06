.. mchoice:: qtnt4_19
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
   :feedback_a: This is correct, but there is another answer that is also correct.
   :feedback_b: This is correct, but there is another answer that is also correct.
   :feedback_c: The for-each loop would not compile.  The variable num is not an array or list.
   :feedback_d: Both I and II print out the value of num and then decrement it by 1.
   :feedback_e: The for-each loop would not compile.  The variable num is not an array or list.

   You are trying to write the ``countDown`` method. The ``countDown`` method takes a parameter ``num`` and decrements it by 1, printing every time until ``num`` equals 0. Which of the following loops will make the ``countDown`` method compile and work as intended?

   .. code-block:: java

     // I.
     for (int i = num; i > 0; i--)
     {
         System.out.print (i + " ");
     }

     // II.
     while (num > 0)
     {
         System.out.print (num + " ");
         num --;
     }

     /// III.
     for (int i : num)
     {
         System.out.print(i + " ");
         i --;
     }