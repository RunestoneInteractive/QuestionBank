.. activecode:: print_AC_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: print
   :topics: Chapter11/print
   :from_source: T
   :language: cpp

   Feel free to mess around with input for ``currentTime`` in the active code below!
   ~~~~
   #include <iostream>
   using namespace std;

   struct Time {
       int hour, minute;
       double second;

       void print ();
   };

   int main() {
       Time currentTime = { 9, 14, 30.0 };
       currentTime.print ();
   }

   ====
   void Time::print () {
     cout << hour << ":" << minute << ":" << second << endl;
   }