.. activecode:: cp_7_AC_1a
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
   #include "ctype.h"
   using namespace std;

   bool isPalindrome (string input) {
       int front = 0;
       int back = input.length() - 1;
       while (front < back) {
           while (!isalpha(input[front])) {
               front++;
           }
           while (!isalpha(input[back])) {
               back--;
           }
           if (input[front] != input[back]) {
               return false;
           }
           front++;
           back--;
       }
       return true;
   }

   int main() {
       cout << isPalindrome ("racecar") << endl;               // Should output 1
       cout << isPalindrome ("no lemon, no melon") << endl;    // Should output 1
       cout << isPalindrome ("kangaroo") << endl;              // Should output 0
   }