.. mchoice:: qtnt4_15
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: penguin
   :answer_b: niugnep
   :answer_c: pp
   :answer_d: nninuinguinnguinenguin
   :answer_e: enguinp
   :correct: b
   :feedback_a: This would be correct if s.substring(0, 1) was returned BEFORE the recursive call. Because the recursive call is placed before s.substring(1), the compiler loops through the entire word and returns the last character of the word before any other character.
   :feedback_b: This code removes the first character from the string s until the length of s equals 1. Then, the letters are returned in reverse order.
   :feedback_c: Notice the substrings in this method. s.substring(1), not s.substring(0, 1) is used in the recursive call. s.substring(1) starts at the first index, taking off the first letter of a string and returning the rest of the characters.
   :feedback_d: Notice the substrings in this method. s.substring(0, 1), not s.substring(1) is returned. s.substring(0, 1) only returns one character, so only one character at a time is returned to the method.
   :feedback_e: This would be correct if the last line returned s.substring(1) and wordMixer(s.substring(0, 1)). Because the first substring is used to make a call to the string with only the first character removed, the code will loop through all of the letters before it returns a character.


   The ``wordMixer`` class is shown below. What is returned as a result of ``wordMixer("penguin")``?

   .. code-block:: java

      public String wordMixer (String s)
      {
          if (s.length() == 1)
              return s;

          else
              return wordMixer(s.substring(1)) + s.substring(0, 1);
      }