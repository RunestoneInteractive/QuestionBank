.. activecode:: foverload_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: DefiningFunctions
    :topics: Introduction/DefiningFunctions
    :from_source: T
    :caption: function overloading in C++
    :language: cpp

    //showcases function overloading in C++
    #include <iostream>
    using namespace std;

    void myfunct(int n) {
         cout << "1 parameter: " << n <<endl;
    }

    void myfunct(int n, int m) {
         cout << "2 parameters: " << n;
         cout << " and " << m <<endl;
    }

    int main() {

        myfunct(4);
        myfunct(5, 6);
        myfunct(100);

        return 0;
    }