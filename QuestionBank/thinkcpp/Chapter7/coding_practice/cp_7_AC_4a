.. activecode:: cp_7_AC_4a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: coding_practice
   :topics: Chapter7/coding_practice
   :from_source: F
   :language: cpp

   #include <iostream>
   using namespace std;

   void removeWord (string input, string word) {
       int length = word.length();
       while (input.find(word) != -1) {
           int index = input.find(word);
           input = input.substr(0, index) + input.substr(index + length);
       }
       cout << input;
   }

   int main() {
       removeWord ("Gucci gang, Gucci gang, Gucci gang, Gucci gang", "gang");
   }