.. mchoice:: question_sort_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Sort
   :subchapter: TheMergeSort
   :topics: Sort/TheMergeSort
   :from_source: T
   :correct: b
   :answer_a: [16, 49, 39, 27, 43, 34, 46, 40]
   :answer_b: [21,1]
   :answer_c: [21, 1, 26, 45]
   :answer_d: [21]
   :feedback_a: This is the second half of the list.
   :feedback_b: Yes, mergesort will continue to recursively move toward the beginning of the list until it hits a base case.
   :feedback_c: Remember mergesort doesn't work on the right half of the list until the left half is completely sorted.
   :feedback_d: This is the list after 4 recursive calls
   :pct_on_first: 0.40625
   :total_students_attempting: 64
   :num_students_correct: 63
   :mean_clicks_to_correct: 2.0158730159

   Given the following list of numbers: [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] which answer illustrates the list to be sorted after 3 recursive calls to mergesort?