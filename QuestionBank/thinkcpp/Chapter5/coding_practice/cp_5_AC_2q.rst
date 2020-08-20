.. activecode:: cp_5_AC_2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter5
    :subchapter: coding_practice
    :topics: Chapter5/coding_practice
    :from_source: T
    :language: cpp
    :practice: T

    A binary number is one that is expressed in the base-2 numeral system.
    Write a function ``convertToBinary`` which takes an ``int decimal`` as
    a parameter. ``convertToBinary`` takes the number in decimal, converts
    it into a binary number, and returns the binary number. Test your function
    in ``main``.
    ~~~~
    #include <iostream>
    using namespace std;

    int convertToBinary (int decimal) {
        // Write your implementation here.
    }

    int main() {
        cout << convertToBinary (1) << endl;      // Should output 1
        cout << convertToBinary (5) << endl;      // Should output 101
        cout << convertToBinary (16) << endl;     // Should output 10000
        cout << convertToBinary (31) << endl;     // Should output 11111
    }