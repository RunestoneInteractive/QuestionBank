.. mchoice:: logical_op_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: logicaloperators
   :topics: Chapter5/logicaloperators
   :from_source: T
   :multiple_answers: 
   :answer_a: if (x > 0 && x < 10) {...
   :answer_b: if (x > 0 || x < 10) {...
   :answer_c: if (x > 0 ! x < 10) {...
   :answer_d: if ( !(x < 0) && !(x > 10) ) {...
   :answer_e: if ( !(x <= 0) && !(x >= 10) ) {...
   :correct: a,e
   :feedback_a: This is exactly what the nested conditionals are saying.
   :feedback_b: || represents "or", but we need both sides of the conditional to be true.
   :feedback_c: The ! operator cannot be used to compare two sides of a conditional.
   :feedback_d: If x = 0 or if x = 10, this expression will return true when it shouldn't.
   :feedback_e: If it IS NOT what we don't want, then it IS what we want!
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.0

   Multiple Response: How could you re-write the following code using a single conditional?
   
   ::
   
      if (x > 0) {
        if (x < 10) {
          cout << "x is a positive single digit" << endl;
        }
      }