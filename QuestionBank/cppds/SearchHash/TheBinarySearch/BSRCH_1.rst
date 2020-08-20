.. mchoice:: BSRCH_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: SearchHash
   :subchapter: TheBinarySearch
   :topics: SearchHash/TheBinarySearch
   :from_source: T
   :correct: b
   :answer_a: 11, 5, 8
   :answer_b: 12, 6, 8
   :answer_c: 3, 5, 8
   :answer_d: 18, 12, 8
   :feedback_a: Looks like you might be guilty of an off-by-one error.  Remember the first position is index 0.
   :feedback_b: Binary search starts at the midpoint and halves the list each time.
   :feedback_c: Binary search does not start at the beginning and search sequentially, its starts in the middle and halves the list after each compare.
   :feedback_d: It appears that you are starting from the end and halving the list each time.
   :pct_on_first: 0.3893129771
   :total_students_attempting: 131
   :num_students_correct: 130
   :mean_clicks_to_correct: 1.8230769231

   Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the recursive binary search algorithm.  Which group of numbers correctly shows the sequence of comparisons used to find the key 8.