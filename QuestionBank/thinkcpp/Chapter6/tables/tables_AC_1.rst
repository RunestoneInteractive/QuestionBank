.. activecode:: tables_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: tables
  :topics: Chapter6/tables
  :from_source: T
  :language: cpp
  :caption: Tables

  The active code below outputs a sequence of values in the left column
  and their logarithms in the right column.
  ~~~~
  #include <iostream>
  #include <cmath>
  using namespace std;

  int main() {
      double x = 1.0;
      while (x < 10.0) {
          cout << x << "\t" << log(x) << "\n";
          x = x + 1.0;
      }
      return 0;
  }