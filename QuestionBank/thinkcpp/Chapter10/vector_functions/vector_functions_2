.. parsonsprob:: vector_functions_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: vector_functions
   :topics: Chapter10/vector_functions
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 7.0

   Construct the ``make_even`` function that loops through vec, adds 1 to any elements
   that are odd, and returns the new vector.
   -----
   vector&#60;int&#62; make_even(vector&#60;int&#62; vec) {
   =====
   void make_even(vector&#60;int&#62; vec) {                         #paired
   =====
      for (size_t i = 0; i &#60; vec.size(); i++) {
   =====
      for (int i = 0; i &#60; vec.size(); i++) {                         #paired
   =====
         if (vec[i] % 2 == 1) {
   =====
         if (i % 2 == 1) {                         #paired
   =====
            vec[i] += 1;
         }
   =====
            i += 1;                         #paired
         }
   =====
         else {                         #distractor
            vec[i] -= 1;
         }
   =====
      return vec;
   =====
      }
   }