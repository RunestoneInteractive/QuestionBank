.. mchoice:: qa2ldb_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: topic-8-2-2D-array-loops-Day1
   :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day1
   :from_source: T
   :practice: T
   :answer_a: nums[3][2]
   :answer_b: nums[2][3]
   :answer_c: nums[2][1]
   :answer_d: nums[1][2]
   :correct: c
   :feedback_a: This would be true if array indices started with 1 but they start with 0.
   :feedback_b: This would be true if array indicies started with 1 and the column was specified first.  However, array indices start at 0 and the row is given first in row-major order.
   :feedback_c: Array indices start with 0 so the third row has an index of 2 and the second column has an index of 1.
   :feedback_d: This would be true if the column index was first, but in row-major order the row index is first.
   :pct_on_first: 0.7453662842
   :total_students_attempting: 2266
   :num_students_correct: 2248.0
   :mean_clicks_to_correct: 1.4021352313

   Which of the following would I use to get the value in the third row and second column from a 2D array called ``nums``?