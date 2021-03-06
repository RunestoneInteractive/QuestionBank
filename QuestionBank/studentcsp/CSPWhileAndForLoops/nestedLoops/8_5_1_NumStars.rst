.. mchoice:: 8_5_1_NumStars
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWhileAndForLoops
   :subchapter: nestedLoops
   :topics: CSPWhileAndForLoops/nestedLoops
   :from_source: T
   :practice: T
   :answer_a: 6
   :answer_b: 9
   :answer_c: 12
   :answer_d: 16
   :answer_e: 20
   :correct: c
   :feedback_a: Remember that the range function will include the start value and all the numbers up to one less than the end value.  So the outer loop will execute 3 times ([0,1,2]).
   :feedback_b: This would be true if they were both range(0,3).  Is that correct?
   :feedback_c: The number of times a nested loop executes is the number of times the outer loop executes (3) times the number of the times the inner loop executes (4) so that is 3 * 4 = 12.
   :feedback_d: This would be true if both were range(0,4).  Is that right?
   :feedback_e: This would be true if the range returned all the numbers from start to end, but it does not.

   How many times will this loop print a ``*``?

   ::

       for x in range(0,3):
           for y in range(0,4):
               print('*')