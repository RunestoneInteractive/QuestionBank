.. parsonsprob:: character_classification_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: character_classification
   :topics: Chapter7/character_classification
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the ``stringToUpper`` function. ``stringToUpper``
   should convert a string to uppercase.
   -----
   void stringToUpper (string &input) {
   =====
   void stringToUpper (string input) {                         #paired
   =====
      int i = 0;
   =====
      while (i < input.length()) {
   =====
      while (i < input.length() - 1) {  #paired
   =====
         if (isalpha(input[i]) && islower(input[i])) {
   =====
         if (isalpha(input[i]) && isupper(input[i])) {                        #paired
   =====
            input[i] = toupper(input[i]);
         }
   =====
            toupper(input[i]);                        #paired
         }
   =====
         i++;
      }
   }