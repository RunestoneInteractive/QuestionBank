.. parsonsprob:: traversal_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: traversal
   :topics: Chapter7/traversal
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the ``reverseWord`` function. ``reverseWord``
   should take a string as a parameter and output the letters backwards.
   -----
   void reverseWord (string input) {
   =====
     int x = input.length() - 1;
   =====
     int x = input.length();  #paired
   =====
     while (x >= 0) {
   =====
     while (x > 0) { #paired
   =====
       cout << input[x];
   =====
       x--;
     }
   }
   =====
       x++;
     }
   } #distractor