.. activecode:: nested_conditionals_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: NestedConditionals
   :topics: Chapter4/NestedConditionals
   :from_source: T
   :language: cpp
   :caption: Classifying an Integer

   This program classifies a number (x) as positive, negative, or zero,
   just like the program on the previous page.  However, this time, we are
   using nested conditionals.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int x = 9;
       if (x == 0) {
           cout << "x is zero" << endl;
       }
       else {
           if (x > 0) {
               cout << "x is positive" << endl;
           }
           else {
               cout << "x is negative" << endl;
           }
       return 0;
   }