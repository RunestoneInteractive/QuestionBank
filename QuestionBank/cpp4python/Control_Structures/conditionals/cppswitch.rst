.. activecode:: cppswitch
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: conditionals
   :topics: Control_Structures/conditionals
   :from_source: T
   :language: cpp
   :sourcefile: switchup.cpp

    // Shows how to use a Switch statement.

    #include <iostream>
    using namespace std;

    int main() {

        int grade = 85;

        int tempgrade = grade/10;
        switch(tempgrade) {  /*switch cases allow for different options based on
                            the value of temp grade similar to if statements*/
        case 10:
        case 9:
            cout << "The grade is A" << endl;
            break;
        case 8:
            cout << "The grade is B" << endl;
            break;
        case 7:
            cout << "The grade is C" << endl;
            break;
        case 6:
            cout << "The grade is D" << endl;
            break;
        default:
            cout << "The grade is F" << endl;
        }

        return 0;
    }