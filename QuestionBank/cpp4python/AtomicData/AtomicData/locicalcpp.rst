.. activecode:: locicalcpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :caption: Basic Relational and Logical Operators C++
    :language: cpp

    #include <iostream>
    using namespace std;

    // function that demonstrates relational operators.
    int main(){

        cout << (5 == 10) << endl;
        cout << (10 > 5) << endl;
        cout << ((5 >= 1) && (5 <= 10)) << endl;

        return 0;
    }