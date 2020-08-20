.. activecode:: cp_5_AC_5q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: coding_practice
   :topics: Chapter5/coding_practice
   :from_source: T
   :language: cpp
   :practice: T

   #include <iostream>
   using namespace std;

   int dogToHumanYears (int dogAge) {
       // Write your implementation here.
   }

   int main() {
       cout << dogToHumanYears (1) << endl;   // Should output 15
       cout << dogToHumanYears (2) << endl;   // Should output 24
       cout << dogToHumanYears (3) << endl;   // Should output 28
       cout << dogToHumanYears (5) << endl;   // Should output 36
   }