.. mchoice:: 8_4_1_Square_Root_Q1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPWhileAndForLoops
  :subchapter: while
  :topics: CSPWhileAndForLoops/while
  :from_source: T
  :answer_a: No error, since we compute it inside the loop.
  :answer_b: We would get an error.
  :answer_c: We need the one before the while loop, but not the one afterward.
  :correct: b
  :feedback_a: We have to compute it before, or abs(target-guessSquared) > 0.01 would be an error.
  :feedback_b: A variable has to be declared (created) before it is used.
  :feedback_c: We need both.  The one before sets up the test.  The one inside the loop lets us update guessSquared.
  :pct_on_first: 0.6963350785
  :total_students_attempting: 1146
  :num_students_correct: 1141.0
  :mean_clicks_to_correct: 1.3987730061

   What would happen if we didn't compute ``guessSquared`` before the ``while`` loop?