.. mchoice:: more_recursion_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: morerecursion
   :topics: Chapter5/morerecursion
   :from_source: T
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :correct: d
   :feedback_a: As the programmer, we explicitly call this function one time... but remember, recursive functions call themselves!
   :feedback_b: Not quite! Maybe you were thinking of the two possible branches of the function call.
   :feedback_c: You're close! But what happens when n = 0?
   :feedback_d: The function is called four times total.  Three of those times, the function recurses.  The last time, the function reaches its base case and returns 1.
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   In the example above, how many times was the ``factorial`` function
   called?