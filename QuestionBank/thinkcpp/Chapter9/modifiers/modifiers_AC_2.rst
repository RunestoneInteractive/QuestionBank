.. activecode:: modifiers_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: modifiers
  :topics: Chapter9/modifiers
  :from_source: T
  :language: cpp

  The solution above is correct, but not very efficient. Can you think of a
  solution that does not require iteration? Try writing a more efficient version
  of ``increment`` in the commented section of the active code below. If you get stuck,
  you can reveal the extra problem at the end for help.
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
      // Write your implementation here.
  }

  int main() {
      Time t1 = { 9, 14, 30.0 };
      increment(t1, 60.0);
      // Should output "9:15:30"
      printTime (t1);

      Time t2 = { 9, 59, 45.0 };
      increment(t2, 120.0);
      // Should output "10:1:45"
      printTime (t2);
  }