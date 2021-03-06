.. mchoice:: multiple_functions_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: ProgramsWithMultipleFunctions
   :topics: Chapter3/ProgramsWithMultipleFunctions
   :from_source: F
   :answer_a: 12, 13, 14, 8, 9, 10, 15, 16, 17
   :answer_b: 12, 13, 14, 8, 9, 4, 5, 6, 4, 5, 6, 4, 5, 6, 10, 15, 16, 17
   :answer_c: 1, 2, 12, 13, 14, 8, 9, 10, 15, 16, 17
   :answer_d: 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17
   :answer_e: 1, 2, 12, 13, 14, 8, 9, 4, 5, 6, 4, 5, 6, 4, 5, 6, 10, 15, 16, 17
   :correct: b
   :feedback_a: Keep in mind that one of the functions is being called three times.
   :feedback_b: Execution begins in the main, then functions are executed as they are called.
   :feedback_c: Keep in mind that one of the functions is being called three times.  Also, note that function execution begins in int main.
   :feedback_d: Keep in mind that execution begins in the main.  Remember to follow the order of execution, which is not necessarily the order the program is written.
   :feedback_e: Keep in mind that execution begins in the main.

   Consider the following C++ code. Note that line numbers are included
   on the left.

   .. code-block:: cpp
      :linenos:

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

   Which of the following reflects the order in which these lines
   of code are executed in C++?