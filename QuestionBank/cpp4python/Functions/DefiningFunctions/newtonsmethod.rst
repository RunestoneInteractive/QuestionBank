.. activecode:: newtonsmethod
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cpp4python
  :chapter: Functions
  :subchapter: DefiningFunctions
  :topics: Functions/DefiningFunctions
  :from_source: T
  :language: cpp
  :caption: Newton's Method for finding Square Root

  // returns the square root of a number as a double
  #include <iostream>
  using namespace std;

  double squareroot(double n) { /*return type double which indicates
                                  that a decimal is being returned*/
        double root = n / 2;

        for (int i = 0; i < 20; i++) {
                  root = (.5) * (root + (n / root));
        }

        return root;
  }

  int main() {
        cout << squareroot(9) << endl;
        cout << squareroot(4563) << endl;

        return 0;
  }