.. activecode:: jsoldclass
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: ObjectOriented
    :subchapter: javascript_classes
    :topics: ObjectOriented/javascript_classes
    :from_source: T
    :language: javascript

    function Fraction(num, den) {
        this.numerator = num;
        this.denominator = den;
    }

    Fraction.prototype.toString = function() {
        return this.numerator + " / " + this.denominator;
    }

    f = new Fraction(2,3);
    writeln("f is " + f)