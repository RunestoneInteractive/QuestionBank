.. activecode:: math_functions_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: MathFunctions
   :topics: Chapter3/MathFunctions
   :from_source: T
   :language: cpp
   :caption: Using the cmath Library

   This program performs calculations using some of the built-in functions
   from the cmath library.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   int main () {
       double result = log (17.0);
       double angle = 1.5;
       double height = sin (angle);
       cout << result << endl;
       cout << angle << endl;
       cout << height << endl;
       return 0;
   }