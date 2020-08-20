.. activecode:: vars_types_a1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter2
   :subchapter: activeCode
   :topics: Chapter2/activeCode
   :from_source: T
   :language: cpp

   Below is one way to fix the program.  ``true`` and ``false`` are
   keywords, so they cannot be used as variable names.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       char t = 'T';
       char f = 'F';
       cout << t << " is short for true. ";
       cout << f << " is short for false." << endl;

       // Do not modify anything below.
       return 0;
   }