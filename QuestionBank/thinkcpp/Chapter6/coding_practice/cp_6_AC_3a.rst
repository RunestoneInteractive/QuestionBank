.. activecode:: cp_6_AC_3a
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

   void printPyramid(int n) {
       int space, numAsterisks;
       int count = 1;
       while (count <= n) {
           space = n - count;
           while (space > 0) {
               cout << " ";
               space--;
           }
           numAsterisks = 2 * count - 1;
           while (numAsterisks > 0) {
               cout << "*";
               numAsterisks--;
           }
           cout << endl;
           count++;
       }
   }

   int main() {
       printPyramid (5);
   }