.. activecode:: cp_7_AC_1q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter7
   :subchapter: coding_practice
   :topics: Chapter7/coding_practice
   :from_source: T
   :language: cpp
   :practice: T

   #include <iostream>
   #include "ctype.h"
   using namespace std;

   bool isPalindrome (string input) {
       // Write your implementation here.
   }

   int main() {
       cout << isPalindrome ("racecar") << endl;               // Should output 1
       cout << isPalindrome ("no lemon, no melon") << endl;    // Should output 1
       cout << isPalindrome ("kangaroo") << endl;              // Should output 0
   }