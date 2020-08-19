.. activecode:: cp_6_AC_7a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: coding_practice
   :topics: Chapter6/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   bool isPrime (int num) {
       if (num <= 1) {
           return false;
       }
       int n = 2;
       while (n < num / 2) {
           if (num % n == 0) {
               return false;
           }
           n++;
       }
       return true;
   }

   int main() {
       cout << isPrime (1) << endl;     // Should output 0
       cout << isPrime (13) << endl;    // Should output 1
       cout << isPrime (24) << endl;    // Should output 0
   }