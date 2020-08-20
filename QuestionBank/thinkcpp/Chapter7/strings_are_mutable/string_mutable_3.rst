.. parsonsprob:: string_mutable_3
      :author: bmiller
      :difficulty: 3.0
      :basecourse: thinkcpp
      :chapter: Chapter7
      :subchapter: strings_are_mutable
      :topics: Chapter7/strings_are_mutable
      :from_source: F
      :numbered: left
      :adaptive:

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
        for (int i = 0; i < input.length(); ++i) {
      =====
        for (int i = 0; i < input.length() - 1; ++i) {  #paired
      =====
          if (input[i] == 'e') {
      =====
          if (input[i] = 'e') {  #paired
      =====
            input[i] = '*';
          }
        }
      =====
            '*' = input[i];  #paired
          }
        }
      =====
        return input;
      }