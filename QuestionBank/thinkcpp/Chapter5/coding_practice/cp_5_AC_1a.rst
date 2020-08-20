.. activecode:: cp_5_AC_1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: coding_practice
   :topics: Chapter5/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   double calculator (double first, double second, char operation) {
       if (operation == '+') {
           return first + second;
       }
       else if (operation == '-') {
           return first - second;
       }
       else if (operation == '*') {
           return first * second;
       }
       else {
           return first / second;
       }
   }

   int main() {
       cout << calculator (3, 6, '+') << endl;      // Should output 9
       cout << calculator (19, 2, '-') << endl;     // Should output 17
       cout << calculator (5, 8, '*') << endl;      // Should output 40
       cout << calculator (16, 4, '/') << endl;     // Should output 4
   }