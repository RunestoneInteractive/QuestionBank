.. mchoice:: qtnt1_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: k
   :answer_b: k + 1
   :answer_c: k - 1
   :answer_d: 1
   :answer_e: 0
   :correct: b
   :feedback_a: This would be the case if i had the initial value 1 and arr[i] < someValue would be true for all i values.
   :feedback_b: If arr[i] < someValue for all i from 0 to k, HELLO will be printed on each iteration of the for loop. The number of times a loop executes is the biggest value in the loop - the smallest value in the loop + 1 (k - 0 + 1 is k + 1).
   :feedback_c: This would be the case if i had the initial value 2 and arr[i] < someValue would be true for all i values.
   :feedback_d: This would be the case if only one element in the array would fulfill the condition that arr[i] < someValue.
   :feedback_e: This is the minimum number of times that HELLO could be executed.

   Consider the following code. What is the maximum amount of times that ``HELLO`` could possibly be printed?

   .. code-block:: java

      for (int i = 0; i <= k; i++)
      {
         if (arr[i] < someValue)
         {
           System.out.print("HELLO")
         }
      }