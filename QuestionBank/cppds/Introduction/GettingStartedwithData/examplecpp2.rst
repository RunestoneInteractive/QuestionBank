.. activecode:: examplecpp2
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: F
    :language: cpp

    #include <iostream>
    using namespace std;

    int main( ) {
        int x = 12345;
        int *ptrx = &x;

        while( ptrx ) {
        cout << "Pointer ptrx points to something\n";
        ptrx = 0;
        }

        cout << "Pointer ptrx points to nothing!\n";
    }