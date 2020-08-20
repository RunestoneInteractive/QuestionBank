.. parsonsprob:: mucp_5_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: mixed_up_code
   :topics: Chapter5/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :practice: T

   Most bacteria cultures grow exponentially. For this problem,
   assume the number of cells in a bacterial culture doubles every hour.
   Let's write the code for the ``countBacteria`` function. ``countBacteria``
   takes an ``int hour`` as a parameter and returns the number of bacteria cells
   after ``hour`` hours. Assume when ``hour`` is 0, there is one cell. When
   ``hour`` is one, the number of cells doubles to two. When hour is ``two``,
   the number of cells doubles to four. Use recursion.
   Put the necessary blocks of code in the correct order.
   -----
   int countBacteria (int hour) {
   =====
   void countBacteria (int hour) {  #distractor
   =====
   bool countBacteria (int hour) {  #distractor
   =====
      if (hour == 0) {
   =====
      if (hour == 1) {  #paired
   =====
         return 1;
      }
   =====
         return 2 * hour;  #distractor
      }
   =====
      else {
   =====
         return 2 * countBacteria (hour - 1);
      }
   =====
         return 2 + countBacteria (hour - 1);  #distractor
      }
   =====
         return 2 * countBacteria (hour);  #distractor
      }
   =====
   }