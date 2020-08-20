.. activecode:: time_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: time
  :topics: Chapter9/time
  :from_source: T
  :language: cpp

  Try writing the ``printTime`` function in the commented section
  of the active code below. ``printTime`` should print out the time
  in the HOUR:MINUTE:SECONDS format. If you get stuck, you can reveal the extra problem
  at the end for help.
  ~~~~
  #include <iostream>
  using namespace std;

  struct Time {
      int hour, minute;
      double second;
  };

  void printTime(Time& time) {
      // ``printTime`` should print out the time in the
      // HOUR:MINUTE:SECONDS format. Write your implementation here.
  }

  int main() {
      Time time = { 11, 59, 3.14159 };

      // Should output "11:59:3.14159"
      printTime(time);
  }