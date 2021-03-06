.. mchoice:: qtnt3_15
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: 5
   :answer_b: 7
   :answer_c: 10
   :answer_d: 12
   :answer_e: 128
   :correct: b
   :feedback_a: This is not enough passes to guarantee that a name is not present. 2 ^ 5, is 32, which is not enough elements. Remember that binary search takes log2 (number of elements) passes at most to find an item.
   :feedback_b: 2 ^ 7 is 128, which is greater than 120. 120 passes will guarantee that the name is not present in the list. Binary search takes log2 (number of elements) at most to find an item.
   :feedback_c: Yes, you would know by 10 passes, but there is a better answer. Remember that binary search takes log2 (number of elements) passes at most to find an item.
   :feedback_d: Yes, you would know by 12 passes, but not all 12 passes are required. Remember that binary search takes log2 (number of elements) passes at most to find an item.
   :feedback_e: This would be true if the list was searched using sequential search. Binary search only requires log2 (number of elements) at most to find an item.
   :pct_on_first: 0.4196428571
   :total_students_attempting: 112
   :num_students_correct: 108.0
   :mean_clicks_to_correct: 2.287037037

   
   A list of 120 names has been sorted in alphabetical order. Using a binary search method, what is the minimum number of passes needed to confirm that a name is not in the list?