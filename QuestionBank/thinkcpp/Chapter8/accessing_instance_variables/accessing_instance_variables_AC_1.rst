.. activecode:: accessing_instance_variables_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter8
  :subchapter: accessing_instance_variables
  :topics: Chapter8/accessing_instance_variables
  :from_source: T
  :language: cpp

  In the active code below, we access the instance variables of ``Point`` object
  ``black`` using dot notation and output their values. Next, we output the
  distance from the origin.
  ~~~~
  #include <iostream>
  #include <cmath>
  using namespace std;

  struct Point {
      double x, y;
  };

  int main() {
      Point blank;
      blank.x = 3.0;
      blank.y = 4.0;
      cout << blank.x << ", " << blank.y << endl;
      double distance = sqrt(blank.x * blank.x + blank.y * blank.y);
      cout << distance << endl;
  }