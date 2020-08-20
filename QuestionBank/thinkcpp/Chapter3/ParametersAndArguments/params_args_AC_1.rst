.. activecode:: params_args_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ParametersAndArguments
   :topics: Chapter3/ParametersAndArguments
   :from_source: T
   :language: cpp
   :caption: Parameter Practice

   The following code will show the output of the printTwice function.
   Try modifying the value of argument to change the output.
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