.. activecode:: locicalcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Basic Relational and Logical Operators C++
    :language: cpp

    //outputs the results from the relational and logical operators
    #include <iostream>
    using namespace std;

    int main(){

        cout << (5 == 10) << endl;
        cout << (10 > 5) << endl;
        cout << ((5 >= 1) && (5 <= 10)) << endl;

        return 0;
    }