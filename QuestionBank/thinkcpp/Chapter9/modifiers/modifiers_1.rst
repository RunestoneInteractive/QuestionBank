.. parsonsprob:: modifiers_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: modifiers
   :topics: Chapter9/modifiers
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 6.0

   Let's write the code for the ``increment`` function. ``increment``
   adds a number of seconds to a ``Time`` object and updates the values
   of the object.
   -----
   void increment (Time& time, double secs) {
   =====
   void increment (const Time& time, double secs) {                         #paired
   =====
      int mins = (time.second + secs) / 60;
   =====
      int mins = (time.second + secs) % 60;                        #paired
   =====
      time.second = time.second + secs - 60 * mins;
   =====
      time.second = time.second + secs;                        #paired
   =====
      int hours = (time.minute + mins) / 60;
   =====
      int hours = (time.second + second) / 60;                        #paired
   =====
      time.minute = time.minute + mins - 60 * hours;
   =====
      time.second = time.minute + mins - 60 * hours;                        #paired
   =====
      time.hour += hours;
   }