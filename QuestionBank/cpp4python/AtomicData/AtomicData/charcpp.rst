.. activecode:: charcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :caption: Considering characters and strings
    :language: cpp

    #include <iostream>
    #include <string>
    using namespace std;

    // Demonstrates how chars and strings can not be
    // directly compared.
    int main(){

        string strvar = "b";
        char charvar = 'b';

        cout << ('b' == charvar) << endl;
        cout << ("b" == strvar) << endl;
        //cout << ('a' == "a") << endl; // will error!

        return 0;
    }