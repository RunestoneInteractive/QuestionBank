.. mchoice:: qtnt4_17
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: 8
   :answer_b: 11
   :answer_c: 20
   :answer_d: 100
   :answer_e: 2000
   :correct: b
   :feedback_a: 2 ^ 9 is 512, which is not enough elements to cover every element in the database. Remember that binary search requires log2 (number of elements) iterations to perform.
   :feedback_b: 2 ^ 11 is 2024. 11 iterations is more than enough to find the value or guarantee that it is not in the database. Binary search takes log2 (number of elements) iterations to perform.
   :feedback_c: The value will be found in 20 iterations, but a smaller number of iterations could be used.
   :feedback_d: The value will be found in 20 iterations, but a smaller number of iterations could be used. Remember that binary search requires log2 (number of elements) iterations to perform correctly.
   :feedback_e: This would be true if we used a sequential search algorithm. However, binary search only needs log2 (number of elements) iterations.
   :pct_on_first: 0.4947368421
   :total_students_attempting: 95
   :num_students_correct: 93.0
   :mean_clicks_to_correct: 2.1505376344

   A database containing 2,000 sorted integers must be searched using a binary search algorithm. What is the maximum number of iterations of the binary search method that   must occur in order to find a specified value or guarantee that it is not in the database?