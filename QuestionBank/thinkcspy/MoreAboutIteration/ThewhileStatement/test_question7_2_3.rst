.. mchoice:: test_question7_2_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: ThewhileStatement
   :topics: MoreAboutIteration/ThewhileStatement
   :from_source: T
   :practice: T
   :answer_a: 4 7
   :answer_b: 5 7
   :answer_c: 7 15
   :correct: c
   :feedback_a: Setting a variable so the loop condition would be false in the middle of the loop body does not keep the variable from actually being set.
   :feedback_b: Setting a variable so the loop condition would be false in the middle of the loop body does not stop execution of statements in the rest of the loop body.
   :feedback_c: After n becomes 5 and the test would be False, but the test does not actually come until after the end of the loop - only then stopping execution of the repetition of the loop.
   :pct_on_first: 0.4166469241
   :total_students_attempting: 12663
   :num_students_correct: 12591.0
   :mean_clicks_to_correct: 1.9394805814

   
   What is printed by this code?
   
   .. code-block:: python
   
     n = 1
     x = 2
     while n < 5:
         n = n + 1
         x = x + 1
         n = n + 2
         x = x + n
     print(n, x)