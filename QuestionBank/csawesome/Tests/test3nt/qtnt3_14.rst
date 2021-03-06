.. mchoice:: qtnt3_14
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: (int) (Math.random() * 25) * 1
   :answer_b: (int) (Math.random() + 1) * 25
   :answer_c: (int) (Math.random() + 25) * 1
   :answer_d: (int) (Math.random()) * 25 + 1
   :answer_e: (int) (Math.random() * 25) + 1
   :correct: e
   :feedback_a: This returns a value between 0 and 24, not 1 and 25. This would be correct if the last part of the expression had + 1 instead of * 1.
   :feedback_b: This always returns 25. Math.random() + 1 becomes 1 when it is cast to an integer, and 1 * 25 equals 25.
   :feedback_c: This always returns 25. Math.random() produces a number between 0 and 1, so when it is added to 25 and cast as an integer, the number always becomes 25.
   :feedback_d: This always returns 1. Math.random() produces a value between 0 and 1, so casting Math.random() to an int results in 0. 0 * 25 remains 0, and 0 + 1 equals 1.
   :feedback_e: Math.random() * 25 finds a random double value between 0 and 24.9999. This is cast to an integer, and 1 is added so the range becomes 1 to 25.
   :pct_on_first: 0.5702479339
   :total_students_attempting: 121
   :num_students_correct: 117.0
   :mean_clicks_to_correct: 1.7948717949

   You need to find a random integer in the range 1 to 25, inclusive. Which of the following always returns a value that satisfies this condition?