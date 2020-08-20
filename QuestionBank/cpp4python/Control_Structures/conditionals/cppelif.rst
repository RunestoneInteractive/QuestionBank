.. activecode:: cppelif
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: conditionals
   :topics: Control_Structures/conditionals
   :from_source: T
   :language: cpp
   :sourcefile: elseif.cpp

    // Shows how to use conditional statements
    #include <iostream>
    using namespace std;

    int main() {

        int grade = 85;

        if (grade < 60) {
          cout<<'F'<< endl;
        }
        else {      /* if, elif, and else statement can be used
                        inside of themselves to allow for sub options */
            if (grade < 70) {
                cout<<'D'<< endl;
            }
            else {
                if (grade < 80) {
                    cout<<'C'<< endl;
                }
                else {
                    if (grade < 90) {
                        cout<<'B'<< endl;
                    }
                    else {
                        cout<<'A'<< endl;
                    }
                }
            }
        }
        return 0;
    }