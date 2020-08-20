.. activecode:: tables_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: tables
  :topics: Chapter6/tables
  :from_source: T
  :language: cpp
  :caption: Tables

  If we wanted to find the logarithms of other powers of two,
  we could modify the program like this. Run the active code below.
  ~~~~
  #include <iostream>
  #include <cmath>
  using namespace std;

  int main() {
      double x = 1.0;
      while (x < 100.0) {
          cout << x << "\t" << log(x) / log(2.0) << endl;
          x = x * 2.0;
      }
  }