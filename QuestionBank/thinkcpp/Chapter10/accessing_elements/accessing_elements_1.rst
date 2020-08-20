.. mchoice:: accessing_elements_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: accessing_elements
   :topics: Chapter10/accessing_elements
   :from_source: T
   :multiple_answers: 
   :answer_a: vec[3] = vec[3]++;
   :answer_b: vec(3) = vec(3) + 1;
   :answer_c: vec[2] = vec[2]++;
   :answer_d: vec(2) = vec(2)++;
   :answer_e: vec[2] = vec[2] + 1;
   :correct: c,e
   :feedback_a: Incorrect! This is actually incrementing the 4th element of **vec**, since vectors are zero indexed.
   :feedback_b: Incorrect! This is not proper syntax.
   :feedback_c: Correct!
   :feedback_d: Incorrect! This is not proper syntax.
   :feedback_e: Correct!
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 2.0

   How would you increment the third element of ``vector<int> vec`` by one?