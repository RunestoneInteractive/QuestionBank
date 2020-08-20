.. mchoice:: RecursiveQ1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: pythondsConvertinganIntegertoaStringinAnyBase
   :topics: Recursion/pythondsConvertinganIntegertoaStringinAnyBase
   :from_source: T
   :answer_a: A stack, because a recursive function will complete the final function call before any of the other function calls, similar to how a stack has the Last-in-First-out principle.
   :answer_b: A queue, because a recursive function will complete its intial function call before any of the other function calls, similar to how a queue has the First-in-First-out principle.
   :correct: a
   :feedback_a: Correct! a recursive function will complete the final function call first, because the rest of the calls are waiting for the results of the calls they made.
   :feedback_b: Incorrect. Think of it this way, when a function is called and it calls itself, the original function call cannot be completed until the new function call is completed.
   :pct_on_first: 0.75
   :total_students_attempting: 52
   :num_students_correct: 51
   :mean_clicks_to_correct: 1.2549019608

   Is the process of stepping through a recursive function similar to the construct of a stack or a queue?