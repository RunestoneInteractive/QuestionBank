.. mchoice:: bisection_search_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter12
   :subchapter: bisection_search
   :topics: Chapter12/bisection_search
   :from_source: T
   :multiple_answers:
   :answer_a: having more than one recursive call
   :answer_b: not including a base case
   :answer_c: writing recursive calls such that the base case is never reached
   :answer_d: having more than one base case
   :correct: b,c
   :feedback_a: Incorrect! You are allowed to make multiple recursive calls inside of a function! You might do this if there is more than one condition.
   :feedback_b: Correct! You always need a base case!
   :feedback_c: Correct! If you never reach the base case, the program will never stop making recursive calls.
   :feedback_d: Incorrect! You are allowed to have multiple base cases. This is often necessary!

   When writing a recursive function, which of the following will result in infinite recursion?