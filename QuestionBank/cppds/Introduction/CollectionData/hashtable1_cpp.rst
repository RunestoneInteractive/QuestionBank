.. activecode:: hashtable1_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: CollectionData
    :topics: Introduction/CollectionData
    :from_source: T
    :caption: Using a Hash Table C++
    :language: cpp

    //shows how hash tables can be used in C++
    #include <iostream>
    #include <unordered_map>
    #include <string>
    using namespace std;

    int main() {
        unordered_map<string, string> spnumbers;

        spnumbers = { {"one", "uno"}, {"two", "dos"} };

        spnumbers["three"] = "tres";
        spnumbers["four"] = "cuatro";

        cout << "one is ";
        cout << spnumbers["one"] << endl;

        cout << spnumbers.size() << endl;
    }