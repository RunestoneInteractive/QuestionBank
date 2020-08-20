.. activecode:: composition_AC_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: Composition
   :topics: Chapter2/Composition
   :from_source: T
   :language: cpp
   :caption: Performing Calculations Before Assignment

   This program performs a calculation involving variables and
   simultaneously assigns the result to a variable.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int minute = 3;
       int percentage;
       percentage = (minute * 100) / 60;
       cout << percentage;
   }