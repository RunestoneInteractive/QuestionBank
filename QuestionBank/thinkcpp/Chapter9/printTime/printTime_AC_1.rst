.. activecode:: printTime_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: printTime
  :topics: Chapter9/printTime
  :from_source: T
  :language: cpp

  In the active code below, the output of this function, if we pass ``time`` an argument, is
  ``11:59:3.14159``.
  ~~~~
  #include <iostream>
  using namespace std;

  struct Time {
      int hour, minute;
      double second;
  };

  void printTime (Time& t) {
      cout << t.hour << ":" << t.minute << ":" << t.second << endl;
  }

  int main () {
      Time time = { 11, 59, 3.14159 };
      printTime(time);
  }