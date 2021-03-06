.. activecode:: fraction1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: definingclasses
    :topics: Java4Python/definingclasses
    :from_source: T
    :language: java
    :sourcefile: Fraction.java

    public class Fraction {

        private Integer numerator;
        private Integer denominator;

        public Fraction(Integer num, Integer den) {
            this.numerator = num;
            this.denominator = den;
        }

        public Fraction(Integer num) {
            this.numerator = num;
            this.denominator = 1;
        }

        public Fraction add(Fraction other) {
            Integer newNum, newDen, common;

            newNum = other.getDenominator()*this.numerator + this.denominator*other.getNumerator();
            newDen = this.denominator * other.getDenominator();
            common = gcd(newNum,newDen);
            return new Fraction(newNum/common, newDen/common );
        }

        public Fraction add(Integer other) {
            return add(new Fraction(other));
        }

        private static Integer gcd(Integer m, Integer n) {
            while (m % n != 0) {
                Integer oldm = m;
                Integer oldn = n;
                m = oldn;
                n = oldm%oldn;
            }
            return n;
        }

        public static void main(String[] args) {
            Fraction f1 = new Fraction(1,2);
            Fraction f2 = new Fraction(2,3);

            System.out.println(f1.mul(f2));
            System.out.println(f1.add(1));
        }

    }