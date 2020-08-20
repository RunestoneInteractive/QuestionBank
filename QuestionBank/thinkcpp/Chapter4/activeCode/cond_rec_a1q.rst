.. activecode:: cond_rec_a1q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Fix the code below so that it prints "THE TEAM" "THE TEAM"
   "THE TEAM" on three separate lines.
   ~~~~
   #include <iostream>
   using namespace std;

   x = 8;
   y = 8;

   if (x % 2 == 0) {
       cout << "THE TEAM";
   }
   else if (x >= y) {
       cout << "THE TEAM";
   }
   else if (y >= x) {
       cout <<< "THE TEAM";
   }