.. activecode:: jsfrac1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: ObjectOriented
    :subchapter: javascript_classes
    :topics: ObjectOriented/javascript_classes
    :from_source: T
    :language: javascript

    "use strict"
    class Fraction {
        constructor(num, den) {
            this._numerator = num;
            this._denominator = den;
        }

        toString() {
            return `${this.numerator} / ${this.denominator}`;
        }

        get numerator() {
            return this._numerator;
        }

        get denominator() {
            return this._denominator;
        }

        set numerator(v) {
            console.log("error cannot set the numerator");
        }

    }

    let x = new Fraction(2,3);
    writeln("x is " + x)
    writeln(x.numerator)