.. parsonsprob:: looping_counting_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: looping_and_counting
   :topics: Chapter7/looping_and_counting
   :from_source: T
   :numbered: left
   :adaptive:

   The following is the correct code for printing the even numbers from 0 to 10, but it also includes some extra code that you won't need. Drag the needed blocks from the left and put them in the correct order on the right.
   -----
   x = x + 1; #distractor
   =====
   x = 0;
   =====
   while (x <= 10) {
   =====
   while (x < 10) { #distractor
   =====
      cout << x << endl;
   =====
      x = x + 2;
   }