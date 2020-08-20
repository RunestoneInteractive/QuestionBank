.. activecode:: first_program_AC
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter1
   :subchapter: first_program
   :topics: Chapter1/first_program
   :from_source: T
   :language: cpp
   :caption: Hello World

   The "Hello, World." program is a great place to start learning a new
   language.  Observe the program structure below.
   ~~~~
   #include <iostream>
   using namespace std;
   // main: generate some simple output
   int main () {
       cout << "Hello, World." << endl;
       return 0;
   }