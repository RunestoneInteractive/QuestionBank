.. mchoice:: qcbdm6_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cDeMorgans
   :topics: Conditionals/cDeMorgans
   :from_source: T
   :answer_a: (x > 5) && (y < 7)
   :answer_b: (x > 5) || (y < 7)
   :answer_c: (x > 5) && (y <= 7)
   :answer_d: (x > 5) || (y <= 7)
   :correct: d
   :feedback_a: The negation of && is || and the negation of y > 7 is y <= 7.
   :feedback_b: The negation of y > 7 is y <= 7.
   :feedback_c: The negation of && is ||.
   :feedback_d: The negation of (x <= 5) is (x > 5).  The negation of && is ||.  The negation of (y > 7) is (y <= 7).


   Which of the following is the same as the code below?

   .. code-block:: java

     !(x<= 5 && y > 7)