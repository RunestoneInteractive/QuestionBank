.. activecode:: address_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :caption: Memory addresses in C++
    :language: cpp

    #include <iostream>
    using namespace std;


    // outputs the value of a variable
    // as well as the memory address in C++.
    int main(){
        int varN = 101;
        cout << varN << endl;
        cout << &varN << endl; //outputs the memory address of variable varN
        return 0;
    }