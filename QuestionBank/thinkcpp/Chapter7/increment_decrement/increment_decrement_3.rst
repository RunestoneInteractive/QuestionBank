.. parsonsprob:: increment_decrement_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: increment_decrement
   :topics: Chapter7/increment_decrement
   :from_source: T
   :numbered: left
   :adaptive:

   Print every number from 1-10 in this format: "Number 1". Each number should be on its own line.
   -----
   int x = 0;
   =====
   x = 0; #distractor
   =====
   while (x < 10) {
   =====
       cout << "Number " << x << endl;
   =====
       cout << "Number " << x; #distractor
   =====
       ++x; #distractor
   =====
       x++;
   }