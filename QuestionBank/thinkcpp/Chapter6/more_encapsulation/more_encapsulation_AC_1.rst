.. activecode:: more_encapsulation_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: more_encapsulation
  :topics: Chapter6/more_encapsulation
  :from_source: T
  :language: cpp
  :caption: Two-dimensional tables

  The active code below uses the ``printMultTable`` function.
  Run the active code to see what happens!
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

  void printMultTable() {
      int i = 1;
      while (i <= 6) {
          printMultiples (i);
          i = i + 1;
      }
  }

  int main() {
      printMultTable();
  }