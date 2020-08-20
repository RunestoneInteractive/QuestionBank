.. activecode:: modifiers_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: modifiers
  :topics: Chapter9/modifiers
  :from_source: T
  :language: cpp

  The active code below uses the ``increment`` function. Run the active code to
  see what the output is!
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

  void increment (Time& time, double secs) {
      time.second += secs;
      while (time.second >= 60.0) {
          time.second -= 60.0;
          time.minute += 1;
      }
      while (time.minute >= 60) {
          time.minute -= 60;
          time.hour += 1;
      }
  }

  int main() {
      Time currentTime = { 9, 14, 30.0 };
      increment(currentTime, 60.0);
      printTime (currentTime);
  }