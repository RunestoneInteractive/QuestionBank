.. activecode:: addfrac_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :language: cpp
    :caption: Addition overloaded for Fraction

    //using functions to abstract the idea of a fraction
    #include <iostream>
    using namespace std;

    class Fraction {
        public:
            Fraction(int top = 0, int bottom = 1) {
                num = top;
                den = bottom;
            }
            Fraction operator +(const Fraction &otherFrac) {
                int newnum = otherFrac.num*den + otherFrac.den*num;
                int newden = den*otherFrac.den;
                return Fraction(newnum, newden);
            }

        friend ostream &operator << (ostream &stream, const Fraction &frac);

        private:
            int num, den;
    };

    ostream &operator << (ostream &stream, const Fraction &frac) {
        stream << frac.num << "/" << frac.den;
        return stream;
    }

    int main(){
        Fraction f1(1, 4);
        Fraction f2(1, 2);
        Fraction f3 = f1 + f2;
        cout << f3 << " is "<< f1 << " + " << f2 << endl;
        return 0;
    }