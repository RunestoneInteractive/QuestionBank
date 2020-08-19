.. activecode:: program_dvlmt_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: programdevelopment
   :topics: Chapter5/programdevelopment
   :from_source: T
   :language: cpp
   :caption: Program Development

   This program implements the distance function that we've been
   talking about and outputs the result.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   double distance (double x1, double y1, double x2, double y2) {
       double dx = x2 - x1;
       double dy = y2 - y1;
       double dsquared = dx*dx + dy*dy;
       double result = sqrt (dsquared);
       return result;
   }

   int main () {
       double dist = distance (1.0, 2.0, 4.0, 6.0);
       cout << dist << endl;
      return 0;
   }