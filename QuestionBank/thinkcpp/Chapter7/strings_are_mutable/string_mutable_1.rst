.. mchoice:: string_mutable_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: strings_are_mutable
   :topics: Chapter7/strings_are_mutable
   :from_source: T
   :practice: T
   :answer_a: icd cream
   :answer_b: icedcream
   :answer_c: ice cream
   :answer_d: iced
   :correct: b
   :feedback_a: Remember that indexing begins at 0, not 1.
   :feedback_b: Index 3 was a space and now it is "d".
   :feedback_c: The character at index 3 should be changed to "d".
   :feedback_d: The character at index 3 should be changed to "d", and the rest stays the same.
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   
   What is printed by the following statements?
   
   .. code-block:: cpp
   
      string fav_food = "ice cream";
      fav_food[3] = "d";
      cout << fav_food << endl;