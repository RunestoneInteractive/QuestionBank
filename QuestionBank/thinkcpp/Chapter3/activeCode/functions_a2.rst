.. activecode:: functions_a2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: activeCode
   :topics: Chapter3/activeCode
   :from_source: T
   :language: cpp

   Fix the code below so that it prints "2 elephants".
   ~~~~
   #include <iostream>
   using namespace std;

   void printAnimals(string a, int b) {
       cout << b << a;
   }

   int main () {
       printAnimals(2, "elephants");
   }