.. mchoice:: qtnt5_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test5nt
   :topics: Tests/test5nt
   :from_source: T
   :answer_a: double x = 0.6 * Math.random( ) + 0.4;
   :answer_b: double x = 0.4 * Math.random( ) + 0.6;
   :answer_c: double x = Math.random( ) - 0.4;
   :answer_d: double x = (double) (Math.random( ) * 0.4);
   :answer_e: double x = (double) (Math.random( ) + 0.6);
   :correct: b
   :feedback_a: This gives .4 <= x <1
   :feedback_b: Math.random() returns 0(inclusive) to 1(exclusive) so this makes 0 + .6 the lower bound, and .99999 the upper bound
   :feedback_c: This gives -.4 <= x < 6
   :feedback_d: This doesn't ensure lower bound and upper bound
   :feedback_e: This doesn't ensure lower bound and upper bound

   Which of the following code segments correctly stores in ``x`` a random real number such that ``0.6 <= x < 1``?