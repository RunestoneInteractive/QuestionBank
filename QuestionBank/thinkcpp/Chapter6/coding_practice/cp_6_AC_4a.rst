.. activecode:: cp_6_AC_4a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter6
   :subchapter: coding_practice
   :topics: Chapter6/coding_practice
   :from_source: F
   :language: cpp

   #include <iostream>
   using namespace std;

   void printAddTable(int n) {
       int row = 0;
       while (row <= n) {
           int col = 0;
           while (col <= n) {
               cout << row + col << '\t';
               col++;
           }
           cout << endl;
           row++;
       }
   }

   int main() {
       printAddTable (10);
   }