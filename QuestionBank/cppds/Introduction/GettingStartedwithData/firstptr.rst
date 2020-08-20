.. activecode:: firstptr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :language: cpp

    //prints a variable by pointer and value
    #include <iostream>
    using namespace std;

    int main( ) {
        int varN = 100;
        int *ptrN = &varN; // ptrN points to varN address

        cout << "varN value: " << varN << endl;
        cout << "varN location: " << ptrN << endl;
        cout << "dereference ptrN: " << *ptrN << "endl";


        return 0;
    }