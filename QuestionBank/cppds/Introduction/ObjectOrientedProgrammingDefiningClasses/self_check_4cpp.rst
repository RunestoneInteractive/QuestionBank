.. activecode:: self_check_4cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :language: cpp
    :nocodelens:

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

    class Fraction {
        public:
            Fraction(int top, int bottom) {
                num = top;
                den = bottom;
            }
            Fraction(int top){
                num = top;
                den = 1;
            }
            Fraction(){
                num = 1;
                den = 1;
            }
            Fraction operator +(Fraction otherFrac) {
                int newnum = num*otherFrac.den + den*otherFrac.num;
                int newden = den*otherFrac.den;
                int common = gcd(newnum, newden);

                return Fraction(newnum/common,newden/common);
            }
            bool operator ==(Fraction &otherFrac) {
                int firstnum = num*otherFrac.den;
                int secondnum = otherFrac.num*den;

                return firstnum==secondnum;
            }

        friend ostream& operator<<(ostream& stream, const Fraction& fraction);

        private:
            int num, den;
    };

    ostream& operator << (ostream& stream, const Fraction& fraction) {
        stream << fraction.num << "/" << fraction.den;

        return stream;
    }

    int main(){
        Fraction x(1, 2);
        Fraction y(2, 4);
        cout << x << " + " << y << " = " << x+y << endl;
        if (x==y){
            cout << "x is equal y" << endl;
        }
        else{
            cout << "x is not equal y" << endl;
        }
        return 0;
    }