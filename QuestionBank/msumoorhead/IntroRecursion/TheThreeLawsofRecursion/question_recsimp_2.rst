.. mchoice:: question_recsimp_2
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: IntroRecursion
   :subchapter: TheThreeLawsofRecursion
   :topics: IntroRecursion/TheThreeLawsofRecursion
   :from_source: None
   :correct: d
   :answer_a: n == 0
   :answer_b: n == 1
   :answer_c: n &gt;= 0
   :answer_d: n &lt;= 1
   :feedback_a:  Although this would work there are better and slightly more efficient choices. since fact(1) and fact(0) are the same.
   :feedback_b: A good choice, but what happens if you call fact(0)?
   :feedback_c: This basecase would be true for all numbers greater than zero so fact of any positive number would be 1.
   :feedback_d: Good, this is the most efficient, and even keeps your program from crashing if you try to compute the factorial of a negative number.

   Suppose you are going to write a recusive function to calculate the factorial of a number.  fact(n) returns n * n-1 * n-2 * ... Where the factorial of zero is definded to be 1.  What would be the most appropriate base case?