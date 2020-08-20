.. activecode:: pure_function_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: pure_functions
  :topics: Chapter9/pure_functions
  :from_source: T
  :language: cpp

  One example is the function ``after``, which compares two ``Time``\ s and returns a
  ``bool`` that indicates whether the first operand comes after the second. Take a look
  at the active code below.
  ~~~~
  #include <iostream>
  using namespace std;

  struct Time {
      int hour, minute;
      double second;
  };

  bool after (Time& time1, Time& time2) {
      if (time1.hour > time2.hour) { return true; }
      if (time1.hour < time2.hour) { return false; }
      if (time1.minute > time2.minute) { return true; }
      if (time1.minute < time2.minute) { return false; }
      if (time1.second > time2.second) { return true; }
      return false;
  }

  int main () {
      Time time = { 11, 59, 3.14159 };
      Time time2 = { 1, 50, 3.14159 };
      cout << after(time, time2);
  }