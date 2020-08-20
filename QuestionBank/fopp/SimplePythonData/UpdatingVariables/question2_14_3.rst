.. mchoice:: question2_14_3
   :author: bmiller
   :difficulty: 3.3502994012
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: UpdatingVariables
   :topics: SimplePythonData/UpdatingVariables
   :from_source: T
   :multiple_answers: 
   :answer_a: x = x + y
   :answer_b: y += x
   :answer_c: x += x + y
   :answer_d: x += y
   :answer_e: x++ y
   :correct: a,d
   :feedback_a: x is updated to be the old value of x plus the value of y.
   :feedback_b: y is updated to be the old value of y plus the value of x.
   :feedback_c: This updates x to be its old value (because of the +=) plus its old value again (because of the x on the right side) plus the value of y, so it's equivalent to x = x + x + y
   :feedback_d: x is updated to be the old value of x plus the value of y.
   :feedback_e: ++ is not a syntax that means anything in Python.
   :practice: T
   :pct_on_first: 0.4124251497
   :total_students_attempting: 2672
   :num_students_correct: 2561.0
   :mean_clicks_to_correct: 2.9394767669

   Which of the following statements are equivalent?