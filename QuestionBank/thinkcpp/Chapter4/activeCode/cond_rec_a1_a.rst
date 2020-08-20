.. activecode:: cond_rec_a1_a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: activeCode
   :topics: Chapter4/activeCode
   :from_source: T
   :language: cpp

   Below is one way to fix the program.  Since we want "THE TEAM"
   to print three times, we must check all three conditons.  this
   means changing the ``else if`` statements to ``if`` statements.
   ~~~~
   #include <iostream>
   using namespace std;

   x = 8;
   y = 8;

   if (x % 2 == 0) {
       cout << "THE TEAM" << endl;
   }
   if (x >= y) {
       cout << "THE TEAM" << endl;
   }
   if (y >= x) {
       cout <<< "THE TEAM" << endl;
   }