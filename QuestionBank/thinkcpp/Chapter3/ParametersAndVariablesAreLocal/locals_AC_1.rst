.. activecode:: locals_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ParametersAndVariablesAreLocal
   :topics: Chapter3/ParametersAndVariablesAreLocal
   :from_source: T
   :language: cpp
   :caption: Understanding Parameters

   The following code will show the output of the printTwice function.
   Notice that it is the argument 'b' that is outputted, not the
   variable 'phil'.
   ~~~~
   #include <iostream>
   using namespace std;

   void printTwice (char phil) {
       cout << phil << phil << endl;
   }

   int main () {
       char argument = 'b';
       printTwice (argument);
       return 0;
   }