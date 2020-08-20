.. mchoice:: implicit_variable_access_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: implicit_variable_access
   :topics: Chapter11/implicit_variable_access
   :from_source: T
   :answer_a: Every time you are working with data structures!
   :answer_b: When you implement member functions inside of the structure definition.
   :answer_c: When you implement member functions outside of the structure definition.
   :answer_d: Never! It is bad practice!
   :correct: c
   :feedback_a: Incorrect! The scope resolution operator is not always necessary!
   :feedback_b: Incorrect! When you write member functions inside of the structure definition, you do not need to specify the scope.
   :feedback_c: Correct!  When you write member functions outside of the structure definition, you need to specify the scope, hence the :: operator!
   :feedback_d: Incorrect! The scope resolution operator is good practice when used correctly!
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   When should you use the scope resolution operator ``::``?