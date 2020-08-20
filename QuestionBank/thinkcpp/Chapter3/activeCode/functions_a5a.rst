.. activecode:: functions_a5a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: activeCode
   :topics: Chapter3/activeCode
   :from_source: T
   :language: cpp

   Below is one way to complete the program.
   ~~~~
   #include <iostream>
   using namespace std;

   void border () {
       cout << "------------" << endl;
   }

   int main () {
       cout << "First Line." << endl;
       border();
       cout << "Second Line." << endl;
       return 0;
   }