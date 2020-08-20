.. mchoice:: question_recsimp_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cppds
   :chapter: Recursion
   :subchapter: TheThreeLawsofRecursion
   :topics: Recursion/TheThreeLawsofRecursion
   :from_source: T
   :correct: c
   :answer_a: 6
   :answer_b: 5
   :answer_c: 4
   :answer_d: 3
   :feedback_a: There are only five numbers on the vector, the number of recursive calls will not be greater than the size of the vector.
   :feedback_b: The initial call to vectsum is not a recursive call.
   :feedback_c: the first recursive call passes the vector {4,6,8,10}, the second {6,8,10} and so on until [10].
   :feedback_d: This would not be enough calls to cover all the numbers on the vector
   :pct_on_first: 0.4875
   :total_students_attempting: 80
   :num_students_correct: 80
   :mean_clicks_to_correct: 1.925

   How many recursive calls are made when computing the sum of the vector {2,4,6,8,10}?