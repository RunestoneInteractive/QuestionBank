.. activecode:: logical_1cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :caption: Logical Operators C++
    :language: cpp

    #include <iostream>
    using namespace std;

    // function that demonstrates logical operators
    int main() {
      cout << true << endl;
      cout << false << endl;
      cout << (true || false) << endl;
      cout << (true && false) << endl;
      return 0;
    }