.. activecode:: more_output_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: MoreOutput
   :topics: Chapter2/MoreOutput
   :from_source: T
   :language: cpp
   :caption: Two Lines of Output

   This program prints two different statements on two different lines
   using ``endl``.
   ~~~~
   #include <iostream>
   using namespace std;

   // main: generate some simple output
   int main () {
       cout << "Hello, world." << endl;     // output one line
       cout << "How are you?" << endl;      // output another
   }