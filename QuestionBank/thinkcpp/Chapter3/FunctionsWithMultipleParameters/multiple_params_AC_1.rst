.. activecode:: multiple_params_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: FunctionsWithMultipleParameters
   :topics: Chapter3/FunctionsWithMultipleParameters
   :from_source: T
   :language: cpp
   :caption: Understanding Multiple Parameters

   This program shows how the dollar_amount and cent_amount arguments
   are passed into the printPrice function.
   ~~~~
   #include <iostream>
   using namespace std;

   void printPrice (int dollars, int cents) {
       cout << "Price is " << dollars << " dollars and " << cents << " cents." << endl;
   }

   int main () {
       int dollar_amount = 2;
       int cent_amount = 92;
       printPrice (dollar_amount, cent_amount);
       return 0;
   }