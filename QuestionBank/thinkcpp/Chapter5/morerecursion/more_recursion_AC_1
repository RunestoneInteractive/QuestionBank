.. activecode:: more_recursion_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: morerecursion
   :topics: Chapter5/morerecursion
   :from_source: T
   :language: cpp
   :caption: Factorial Recursion

   This program uses recursion to calculate the factorial of
   the passed argument.
   ~~~~
   #include <iostream>
   using namespace std;

   int factorial (int n) {
       if (n == 0) {
           return 1;
       }
       else {
           int recurse = factorial (n-1);
           int result = n * recurse;
           return result;
       }
   }

   int main () {
       cout << factorial(3) << endl;
   }