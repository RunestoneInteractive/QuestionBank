.. parsonsprob:: operations_structures_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: operations_on_structures
   :topics: Chapter8/operations_on_structures
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   Construct a block of code that correctly initializes the instance variables of a structure.
   -----
   struct Point {
   =====
      double x, y;
   };
   =====
   int main() {
   =====
      Point blank;
   =====
      int blank; #distractor
   =====
      blank = (Point){ 12.0, 3.2 };
   =====
      blank = (Point){ 12.0, 3.2 } #distractor
   =====
      blank = { 12.0, 3.2 }; #distractor
   }