.. mchoice:: question_recsimp_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: Recursion
   :subchapter: TheThreeLawsofRecursion
   :topics: Recursion/TheThreeLawsofRecursion
   :from_source: T
   :correct: d
   :answer_a: n == 0
   :answer_b: n == 1
   :answer_c: n &gt;= 0
   :answer_d: n &lt;= 1
   :feedback_a: Although this would work there are better and slightly more efficient choices. since fact(1) and fact(0) are the same.
   :feedback_b: A good choice, but what happens if you call fact(0)?
   :feedback_c: This basecase would be true for all numbers greater than zero so fact of any positive number would be 1.
   :feedback_d: Good, this is the most efficient, and even keeps your program from crashing if you try to compute the factorial of a negative number.
   :pct_on_first: 0.0909090909
   :total_students_attempting: 11
   :num_students_correct: 11
   :mean_clicks_to_correct: 2.9090909091

   Suppose you are going to write a recusive function to calculate the factorial of a number.  fact(n) returns n * n-1 * n-2 * ... Where the factorial of zero is defined to be 1.  What would be the most appropriate base case?