.. activecode:: introvector_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Vectors
    :topics: CollectionData/Vectors
    :from_source: T
    :caption: Using a vector in C++
    :language: cpp

    // function that uses a vector to square
    // every number from 0 to 49
    // uses the reserve operation to save space in memory
    #include <iostream>
    #include <vector>
    using namespace std;

    int main(){

        vector<int> intvector;
        intvector.reserve(50);

        for (int i=0; i<50; i++){
            intvector.push_back(i*i);
            cout << intvector[i] << endl;
        }
        return 0;
    }