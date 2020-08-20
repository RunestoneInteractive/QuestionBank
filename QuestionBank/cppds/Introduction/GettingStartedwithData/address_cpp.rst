.. activecode:: address_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Memory addresses in C++
    :language: cpp

    //outputs both the value of varN and the location in memory of varN
    #include <iostream>
    using namespace std;

    int main(){
        int varN = 101;
        cout << varN << endl;
        cout << &varN << endl;
        return 0;
    }