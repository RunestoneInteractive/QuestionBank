.. mchoice:: question19_1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TestCases
   :subchapter: intro-TestCases
   :topics: TestCases/intro-TestCases
   :from_source: T
   :answer_a: A runtime error will occur
   :answer_b: A message is printed out saying that the test failed.
   :answer_c: x will get the value that y currently has
   :answer_d: Nothing will happen
   :answer_e: A message is printed out saying that the test passed.
   :correct: a
   :feedback_a: The expression ``x==y`` evaluates to ``False``, so a runtime error will occur
   :feedback_b: If the assertion fails, a runtime error will occur
   :feedback_c: ``x==y`` is a Boolean expression, not an assignment statement
   :feedback_d: The expression ``x==y`` evaluates to ``False``
   :feedback_e: When an assertion test passes, no message is printed. In this case, the assertion test fails.
   :practice: T
   :pct_on_first: 0.6426116838
   :total_students_attempting: 291
   :num_students_correct: 286.0
   :mean_clicks_to_correct: 1.6398601399

   When ``assert x==y`` is executed and x and y have different values, what will happen?