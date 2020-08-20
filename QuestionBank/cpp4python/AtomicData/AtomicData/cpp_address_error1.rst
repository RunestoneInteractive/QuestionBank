.. activecode:: cpp_address_error1
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

    int main( ) {
        int varN = 100;
        int *ptrN = varN; // Note no ampersand,
            // ptrN now refers to memory position 100,
            // whatever happens to be there!
            // You might get an error or you might not!

         cout << "varN value: " << varN << endl;
         cout << "ptrN location: " << ptrN << endl;
         cout << "ptrN points to varN: " << endl;
         cout << "dereference ptrN: " << *ptrN << endl;

         return 0;
    }