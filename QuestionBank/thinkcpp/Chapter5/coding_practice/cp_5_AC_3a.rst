.. activecode:: cp_5_AC_3a
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

   double calculateIntAngle (int numSides) {
       return (numSides - 2) * 180.0 / numSides;
   }

   int main() {
       cout << calculateIntAngle (3) << endl;   // Should output 60
       cout << calculateIntAngle (4) << endl;   // Should output 90
       cout << calculateIntAngle (5) << endl;   // Should output 108
       cout << calculateIntAngle (8) << endl;   // Should output 135
   }