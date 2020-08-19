.. mchoice:: fillin_functions_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter9
   :subchapter: fillin_functions
   :topics: Chapter9/fillin_functions
   :from_source: T
   :answer_a: Time& t1
   :answer_b: Time& t2
   :answer_c: Time& sum
   :correct: c
   :feedback_a: Try again.
   :feedback_b: Try again.
   :feedback_c: Correct!
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Which parameter is not declared as a ``const``?
   
   .. code-block:: cpp
   
      void addTimeFill (const Time& t1, const Time& t2, Time& sum) {
        sum.hour = t1.hour + t2.hour;
        sum.minute = t1.minute + t2.minute;
        sum.second = t1.second + t2.second;
   
        if (sum.second >= 60.0) {
          sum.second -= 60.0;
          sum.minute += 1;
        }
        if (sum.minute >= 60) {
          sum.minute -= 60;
          sum.hour += 1;
        }
      }