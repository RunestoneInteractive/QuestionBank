.. activecode:: NULLexamplecpp
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

    //Shows the use of a Null pointer to represent "nothing".
    int main( ) {
        int x = 12345;
        int *ptrx = &x;

        while (ptrx) {
            cout << "Pointer ptrx points to " << &ptrx << endl;
            ptrx = nullptr;
        }

        cout << "Pointer ptrx points to nothing!\n";
    }