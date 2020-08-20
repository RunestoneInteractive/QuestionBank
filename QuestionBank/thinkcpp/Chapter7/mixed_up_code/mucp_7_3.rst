.. parsonsprob:: mucp_7_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: mixed_up_code
   :topics: Chapter7/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Let's write the function ``longerString``, which takes two ``strings``
   as parameters, ``first`` and ``second``. If ``first`` has more letters
   than ``second``, ``longerString`` prints "``first`` is longer than ``second``",
   and vice versa. If they have the same number of letters, ``longerString``
   prints "``first`` and ``second`` are the same length".
   Put the necessary blocks in the correct order.
   -----
   void longerString (string first, string second) {
   =====
   string longerString (string first, string second) {  #paired
   =====
      if (first.length() > second.length()) {
   =====
      if (first.length() >= second.length()) {  #paired
   =====
         cout << first << " is longer than " << second << endl;
      }
   =====
      else if (first.length() < second.length()) {
   =====
         cout << second << " is longer than " << first << endl;
      }
   =====
         cout << second << " is longer than " << second << endl;  #paired
      }
   =====
      else {
   =====
      else (first.length() == second.length()) {  #distractor
   =====
         cout << first << " and " << second << " are the same length" << endl;
      }
   =====
   }