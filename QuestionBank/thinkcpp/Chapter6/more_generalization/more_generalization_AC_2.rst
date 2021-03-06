.. activecode:: more_generalization_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: more_generalization
  :topics: Chapter6/more_generalization
  :from_source: T
  :language: cpp
  :caption: Two-dimensional tables

  The active code below prints half the multiplication table.
  We can achieve this by replacing the ``printMultiples (i, high)`` in
  ``printMultTable`` with ``printMultiples (i, i)``.
  Run the active code to see what happens!
  ~~~~
  #include <iostream>
  using namespace std;

  void printMultiples (int n, int high) {
      int i = 1;
      while (i <= high) {
          cout << n*i << "\t";
          i = i + 1;
      }
      cout << endl;
  }

  void printMultTable (int high) {
      int i = 1;
      while (i <= high) {
          printMultiples (i, i);
          i = i + 1;
      }
  }

  int main() {
      printMultTable(7);
  }