.. activecode:: random_numbers_AC_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter10
   :subchapter: random_numbers
   :topics: Chapter10/random_numbers
   :from_source: T
   :language: cpp

   The active code below generates random numbers between 0 and 1. Can you modify it
   to generate random numbers between 100.0 and 200.0? If you're stuck you can
   reveal the hint below!
   ~~~~
   #include <iostream>
   #include <cstdlib>
   using namespace std;

   int main () {
       cout << "Let's generate some random numbers between 0 and 1!" << endl;
       for (int i = 0; i < 10; i++) {
           int x = random ();
           double y = double(x) / RAND_MAX;
           cout << y << " ";
       }
   }