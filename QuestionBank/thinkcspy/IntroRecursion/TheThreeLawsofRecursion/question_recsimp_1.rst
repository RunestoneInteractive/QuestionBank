.. mchoice:: question_recsimp_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: IntroRecursion
   :subchapter: TheThreeLawsofRecursion
   :topics: IntroRecursion/TheThreeLawsofRecursion
   :from_source: T
   :practice: T
   :correct: c
   :answer_a: 6
   :answer_b: 5
   :answer_c: 4
   :answer_d: 3
   :feedback_a: There are only five numbers on the list, the number of recursive calls will not be greater than the size of the list.
   :feedback_b: The initial call to listsum is not a recursive call.
   :feedback_c: the first recursive call passes the list [4,6,8,10], the second [6,8,10] and so on until [10].
   :feedback_d: This would not be enough calls to cover all the numbers on the list
   :pct_on_first: 0.4937207584
   :total_students_attempting: 4061
   :num_students_correct: 4039.0
   :mean_clicks_to_correct: 1.7011636544

   How many recursive calls are made when computing the sum of the list [2,4,6,8,10]?