.. activecode:: recursion_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: Recursion
   :topics: Chapter4/Recursion
   :from_source: T
   :language: cpp
   :caption: Recursion

   Watch how the countdown function works when we start with a value
   of 3.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   void countdown (int n) {
       if (n == 0) {
           cout << "Blastoff!" << endl;
       }
       else {
           cout << n << endl;
           countdown (n-1);
       }
   }

   int main () {
       countdown (3);
       return 0;
   }