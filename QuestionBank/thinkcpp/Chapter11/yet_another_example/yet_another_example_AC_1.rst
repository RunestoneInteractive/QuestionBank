.. activecode:: yet_another_example_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: yet_another_example
   :topics: Chapter11/yet_another_example
   :from_source: T
   :language: cpp

   Feel free to try out the ``convertToSeconds()`` function in the active code below!
   ~~~~
   #include <iostream>
   using namespace std;

   struct Time {
       int hour, minute;
       double second;
       double convertToSeconds () const;
       void print ();
   };

   int main() {
       Time currentTime = { 9, 14, 30.0 };
       double secs = currentTime.convertToSeconds();

       cout << "The current time is "; currentTime.print(); cout << "." << endl;
       cout << "This time in seconds is " << secs << "." << endl;
   }

   ====

   void Time::print () {
     cout << hour << ":" << minute << ":" << second;
   }

   double Time::convertToSeconds () const {
     int minutes = hour * 60 + minute;
     double seconds = minutes * 60 + second;
     return seconds;
   }