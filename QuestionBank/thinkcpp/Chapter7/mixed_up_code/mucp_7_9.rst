.. parsonsprob:: mucp_7_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: mixed_up_code
   :topics: Chapter7/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive:

   Your work for the planet of Noes impressed the nearby planets of Noas, Nois, Noos, and Nous.
   They want you to write different functions that censor out each planet's corresponding forbidden letter.
   However, your galaxy brain knows better than to write a different function for each planet.
   Using generalization, write the function ``censorLetter`` which takes a string input and a char to censor
   as parameters and returns a censored string. For example, censorLetter("Bye world", 'o') returns the
   string "Bye w*rld".
   -----
   string censorLetter (string input, char letter) {
   =====
   string censorLetter (string input) {  #paired
   =====
      int i = 0;
   =====
      int i = 1;  #paired
   =====
      while (i < input.length()) {
   =====
         if (input[i] == letter) {
   =====
         if (input[i] == "letter") {  #paired
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