.. activecode:: activepassrefcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: DefiningFunctions
    :topics: Introduction/DefiningFunctions
    :from_source: T
    :caption: Pass by Reference
    :language: cpp

    #include <iostream>
    using namespace std;

    // swap_values() function definition
    // Interchanges the values located by variable1 and variable2.

    // Notice that this function does not return anything!
    void swap_values(int &variable1, int &variable2) {
        int temp;           // temporary storage for swap

        temp = variable1;
        variable1 = variable2;
        variable2 = temp;
    }

    int main( ) {
        int first_num, second_num;
        first_num = 7;
        second_num = 8;

        cout << "Two numbers before swap function: 1) " << first_num << " 2) " << second_num << endl;
        swap_values(first_num, second_num);
        cout << "The numbers after swap function: 1) " << first_num << " 2) " << second_num;

        return 0;
    }