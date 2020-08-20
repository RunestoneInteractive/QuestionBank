.. activecode:: functions_a7a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: activeCode
   :topics: Chapter3/activeCode
   :from_source: T
   :language: cpp

   Below is one way to complete the program.  I used the
   ``ceil`` function from the ``cmath`` library, but you
   could have solved this problem without using any functions
   from ``cmath``.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   void gpaBoost (double GPA) {
       int betterGPA = ceil(GPA);
       cout << betterGPA << ".000";
   }