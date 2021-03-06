.. activecode:: incremental_development_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter9
  :subchapter: incremental_development
  :topics: Chapter9/incremental_development
  :from_source: T
  :language: cpp

  The active code below uses the ``convertToSeconds`` and ``makeTime`` functions.
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

  double convertToSeconds (const Time& t) {
      int minutes = t.hour * 60 + t.minute;
      double seconds = minutes * 60 + t.second;
      return seconds;
  }

  Time makeTime (double secs) {
      Time time;
      time.hour = int (secs / 3600.0);
      secs -= time.hour * 3600.0;
      time.minute = int (secs / 60.0);
      secs -= time.minute * 60;
      time.second = secs;
      return time;
  }

  Time addTime (const Time& t1, const Time& t2) {
      double seconds = convertToSeconds (t1) + convertToSeconds (t2);
      return makeTime (seconds);
  }

  int main() {
      Time currentTime = { 9, 14, 30.0 };
      Time otherTime = { 10, 32, 15.2 };
      Time doneTime = addTime(currentTime, otherTime);
      printTime (doneTime);
  }