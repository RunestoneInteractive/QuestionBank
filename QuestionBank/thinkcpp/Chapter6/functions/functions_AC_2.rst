.. activecode:: functions_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: functions
  :topics: Chapter6/functions
  :from_source: T
  :language: cpp
  :caption: Two-dimensional tables

  #include <iostream>
  using namespace std;

  void all_operators(int x) {
      x = x * 2;
      x = x / 2;
      x = x + 2;
      x = x - 2;
      cout << x << endl;
  }

  int main() {
      all_operators(4);
      all_operators(13);
      all_operators(100);
      all_operators(22);
      all_operators(220);
      all_operators(0);
      all_operators(1000);
      all_operators(254);
  }