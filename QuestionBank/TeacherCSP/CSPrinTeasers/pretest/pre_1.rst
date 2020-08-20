.. mchoice:: pre_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPrinTeasers
   :subchapter: pretest
   :topics: CSPrinTeasers/pretest
   :from_source: T
   :answer_a: x = 7, y = 5, z = 0
   :answer_b: x = 5, y = 7, z = 7
   :answer_c: x = 5, y = 7, z = 0
   :answer_d: x = 5, y = 5, z = 7
   :answer_e: I don't know
   :correct: b
   :feedback_a: Those are the original values, but they change.
   :feedback_b: x is set to 7 but changed to the value of y which is 5.  y is set to 5 originally, but is changed to the value of z but after z has been set to the value of x which is 7.  z was set to 0 originally but changes to the the value of x which is 7.
   :feedback_c: This would be true if setting y to z reset z to 0, but that is not what happens.
   :feedback_d: y was set to 5 originally, but the value was changed.
   :feedback_e: That is okay.  We do not expect you to know this.

   What will be the values in x, y, and z after the following lines of code execute?

   ::

      x = 7;
      y = 5;
      z = 0;
      z = x;
      x = y;
      y = z;