.. activecode:: cp_7_AC_7a
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

   string capitalize (string input) {
       int n = 0;
       while (n < (int)input.length()) {
           if (n == 0) {
               input[n] = toupper(input[n]);
           }
           else if (input[n-1] == ' ') {
               input[n] = toupper(input[n]);
           }
           n++;
       }
       return input;
   }

   int main() {
       cout << capitalize ("every word in this string should be capitalized!") << endl;
       cout << capitalize ("this String As well") << endl;
   }