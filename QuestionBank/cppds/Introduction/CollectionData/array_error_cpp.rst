.. activecode:: array_error_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Iterating an array in C++
    :language: cpp

    //outputs the result of trying to access a value outside of an array
    #include <iostream>
    using namespace std;

    int main(){
        int myarray[] = {2,4,6,8};
        for (int i=0; i<=8; i++){
            cout << myarray[i] << endl;
            cout << "id: " << &myarray[i] << endl;
        }
        return 0;
    }