.. activecode:: NULLexamplecpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :language: cpp

    //showcases how you can use NULL.
    #include <iostream>
    using namespace std;

    int main( ) {
        int x = 12345;
        int *ptrx = &x;

        while (ptrx) {
            cout << "Pointer ptrx points to " << ptrx << endl;
            ptrx = NULL;
        }

        cout << "Pointer ptrx points to nothing!" <<endl;
    }