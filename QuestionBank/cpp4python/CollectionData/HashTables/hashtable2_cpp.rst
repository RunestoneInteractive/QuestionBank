.. activecode:: hashtable2_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: HashTables
    :topics: CollectionData/HashTables
    :from_source: T
    :caption: Iterating a Hash Table C++
    :language: cpp

    // Creates a hash table that maches
    // the english letter to it's spanish
    // equivalent, and outputs every item
    // in the table to the console
    #include <iostream>
    #include <unordered_map>
    #include <string>
    using namespace std;

    int main() {
        unordered_map<string, string> spnumbers;

        spnumbers = { {"one","uno"},{"two","dos"},{"three","tres"},{"four","cuatro"},{"five","cinco"} };

        for (auto i=spnumbers.begin(); i!=spnumbers.end(); i++ ){
            //auto is used to automatically detect the data type when
            //a variable is declared. Use this ONLY when declaring complex
            //variables.

            cout << i->first << ":";
            cout << i->second << endl;
        }
    }