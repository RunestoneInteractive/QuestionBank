.. mchoice:: question4_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Debugging
   :subchapter: RuntimeErrors
   :topics: Debugging/RuntimeErrors
   :from_source: T
   :answer_a: Attempting to divide by 0.
   :answer_b: Forgetting a colon at the end of a statement where one is required.
   :answer_c: Forgetting to divide by 100 when printing a percentage amount.
   :correct: a
   :feedback_a: Python cannot reliably tell if you are trying to divide by 0 until it is executing your program (e.g., you might be asking the user for a value and then dividing by that value—you cannot know what value the user will enter before you run the program).
   :feedback_b: This is a problem with the formal structure of the program.  Python knows where colons are required and can detect when one is missing simply by looking at the code without running it.
   :feedback_c: This will produce the wrong answer, but Python will not consider it an error at all.  The programmer is the one who understands that the answer produced is wrong.
   :practice: T
   :pct_on_first: 0.6615305598
   :total_students_attempting: 1947
   :num_students_correct: 1941.0
   :mean_clicks_to_correct: 1.4585265327

   Which of the following is a run-time error?