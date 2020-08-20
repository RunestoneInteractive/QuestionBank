.. mchoice:: ePost_4_16
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPAbilitySummary
   :subchapter: Exercises
   :topics: CSPAbilitySummary/Exercises
   :from_source: T
   :answer_a: a = 7, b = 5, c = 0
   :answer_b: a = 5, b = 7, c = 7
   :answer_c: a = 5, b = 0, c = 7
   :answer_d: a = 5, b = 7, c = 0
   :answer_e: a = 5, b = 5, c = 7
   :correct: b
   :feedback_a: The variable a is set to 7 initially, but it is changed to the value of b which is 5.
   :feedback_b: While a starts at 7, b starts at 5 and c starts at 0, c is set to a copy of a's value, then a is set to a copy of b's value, and b is set to a copy of c's value.
   :feedback_c: Since b is set to 0 and c starts out a 0 this may seem right, but c is changed to a copy of the value in a before that.
   :feedback_d: Did you miss that c is set to a copy of the value in a?
   :feedback_e: Did you miss that b is set to a copy of the value in c and c is set to a copy of the value in a?

   What will be the values in a, b, and c after the following lines of code execute?

   ::

      a = 7;
      b = 5;
      c = 0;
      c = a;
      a = b;
      b = c;