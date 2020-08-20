.. activecode:: return_vals_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: returnvalues
   :topics: Chapter5/returnvalues
   :from_source: T
   :language: cpp
   :caption: Return Values

   Notice that there are two return statements in the code below.
   What if we pass zero as an argument, and neither conditional
   returns true?
   ~~~~
   #include <iostream>
   using namespace std;

   double absoluteValue (double x) {
       if (x < 0) {
           return -x;
       }
       else if (x > 0) {
           return x;
       }                          // WRONG!!
   }

   int main () {
       cout << absoluteValue(0);
       return 0;
   }