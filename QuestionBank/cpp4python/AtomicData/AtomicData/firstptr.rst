.. activecode:: firstptr
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :language: cpp

    #include <iostream>
    using namespace std;

    // demonstrates what happens when you dereference a pointer
    int main( ) {
        int varN = 9;
        int *ptrN = &varN; // ptrN points to varN address

        cout << "varN value: " << varN << endl;
        cout << "varN location: " << ptrN << endl;
        cout << "dereference ptrN: " << *ptrN << endl;


        return 0;
    }