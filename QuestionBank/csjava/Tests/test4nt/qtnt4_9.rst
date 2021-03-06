.. mchoice:: qtnt4_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 5! 4! 3! 2! 1! 0!
   :answer_b: 0! 1! 2! 3! 4! 5!
   :answer_c: 0!
   :answer_d: 5!
   :answer_e: This method will result in an infinite loop.
   :correct: c
   :feedback_a: This would be correct if the recursive call contained a return to n + "! " in addition to the call to numList. Notice the recursive call in this problem. Only the value of numList(n - 1) is returned, with nothing else added.
   :feedback_b: This would be correct if the recursive call contained a call to numList AND a return of n + "! ". Notice the recursive call in this problem. Only the value of numList(n - 1) is returned, with nothing else added.
   :feedback_c: The method makes recursive calls until 0 is reached, then "0! " is returned. None of the recursive calls modify the returned response, so only "0! " is returned.
   :feedback_d: Notice the if-statement. When n + "! " is returned, n equals the base case found in the if-statement. This occurs ONLY when n == 0, not 5.
   :feedback_e: An infinite loop will not occur in this method, because of the precondition. After a certain number of calls, n will reach the base case and the method will end.

   The method ``numList`` is shown below. What is returned as a result of ``numList(5)``?

   .. code-block:: java

       /** Precondition: all values of n are greater than 1 **/
       public String numList (int n)
       {
           if (n == 0)
               return n + "! "

           else
               return numList(n - 1);
       }