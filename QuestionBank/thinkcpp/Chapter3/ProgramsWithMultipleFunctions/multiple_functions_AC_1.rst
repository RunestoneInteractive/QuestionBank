.. activecode:: multiple_functions_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ProgramsWithMultipleFunctions
   :topics: Chapter3/ProgramsWithMultipleFunctions
   :from_source: T
   :language: cpp
   :caption: Multiply / Add Two

   This program calls the multiplyTwo and addTwo functions in the
   main.  See if you can follow the order of execution.
   ~~~~
   #include <iostream>
   using namespace std;

   void printTotal (int x) {
       cout << x << endl;
   }

   int multiplyTwo (int x) {
       int total = x * 2;
       printTotal(total);
       return total;
   }

   int addTwo (int x) {
       int total = x + 2;
       return total;
   }

   int main () {
       int num = 2;
       int newNum = multiplyTwo(num);
       int newerNum = addTwo(newNum);
       return 0;
   }