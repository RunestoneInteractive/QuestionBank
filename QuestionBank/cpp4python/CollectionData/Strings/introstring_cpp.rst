.. activecode:: introstring_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: CollectionData
    :subchapter: Strings
    :topics: CollectionData/Strings
    :from_source: T
    :caption: Strings in C++
    :language: cpp

    // This function concatenates the string hello World
    // Then it says where World begins in the concatenated string
    #include <iostream>
    #include <string>
    using namespace std;

    int main(){

        string mystring1 = "Hello";
        string mystring2 = "World!";
        string mystring3;

        mystring3 = mystring1 + " " + mystring2;
        cout << mystring3 << endl;

        cout << mystring2 << " begins at ";
        cout << mystring3.find(mystring2) << endl;

        return 0;
    }