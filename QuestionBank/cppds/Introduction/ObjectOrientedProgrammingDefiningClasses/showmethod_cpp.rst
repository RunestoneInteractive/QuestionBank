.. activecode:: showmethod_cpp
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :language: cpp
    :caption: Show method implementation

    //using functions to print fractions to the command line.
    #include <iostream>
    using namespace std;

    class Fraction {
        public:
            Fraction(int top = 0, int bottom = 1){
                num = top;
                den = bottom;
            }

            void show(){
                cout << num << "/" << den << endl;
            }
        private:
            int num, den;
    };

    int main() {
        Fraction fraca(3, 5);
        Fraction fracb(3);
        Fraction fracc; //notice there are no parentheses here.
        // cout << fraca << endl; //uncomment to see error
        fraca.show();
        fracb.show();
        fracc.show();
        return 0;
    }