.. activecode:: return_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: TheReturnStatement
   :topics: Chapter4/TheReturnStatement
   :from_source: T
   :language: cpp
   :caption: Terminating a Function with a Return

   This program will terminate with a return statement if the argument
   provided is not positive.  Try running the code as is.  If you get
   an error message, try changing the value of x.
   ~~~~
   #include <iostream>
   #include <cmath>
   using namespace std;

   void printLogarithm (double x) {
       if (x <= 0.0) {
           cout << "Positive numbers only, please." << endl;
           return;
       }
       double result = log (x);
       cout << "The log of x is " << result;
   }

    int main() {
        double y = -9.8;
        printLogarithm(y);
        return 0;
    }