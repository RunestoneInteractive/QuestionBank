.. activecode:: vector_errors_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Vectors
    :topics: CollectionData/Vectors
    :from_source: T
    :caption: Vectors out of bounds
    :language: cpp

    // Note: counting always starts at 0
    // This demonstrates what happens when
    // accessing datat outside of your vector

    #include <iostream>
    #include <vector>
    using namespace std;

    int main(){

        vector<int> intvector;
        intvector.reserve(10);

        for (int i=0; i<10; i++){
            intvector.push_back(i);
        }

        for (int i=0; i<=10; i++){
            cout << "intvector[" << i << "]="
            <<intvector[i] << endl;
        }

        return 0;
    }