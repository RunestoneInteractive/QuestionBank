.. parsonsprob:: pass_others_reference_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: passing_other_types_by_reference
   :topics: Chapter8/passing_other_types_by_reference
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Create a function called addNum that takes two parameters, an integer x and an integer y. The function should add y to x, then print x. The variable x should be modified, while the variable y should not.
   -----
   void addNum(int& x, int y) {
   =====
   void addNum(int x&, int y) { #distractor
   =====
   void addNum(int x, int y) { #distractor
   =====
   void addNum(int& x, int& y) { #distractor
   =====
      x = x + y;
   =====
      y = x + y; #distractor
   =====
      cout << x;
   }
   =====
      return x; #distractor
   }