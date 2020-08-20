.. mchoice:: while_statement_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: the_while_statement
   :topics: Chapter6/the_while_statement
   :from_source: T
   :practice: T
   :answer_a: 4 7
   :answer_b: 5 7
   :answer_c: 7 15
   :correct: c
   :feedback_a: Setting a variable so the loop condition would be false in the middle of the loop body does not keep the variable from actually being set.
   :feedback_b: Setting a variable so the loop condition would be false in the middle of the loop body does not stop execution of statements in the rest of the loop body.
   :feedback_c: After n becomes 5 and the test would be False, but the test does not actually come until after the end of the loop - only then stopping execution of the repetition of the loop.
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.5

   
   What is printed by this code?
   
   .. code-block:: cpp
   
     int n = 1;
     int x = 2;
     while (n < 5) {
       n = n + 1;
       x = x + 1;
       n = n + 2;
       x = x + n;
     }
     cout << n;
     cout << x;