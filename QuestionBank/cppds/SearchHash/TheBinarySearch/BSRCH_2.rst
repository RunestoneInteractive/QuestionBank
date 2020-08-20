.. mchoice:: BSRCH_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: SearchHash
   :subchapter: TheBinarySearch
   :topics: SearchHash/TheBinarySearch
   :from_source: T
   :correct: d
   :answer_a: 11, 17, 14, 15
   :answer_b: 18, 17, 14, 15
   :answer_c: 14, 12, 17, 15
   :answer_d: 12, 17, 14, 15
   :feedback_a: Looks like you might be guilty of an off-by-one error.  Remember the first position is index 0.
   :feedback_b: Remember binary search starts in the middle and halves the list.
   :feedback_c: Looks like you might be off by one, be careful that you are calculating the midpont using integer arithmetic.
   :feedback_d: Binary search starts at the midpoint and halves the list each time. It is done when the list is empty.
   :pct_on_first: 0.6461538462
   :total_students_attempting: 130
   :num_students_correct: 127
   :mean_clicks_to_correct: 1.4330708661

   Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the recursive binary search algorithm.  Which group of numbers correctly shows the sequence of comparisons used to search for the key 16?