.. parsonsprob:: mucp_7_8
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

   On the strange planet of Noes, there's a law that prohibits the usage of the letter "e".
   As a result, they hired you to write a function called ``censorE`` that replaces all occurences
   of the letter "e" in a string with an asterisk and returns the censored string. For example,
   if the input is "hello world", the function returns "h*llo world".
   -----
   string censorE (string input) {
   =====
   void censorE (string input) {  #paired
   =====
      string copy = input;  #distractor
   =====
      int i = 0;
   =====
      while (i < input.length()) {
   =====
      while (i < input.length() - 1) {  #paired
   =====
         if (input[i] == 'e') {
   =====
         if (input[i] = 'e') {  #paired
   =====
            input[i] = '*';
         }
   =====
            '*' = input[i];  #paired
         }
   =====
         i++;
      }
   =====
      return input;
   }