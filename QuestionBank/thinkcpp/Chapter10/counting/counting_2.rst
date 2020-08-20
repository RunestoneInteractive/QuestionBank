.. parsonsprob:: counting_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: counting
   :topics: Chapter10/counting
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 6.0

   Construct a block of code that counts how many numbers are between lowerbound and upperbound inclusive.
   -----
   int just_right(const vector<int>& vec, int lowerbound, int upperbound) {
   =====
      int count = 0;
   =====
      for (size_t i = 0; i &#60; vec.size(); i++) {
   =====
      for (int i = 0; i &#60; upperbound; i++)                         #paired
   =====
         if (vec[i] i &#62;= lowerbound && vec[i] i &#60;= upperbound) {
            count++;
   =====
         if (vec[i] i &#62; lowerbound && vec[i] i &#60; upperbound) {                         #paired
            count++;
   =====
         }
      }
      return count;
   }