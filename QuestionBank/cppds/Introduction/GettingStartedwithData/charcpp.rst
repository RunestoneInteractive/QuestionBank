.. activecode:: charcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Considering characters and strings
    :language: cpp

    //outputs the boolean results to show how strings and chars differ in C++
    #include <iostream>
    #include <string>
    using namespace std;

    int main(){

        string strvar = "b";
        char charvar = 'b';

        cout << ('b' == charvar) << endl;
        cout << ("b" == strvar) << endl;
        //cout << ('a' == "a") << endl; // will error!

        return 0;
    }