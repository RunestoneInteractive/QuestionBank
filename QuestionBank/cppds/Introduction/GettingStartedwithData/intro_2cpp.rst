.. activecode:: intro_2cpp
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: F
    :caption: Basic Relational and Logical Operators C++
    :language: cpp

    #include <iostream>
    #include <cmath>
    using namespace std;

    int main(){

        cout << (5==10) << endl;
        cout << (10 > 5) << endl;
        cout << (5 >= 1 && 5 <= 10) << endl;

        return 0;
    }