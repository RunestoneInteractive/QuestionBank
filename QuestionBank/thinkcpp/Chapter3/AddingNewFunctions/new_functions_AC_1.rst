.. activecode:: new_functions_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: AddingNewFunctions
   :topics: Chapter3/AddingNewFunctions
   :from_source: T
   :language: cpp
   :caption: The threeLine Function

   Here we define the threeLine function, which calls the newLine function
   three times.  The result is a function that prints three lines after it
   is called.
   ~~~~
   #include <iostream>
   using namespace std;

   void newLine () {
       cout << endl;
   }

   void threeLine () {
       newLine ();  newLine ();  newLine ();
   }

   int main () {
       cout << "First Line." << endl;
       threeLine ();
       cout << "Second Line." << endl;
       return 0;
   }