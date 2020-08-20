.. activecode:: array_error_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Iterating an array in C++
    :language: cpp

    #include <iostream>
    using namespace std;

    // demonstrates what happens when iterating
    // outside of an array in C++,
    //also outputs the location of the value in memory
    int main(){
        int myarray[] = {2,4,6,8};
        for (int i=0; i<=8; i++){
            cout << myarray[i] << endl;
            cout << "id: " << &myarray[i] << endl;
        }
        return 0;
    }