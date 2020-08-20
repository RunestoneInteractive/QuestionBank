.. activecode:: overloaded_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :language: cpp
    :caption: An overloaded cout operator for the Fraction class

    /*overloading functions to take in different
    inputs and output the correct results*/
    #include <iostream>
    using namespace std;

    class Fraction {
        public:
            Fraction(int top = 0, int bottom = 1){
                num = top;
                den = bottom;
            }

        //the following tells the compiler to look for this friend's definition outside the class
        friend ostream &operator << (ostream &stream, const Fraction &frac);

        private:
            int num, den;
    };

    ostream &operator << (ostream &stream, const Fraction &frac) {
        /** this is the definition. */
        stream << frac.num << "/" << frac.den;
        return stream;
    }

    int main() {
        Fraction myfraction(3, 5);
        cout << myfraction;

        return 0;
    }