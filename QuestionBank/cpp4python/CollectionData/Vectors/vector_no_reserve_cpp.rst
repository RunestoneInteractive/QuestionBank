.. activecode:: vector_no_reserve_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Vectors
    :topics: CollectionData/Vectors
    :from_source: T
    :caption: With use of ``reserve``
    :language: cpp

    // function that uses a vector to square
    // every number from 0 to 49
    // and does not use reserve.
    // shows amount of space used
    #include <iostream>
    #include <vector>
    using namespace std;

    int main(){

        vector<int> intvector;
        // without intvector.reserve(50);

        for (int i=0; i<50; i++){
            intvector.push_back(i*i);
            cout << intvector[i] << endl;
            cout << "capacity: " << intvector.capacity() << endl;
        }
        return 0;
    }