.. parsonsprob:: cond_recc_p5
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

   Construct a block of code that prints "Pick me!" if x is
   equal to y, "Choose me!" if x is less than y, OR "Love me!"
   if x + y is even.
   -----
   if (x == y) {
   =====
   if (x = y) { #paired
   =====
    cout << "Pick me!"; }
   =====
   else if (y > x) {
   =====
   if (x < y) { #paired
   =====
    cout << "Choose me!"; }
   =====
   else if ((x + y) % 2 == 0) {
   =====
   else (x + y % 2 == 0) { #paired
   =====
   else if (x + y % 2 == 0) { #paired
   =====
    cout << "Love me!"; }