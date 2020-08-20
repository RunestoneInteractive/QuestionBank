.. parsonsprob:: mucp_7_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: mixed_up_code
   :topics: Chapter7/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:
   :practice: T

   Let's write the code for the ``cipherText`` function. ``cipherText``
   should be a void function that takes a string input as a parameter,
   increases the value of each character by 1 (i.e. "bad" turns into "cbe"),
   and outputs the encrypted string.
   -----
   void cipherText (string input) {
   =====
   string cipherText (string input) {  #paired
   =====
      int i = 0;
   =====
      while (i < input.length()) {
   =====
      while (i < input.length() - 1) {  #paired
   =====
         input[i] = input[i] + 1;
   =====
         input[i] = input[i] - 1;  #paired
   =====
         i++;
      }
   =====
      cout << input;
   }
   =====
      return input;  #paired
   }