.. mchoice:: question_recsimp_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: TheThreeLawsofRecursion
   :topics: Recursion/TheThreeLawsofRecursion
   :from_source: T
   :answer_c: If a recursive function didn't have a base case, then the function would continue to make recursive calls creating an infinite loop.
   :answer_b: If a recursive function didn't have a base case, then the function would return an undesired outcome.
   :answer_a: If a recursive function didn't have a base case, then the function would end too early.
   :answer_d: If a recursive function didn't have a base case, then the function would not be able to ever make recursive calls in the first place.
   :correct: c
   :feedback_c: Correct! a base case is needed to end the continuous recursive calls, so that the program doesn't get stuck in a never ending loop.
   :feedback_b: Incorrect. In fact, the program wouldn't return anything.
   :feedback_a: Incorrect. The complete opposite would happen instead.
   :feedback_d: Incorrect. Recursive calls will continue to be called even without a base case.
   :pct_on_first: 0.6588235294
   :total_students_attempting: 85
   :num_students_correct: 85
   :mean_clicks_to_correct: 1.4823529412

   Why is a base case needed in a recursive function?