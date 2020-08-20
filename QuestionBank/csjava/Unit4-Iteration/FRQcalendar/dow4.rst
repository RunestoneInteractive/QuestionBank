.. mchoice:: dow4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: FRQcalendar
   :topics: Unit4-Iteration/FRQcalendar
   :from_source: T
   :answer_a: firstDayOfYear(2019) + dayOfYear(1,8,2019)
   :answer_b: firstDayOfYear(2019) + dayOfYear(1,8,2019) - 1
   :answer_c: firstDayOfYear(2019) + dayOfYear(1,8,2019) % 7
   :answer_d: firstDayOfYear(2019) + dayOfYear(1,8,2019) - 1 % 4
   :answer_e: (firstDayOfYear(2019) + dayOfYear(1,8,2019) - 1) % 7
   :correct: e
   :feedback_a: This would return 10 but there are only 7 days of the week.
   :feedback_b: This would return 9 but there are only 7 days of the week.
   :feedback_c: Remember that % has precedence so this would return 2 + (8 % 7) = 2 + 1 = 3
   :feedback_d: Mod 4 does not make sense because there are 7 days of the week.
   :feedback_e: This would return (2 + 8 - 1) % 7 = 2.

   Which of the following expressions return the right value for the day of the week (2) for Jan. 8th 2019 given that firstDayOfYear(2019) returns 2 and dayOfYear(1,8,2019) returns 8?