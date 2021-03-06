.. activecode:: one_last_example_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: one_last_example
   :topics: Chapter11/one_last_example
   :from_source: T
   :language: cpp

   Feel free to try out the ``add`` function in the active code below!
   ~~~~
   #include <iostream>
   using namespace std;

   struct Time {
       int hour, minute;
       double second;
       Time (double secs);
       Time (int h, int m, double s);
       bool after (const Time& time2) const;
       Time add (const Time& t2) const;
       double convertToSeconds () const;
       void print ();
   };

   int main() {
       Time t1 (9, 20, 0.0); cout << "t1 = "; t1.print(); cout << endl;
       Time t2 (7, 30, 0.0); cout << "t2 = "; t2.print(); cout << endl;
       Time t3 = t1.add(t2);
       cout << "Time t1 + Time t2 = "; t3.print(); cout << endl;
   }

   ====

   Time::Time (double secs) {
     hour = int (secs / 3600.0);
     secs -= hour * 3600.0;
     minute = int (secs / 60.0);
     secs -= minute * 60.0;
     second = secs;
   }

   Time::Time (int h, int m, double s) {
     hour = h; minute = m; second = s;
   }

   void Time::print () {
     cout << hour << ":" << minute << ":" << second;
   }

   double Time::convertToSeconds () const {
     int minutes = hour * 60 + minute;
     double seconds = minutes * 60 + second;
     return seconds;
   }

   Time Time::add (const Time &t2) const {
     double seconds = convertToSeconds () + t2.convertToSeconds ();
     Time time (seconds);
     return time;
   }

   bool Time::after (const Time& time2) const {
     if (hour > time2.hour) return true;
     if (hour < time2.hour) return false;

     if (minute > time2.minute) return true;
     if (minute < time2.minute) return false;

     if (second > time2.second) return true;
     return false;
   }