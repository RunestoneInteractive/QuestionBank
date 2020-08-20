.. parsonsprob:: mucp_7_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: mixed_up_code
   :topics: Chapter7/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write a function called ``alphabetizer`` which takes
   three ``string``\s, ``first``, ``second``, and ``third``,
   and returns a ``string`` which alphabetizes
   the words and separates them with spaces. For example,
   ``alphabetizer ("just", "do", "it")`` returns the ``string``
   "do it just". Put the necessary blocks in the correct order.
   Use the ``compare`` function from the ``<string>`` library.
   -----
   string alphabetizer (string first, string second, string third) {
   =====
   void alphabetizer (string first, string second, string third) {  #paired
   =====
      if (first.compare(second) < 0) {
   =====
         if (third.compare(first) < 0) {
   =====
            return third + " " + first + " " + second;
         }
   =====
         else if (third.compare(second) < 0) {
   =====
            return first + " " + third + " " + second;
         }
   =====
         else {
   =====
            return first + " " + second + " " + third;
         }
      }
   =====
      else {
   =====
         if (third.compare(second) < 0) {
   =====
            return third + " " + second + " " + first;
         }
   =====
         else if (third.compare(first) < 0) {
   =====
            return second + " " + third + " " + first;
         }
   =====
         else {
   =====
            return second + " " + first + " " + third;
         }
      }
   }