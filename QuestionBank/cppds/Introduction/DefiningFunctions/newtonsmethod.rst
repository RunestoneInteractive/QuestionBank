.. activecode:: newtonsmethod
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: DefiningFunctions
  :topics: Introduction/DefiningFunctions
  :from_source: T
  :language: cpp
  :caption: Newton's Method for finding Square Root

  #include <iostream>
  using namespace std;

  double squareroot(double n) { /*return type int which indicates
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