.. activecode:: encapsulation_generalization_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: encapsulation_generalization
  :topics: Chapter6/encapsulation_generalization
  :from_source: T
  :language: cpp
  :caption: Two-dimensional tables

  The active code below uses tab characters to make the table neater.
  ~~~~
  #include <iostream>
  using namespace std;

  void printMultiples (int n) {
      int i = 1;
      while (i <= 6) {
          cout << n*i << '\t';
          i = i + 1;
      }
      cout << endl;
  }

  int main() {
      int i = 1;
      while (i <= 6) {
          printMultiples (i);
          i = i + 1;
      }
  }