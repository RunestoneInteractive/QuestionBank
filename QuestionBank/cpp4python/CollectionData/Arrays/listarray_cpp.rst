.. activecode:: listarray_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Arrays
    :topics: CollectionData/Arrays
    :from_source: T
    :caption: Iterating an array in C++
    :language: cpp

    // outputs all elements in the array
    //to the console
    #include <iostream>
    using namespace std;

    int main(){
        int myarray[] = {2,4,6,8};
        for (int i=0; i<4; i++){
            cout << myarray[i] << endl;
        }
        return 0;
    }