.. activecode:: random_numbers_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: random_numbers
   :topics: Chapter10/random_numbers
   :from_source: T
   :language: cpp

   Take a look at the active code below, which generates 4 random numbers.
   ~~~~
   #include <iostream>
   #include <cstdlib>
   using namespace std;

   int main () {
       for (int i = 0; i < 4; i++) {
           int x = random ();
           cout << x << endl;
       }
       return 0;
   }