.. mchoice:: qtnt3_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: [62, 45, 30, 12, 7, 8, 10, 3]
   :answer_b: [30, 12, 8, 7, 62, 45, 10, 3]
   :answer_c: [62, 45, 30, 7, 12, 8, 10, 3]
   :answer_d: [62, 45, 30, 12, 7, 8, 10, 3]
   :answer_e: [12, 8, 30, 7, 62, 45, 10, 3]
   :correct: c
   :feedback_a: This is the fully sorted array after eight passes. Reread the question and try again.
   :feedback_b: This is the result after three passes of insertion sort. Remember that in selection sort, only two values swap positions after every pass.
   :feedback_c: Since 62 is the largest value in the array, it swaps position with the value in index 0 of the array, 12. 45 is the next largest value, and it swaps with 8. 30 is the next largest value, and it swaps with 7. So, after three passes the list contains [62, 45, 30, 7, 12, 8, 10, 3].
   :feedback_d: This is the result after 4 passes of selection sort. Check your steps and try again.
   :feedback_e: This is the result after one merge of merge sort. Remember that in selection sort, only two values change postions at every pass.

   A list of integers containing ``[12, 8, 7, 30, 62, 45, 10, 3]`` is sorted from largest to smallest using a selection sort method. After three passes, what does the list look like?