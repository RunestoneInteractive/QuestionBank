.. activecode:: more_complicated_example_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: a_more_complicated_example
   :topics: Chapter11/a_more_complicated_example
   :from_source: T
   :language: cpp

   The active code below is another practical example using the ``after`` function.
   Feel free to modify the time that school gets out, and the time that the track meet starts, if you wish!
   ~~~~
   #include <iostream>
   using namespace std;

   struct Time {
       int hour, minute;
       double second;
       bool after (const Time& time2) const;
   };

   int main() {
       Time end_school = { 2, 20, 0.0 };
       Time track_meet = { 1, 30, 0.0 };
       if (track_meet.after (end_school)) {
           cout << "The track meet starts after school is dismissed." << endl;
       }
       else {
           cout << "The track meet starts before school gets out, athletes will get an early dismissal." << endl;
       }
   }

   ====

   bool Time::after (const Time& time2) const {
     if (hour > time2.hour) return true;
     if (hour < time2.hour) return false;

     if (minute > time2.minute) return true;
     if (minute < time2.minute) return false;

     if (second > time2.second) return true;
     return false;
   }