.. activecode:: cp_7_AC_3a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: coding_practice
   :topics: Chapter7/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   void censorWord(string input, string word) {
       int length = word.length();
       while ((int)input.find(word) != -1) {
           int index = input.find(word);
           int i = 0;
           while (i < length) {
               input[index + i] = '*';
               i++;
           }
       }
       cout << input;
   }

   int main() {
       censorWord ("I really, really, really, really, really, really like you", "really");
   }