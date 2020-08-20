.. activecode:: functions_a9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: activeCode
   :topics: Chapter3/activeCode
   :from_source: T
   :language: cpp

   Below is one way to complete the program.  Cotangent, arctangent,
   and ``atan`` from the ``cmath`` library are all the same.  You just
   need to make sure to convert your angle to radians before doing any
   calculations with sinusoidal functions.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   void tanDegrees (double degrees) {
       double radians = degrees * (2 * 3.14) / 360.0;
       double tangent = tan(radians);
       cout << tangent;
   }