.. activecode:: initialize_or_construct_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: initialize_or_construct
   :topics: Chapter11/initialize_or_construct
   :from_source: T
   :language: cpp

   In the active code below, you can experiment passing values into the two
   different constructors that we have defined on this page and the previous
   page.
   ~~~~
   #include <iostream>
   using namespace std;

   struct Time {
       int hour, minute;
       double second;
       Time (double secs);
       Time (int h, int m, double s);
       void print ();
   };

   int main() {
       Time marathon (9000);
       cout << "My marathon time is "; marathon.print(); cout << "." << endl;
       Time race (7, 30, 0.0);
       cout << "My next race is at "; race.print(); cout << "." << endl;
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