.. activecode:: call_by_value_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter8
  :subchapter: call_by_value
  :topics: Chapter8/call_by_value
  :from_source: T
  :language: cpp

  Take a look at the active code below. Notice from the output of the code below how the
  function ``addTwo`` changes the instance variables, but not on ``blank`` itself.
  ~~~~
  #include <iostream>
  using namespace std;

  struct Point {
      double x, y;
  };

  void addTwo (Point p) {
      cout << "(" << p.x + 2 << ", " << p.y + 2 << ")" << endl;
  }

  int main() {
      Point blank = { 3.0, 4.0 };
      addTwo (blank);
      cout << "(" << blank.x << "," << blank.y << ")" << endl;
  }