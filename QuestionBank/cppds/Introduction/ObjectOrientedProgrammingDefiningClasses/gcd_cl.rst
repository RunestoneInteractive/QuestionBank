.. activecode::  gcd_cl
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: F
    :language: cpp
    :caption: The Greatest Common Divisor Function

    //
    #include <iostream>
    using namespace std;

    int gcd(int m, int n) {
        while (m%n != 0) {
            int oldm = m;
            int oldn = n;

            m = oldn;
            n = oldm%oldn;
        }

        return n;
    }

    int main() {
        cout << gcd(20, 10) << endl;
        return 0;
    }