.. activecode:: cp_7_AC_9a
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

   string longestWord (string input) {
       int n = 0;
       string longest;
       int maxLength = 0;
       while (n < (int)input.length()) {
           int wordLength = 0;
           while (input[n] != ' ' && n < (int)input.length()) {
               wordLength++;
               n++;
           }
           if (wordLength > maxLength) {
               maxLength = wordLength;
               longest = input.substr(n - maxLength, maxLength);
           }
           n++;
       }
       return longest;
   }

   int main() {
       cout << longestWord ("what is the longest word in this string") << endl;  // Should output "longest"
       cout << longestWord ("these words are very close in size") << endl;       // Should output "these"
   }