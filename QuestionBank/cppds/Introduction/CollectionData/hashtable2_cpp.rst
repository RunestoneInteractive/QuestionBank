.. activecode:: hashtable2_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Iterating a Hash Table C++
    :language: cpp

    //shows how to iterate through a hash table in C++
    #include <iostream>
    #include <unordered_map>
    #include <string>
    using namespace std;

    int main() {
        unordered_map<string, string> spnumbers;

        spnumbers = { {"one","uno"},{"two","dos"},{"three","tres"},{"four","cuatro"},{"five","cinco"} };

        for (auto i=spnumbers.begin(); i!=spnumbers.end(); i++ ){
            cout << i->first << ":";
            cout << i->second << endl;
        }
    }