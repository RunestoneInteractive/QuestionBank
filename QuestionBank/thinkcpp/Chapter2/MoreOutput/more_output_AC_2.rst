.. activecode:: more_output_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: MoreOutput
   :topics: Chapter2/MoreOutput
   :from_source: T
   :language: cpp
   :caption: Two Statements, One Line of Output

   This program prints two different statements on the same line.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       cout << "Goodbye, ";
       cout << "cruel world!" << endl;
   }