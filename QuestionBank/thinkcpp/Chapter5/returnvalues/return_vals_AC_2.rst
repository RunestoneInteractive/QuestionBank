.. activecode:: return_vals_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: returnvalues
   :topics: Chapter5/returnvalues
   :from_source: T
   :language: cpp
   :caption: Return Values

   This code fixes the error in the previoius implementation of
   absoluteValue.  If we pass 0 as an argument, the function will
   return 0.  Thus, every route through the conditonal is satisfied.
   ~~~~
   #include <iostream>
   using namespace std;

   double absoluteValue (double x) {
       if (x < 0) {
           return -x;
       }
       else if (x > 0) {
           return x;
       }
       return x;                      // WRONG!!
   }

   int main () {
      cout << absoluteValue(0);
      return 0;
   }