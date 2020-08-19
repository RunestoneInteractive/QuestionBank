.. parsonsprob:: question15_6_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter15
   :subchapter: Parsing_numbers
   :topics: Chapter15/Parsing_numbers
   :from_source: T
   :adaptive:
   :numbered: left

   Create the replace_with() function that takes a string "str", a character to get rid of "olc_char",
   and a character to replace it with "new_char".  It should return a new string that has replaces any
   occurances of old_char with new_char.
   -----
   string replace_with (string str, char old_char, char new_char) {
   =====
   string replace_with () {                              #paired
   =====
    for (size_t i = 0; i < str.length(); i++) {
   =====
    for (int i = 0; i < str.length(); i++) {                              #paired
   =====
    for (size_t i = 0; i < str.size(); i++) {                              #paired
   =====
     if (str[i] == old_char) {
   =====
     if (i == old_char) {                              #paired
   =====
      str[i] = new_char;
     }
   =====
      new_char = str[i];                              #paired
     }
   =====
      i = new_char;                              #paired
     }
   =====
    }
    return str;
   }
   =====
    }                              #paired
    return new_char;
   }