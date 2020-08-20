.. mchoice:: qpret_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: hours = hours + minutes / 60; minutes = minutes % 60;
    :answer_b: minutes = minutes % 60;
    :answer_c: minutes = minutes + hours % 60;
    :answer_d: hours = hours + minutes % 60; minutes = minutes / 60;
    :answer_e: hours = hours + minutes / 60;
    :correct: a
    :feedback_a: This will update the hours and minutes correctly. It will add the floor of the division of minutes by 60 to hours and then set minutes to the remainder of the division of minutes by 60.
    :feedback_b: This won't add to hour so it can't be correct. It will set minutes to the remainder of dividing minutes by 60 so minutes will be set correctly.
    :feedback_c: This will set the minutes to the minutes plus the remainder of dividing the hours by 60.
    :feedback_d: This will set hours to hours plus the remainder of dividing minutes by 60 and then set minutes to the number of hours (int division of minutes by 60).
    :feedback_e: This will correctly update the hours, but not update the minutes.

    Given the following incomplete class declaration, which of the following can be used to replace the missing code in the ``advance`` method so that it will correctly update the time?

    .. code-block:: java

        public class TimeRecord
        {
           private int hours;
           private int minutes; // 0<=minutes<60

           public TimeRecord(int h, int m)
           {
              hours = h;
              minutes = m;
           }

           // postcondition: returns the
           // number of hours
           public int getHours()
           { /* implementation not shown */ }

           // postcondition: returns the number
           // of minutes; 0 <= minutes < 60
           public int getMinutes()
           { /* implementation not shown */ }

           // precondition: h >= 0; m >= 0
           // postcondition: adds h hours and
           // m minutes to this TimeRecord
           public void advance(int h, int m)
           {
              hours = hours + h;
              minutes = minutes + m;
              /* missing code */
           }

           // ... other methods not shown

       }