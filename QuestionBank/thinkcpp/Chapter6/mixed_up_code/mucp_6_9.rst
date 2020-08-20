.. parsonsprob:: mucp_6_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: mixed_up_code
   :topics: Chapter6/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :practice: T

   Write the function ``summation`` which takes two ``int``\s
   as parameters, ``start`` and ``end``. ``summation`` adds
   all the integers from ``start`` to ``end``, inclusive, together and returns
   the sum. Put the necessary blocks in the correct order.
   -----
   int summation (int start, int end) {
   =====
   void summation (int start, int end) {  #distractor
   =====
   int summation () {  #distractor
   =====
      int n = start;
   =====
      int sum = 0;
   =====
      int sum = start;  #distractor
   =====
      while (n <= end) {
   =====
      while (n < end) {  #paired
   =====
         sum = sum + n;
   =====
         n++;
      }
   =====
      return sum;
   }
   =====
      return n;  #distractor
   }