.. activecode:: rectangles_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter8
  :subchapter: rectangles
  :topics: Chapter8/rectangles
  :from_source: T
  :language: cpp

  The active code below uses the ``Rectangle`` structure. Feel free to
  modify the code and experiment around!
  ~~~~
  #include <iostream>
  using namespace std;

  struct Point {
      double x, y;
  };

  struct Rectangle {
      Point corner;
      double width, height;
  };

  int main() {
      Rectangle box = { { 0.0, 0.0 }, 100.0, 200.0 };
      box.width += 50.0;
      cout << box.height << endl;
      cout << box.width << endl;
  }