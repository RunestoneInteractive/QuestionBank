.. activecode:: pure_function_AC_3
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: pure_functions
  :topics: Chapter9/pure_functions
  :from_source: T
  :language: cpp

  The active code below is the corrected version of ``addTime``.
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

  Time addTime (Time& t1, Time& t2) {
      Time sum;
      sum.hour = t1.hour + t2.hour;
      sum.minute = t1.minute + t2.minute;
      sum.second = t1.second + t2.second;
      if (sum.second >= 60.0) {
          sum.second -= 60.0;
          sum.minute += 1;
      }
      if (sum.minute >= 60) {
          sum.minute -= 60;
          sum.hour += 1;
      }
      return sum;
  }

  int main() {
      Time currentTime = { 9, 14, 30.0 };
      Time breadTime = { 3, 35, 0.0 };
      Time doneTime = addTime (currentTime, breadTime);
      printTime (doneTime);
  }