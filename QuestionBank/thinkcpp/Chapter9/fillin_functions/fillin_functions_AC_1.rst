.. activecode:: fillin_functions_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: fillin_functions
  :topics: Chapter9/fillin_functions
  :from_source: T
  :language: cpp

  The active code below uses the fill-in version of the ``addTime`` function.
  Feel free to modify the code!
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

  void addTimeFill (const Time& t1, const Time& t2, Time& sum) {
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
  }

  int main() {
      Time currentTime = { 5, 45, 30.0 };
      Time bakingTime = {0, 55, 0.0 };
      Time finishedTime; // We'll store the sum in this variable
      addTimeFill (currentTime, bakingTime, finishedTime);
      cout << "The bread will be ready at ";
      printTime (finishedTime);
  }