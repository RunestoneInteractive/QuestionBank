.. parsonsprob:: cond_recc_p3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: MixedUpCode
   :topics: Chapter4/MixedUpCode
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   Construct a function that prints the difference of a and b if the result
   would result in a positive number.  Otherwise, prints -1.
   -----
   void difference (int a, int b) {
   =====
   int difference (int a, int b) { #paired
   =====
    if (a - b > 0) {
   =====
    if (a - b < 0) { #paired
   =====
     cout << a - b;
    }
   =====
    else {
   =====
     cout << -1;
    }
   =====
   }