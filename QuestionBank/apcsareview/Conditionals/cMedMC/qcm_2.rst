.. mchoice:: qcm_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: cMedMC
   :topics: Conditionals/cMedMC
   :from_source: T
   :answer_a: x = 0;
   :answer_b: if (x > 2) x *= 2;
   :answer_c: if (x > 2) x = 0;
   :answer_d: if (x > 2) x = 0; else x *= 2;
   :correct: c
   :feedback_a: If x was set to 1 then it would still equal 1.
   :feedback_b: What happens in the original when x is greater than 2?
   :feedback_c: If x is greater than 2 it will be set to 0.
   :feedback_d: In the original what happens if x is less than 2?  Does this give the same result?

   Which of the following is equivalent to the code segment below?

   .. code-block:: java

     if (x > 2) x = x * 2;
     if (x > 4) x = 0;