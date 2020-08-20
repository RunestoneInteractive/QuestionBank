.. parsonsprob:: time_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: time
   :topics: Chapter9/time
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the ``printTime`` function. ``printTime``
   should print out the time in the HOUR:MINUTE:SECONDS format.
   -----
   void printTime(Time& time) {
   =====
   Time printTime(Time& time) {                         #paired
   =====
      cout << time.hour << ":" << time.minute << ":" << time.second;
   =====
      cout << hour << ":" << minute << ":" << second;                        #paired
   }