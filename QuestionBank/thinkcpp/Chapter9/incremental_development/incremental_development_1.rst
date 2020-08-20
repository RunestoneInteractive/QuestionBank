.. parsonsprob:: incremental_development_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: incremental_development
   :topics: Chapter9/incremental_development
   :from_source: T
   :numbered: left
   :adaptive:

   Let's write the code for the updated version of the ``increment`` function. ``increment``
   adds a number of seconds to a ``Time`` object and updates the values
   of the object. This version should use ``convertToSeconds`` and ``makeTime``.
   -----
   void increment (Time& time, double secs) {
   =====
   Time increment (Time& time, double secs) {                         #paired
   =====
      double seconds = convertToSeconds (time) + secs;
   =====
      double seconds = convertToSeconds (time);                        #paired
   =====
      time = makeTime (seconds);
   }
   =====
      return makeTime (seconds)                        #paired
   }