.. mchoice:: apcsa-sample5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: T
   :practice: T
   :answer_a: The value is always true.
   :answer_b: The value is always false.
   :answer_c: The value is true when a has the value false, and is false otherwise.
   :answer_d: The value is true when b has the value false, and is false otherwise.
   :answer_e: The value is true when either a or b has the value true, and is false otherwise.
   :correct: b
   :feedback_a: Try simplifying !(b ||a) or consider what happens if a and b are true.
   :feedback_b: Yes, a && !(b || a) = a && !b && !a. Since (a && !a) can never be true, the result will always be false.
   :feedback_c: Try the expression with a = false. Is the result true?
   :feedback_d: Try the expression with b = false with a = true and then try it with a = false. Is the result ever true?
   :feedback_e: Try the expression with a = true. Is the result true?
   :pct_on_first: 0.4221598878
   :total_students_attempting: 3565
   :num_students_correct: 3508.0
   :mean_clicks_to_correct: 2.5553021665

    Which of the following best describes the value of the Boolean expression: a && !(b || a)