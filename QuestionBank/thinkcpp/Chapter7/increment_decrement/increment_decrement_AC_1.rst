.. activecode:: increment_decrement_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: increment_decrement
  :topics: Chapter7/increment_decrement
  :from_source: T
  :language: cpp
  :caption: Looping and counting

  The active code demonstrates how using increment operators
  with ``cout`` statements can be confusing.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      int x = 0;
      // We incremented x, so it should print out 1 now right?
      cout << x++ << endl; // Weird, x is still 0?
  }