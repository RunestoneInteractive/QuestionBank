.. activecode:: recursion_ex_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter5
   :subchapter: onemoreexample
   :topics: Chapter5/onemoreexample
   :from_source: T
   :language: cpp
   :caption: Fibonacci Recursion

   This program uses recursion to calculate the nth number in the
   fibonacci sequence.
   ~~~~
   #include <iostream>
   using namespace std;

   int fibonacci (int n) {
       if (n == 0 || n == 1) {
           return 1;
       }
       else {
           return fibonacci (n-1) + fibonacci (n-2);
       }
   }

   int main () {
       cout << fibonacci(3) << endl;
   }