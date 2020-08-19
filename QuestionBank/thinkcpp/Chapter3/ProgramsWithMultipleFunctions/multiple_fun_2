.. mchoice:: multiple_fun_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: ProgramsWithMultipleFunctions
    :topics: Chapter3/ProgramsWithMultipleFunctions
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.0

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
    
    Which of the following reflects the order in which these functions
    are executed in C++?
    
    -   ``newLine, threeLine, main``
    
        -   Remember to follow the order of execution, which is not necessarily the order the program is written.
    
    -   ``newLine, threeLine, newLine, newLine, newLine, main``
    
        -   Remember to follow the order of execution, which is not necessarily the order the program is written.
    
    -   ``main, threeLine, newLine, newLine, newLine``
    
        +   Execution begins in the main, then functions are executed as they are called.
    
    -   ``main, threeLine``
    
        -   Note that ``newLine`` is called inside of ``threeLine``.