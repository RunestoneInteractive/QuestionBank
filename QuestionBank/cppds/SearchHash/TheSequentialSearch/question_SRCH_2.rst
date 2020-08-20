.. mchoice:: question_SRCH_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: SearchHash
   :subchapter: TheSequentialSearch
   :topics: SearchHash/TheSequentialSearch
   :from_source: T
   :correct: c
   :answer_a: 10
   :answer_b: 5
   :answer_c: 7
   :answer_d: 6
   :feedback_a: You do not need to search the entire list, since it is ordered you can stop searching when you have compared with a value larger than the key.
   :feedback_b: Since 11 is less than the key value 13 you need to keep searching.
   :feedback_c: Since 14 is greater than the key value 13 you can stop.
   :feedback_d: Because 12 is less than the key value 13 you need to keep going.
   :pct_on_first: 0.4545454545
   :total_students_attempting: 132
   :num_students_correct: 126
   :mean_clicks_to_correct: 1.8015873016

   Suppose you are doing a sequential search using a program that is enhanced to handle ordered lists more efficiently. When passing the list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] as a parameter, how many comparisons would you need to do in order to find the key 13?