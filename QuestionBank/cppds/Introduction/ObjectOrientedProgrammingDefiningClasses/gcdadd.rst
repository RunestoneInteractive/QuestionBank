.. activecode:: gcdadd
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: ObjectOrientedProgrammingDefiningClasses
  :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
  :from_source: T
  :language: cpp
  :caption: Reduced fraction addition

  #include <iostream>
  using namespace std;

  int gcd(int m, int n){
      /** gcd is a helper function, used by but not part of the Fraction class */
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
              return Fraction(newnum/common, newden/common);
          }

      friend ostream& operator << (ostream& stream, const Fraction& fraction);

      private:
          int num, den;
  };

  ostream & operator << (ostream& stream, const Fraction& fraction) {
      stream<<fraction.num<<"/"<<fraction.den;
      return stream;
  }

  int main(){
      Fraction f1(1, 4);
      Fraction f2(1, 2);
      Fraction f3 = f1 + f2;
      cout << f3 << " is "<< f1 << " + " << f2 << endl;
      return 0;
  }