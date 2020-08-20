.. activecode:: mod_operator_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: TheModulusOperator
   :topics: Chapter4/TheModulusOperator
   :from_source: T
   :language: cpp
   :caption: Modulus Operations

   This program shows the difference between the division operator
   and the modulus operator.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int quotient = 7 / 3;
       int remainder = 7 % 3;
       cout << quotient << endl;
       cout << remainder << endl;
       return 0;
   }