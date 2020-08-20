.. parsonsprob:: mucp_7_2
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

   An anagram is a play on words by rearranging the letters of the original words
   to form new words. For example, the letters in "listen" can be rearranged to
   make "silent". Write a program that rearranges "night" into "thing" and prints the anagram.
   Put the necessary blocks in the correct order.
   -----
   int main() {
   =====
      string original = "night";
   =====
      string original = "thing";  #paired
   =====
      string anagram = original;
   =====
      anagram[0] = original[original.find('t')];
   =====
      anagram[1] = original[original.find('h')];
   =====
      anagram[2] = original[original.find('i')];
   =====
      anagram[3] = original[original.find('n')];
   =====
      anagram[4] = original[original.find('g')];
   =====
      cout << anagram;
   =====
   }