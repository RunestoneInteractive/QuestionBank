.. activecode:: random_numbers_AC_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: random_numbers
   :topics: Chapter10/random_numbers
   :from_source: T
   :language: cpp

   The active code below generates random numbers between 1 and 7.
   ~~~~
   #include <iostream>
   #include <cstdlib>
   using namespace std;

   int main () {
       int upperBound = 8;
       cout << "Let's generate some random numbers between 1 and 7!" << endl;
       for (int i = 0; i < 10; i++) {
           int x = random ();
           int y = x % upperBound;
           cout << y << " ";
       }
   }