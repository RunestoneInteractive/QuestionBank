.. mchoice:: qtnt4_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: (x >= 7) && (x > 2)
   :answer_b: (x < 7) && (x <= 2)
   :answer_c: (x >= 7) && (x < 2)
   :answer_d: (x >= 7) || (x <= 2)
   :answer_e: (x < 7) || (x < 2)
   :correct: d
   :feedback_a: Use A and B to represent the expressions -- A becomes !(x >= 7), B becomes (x > 2). ! (A && B) does NOT equal !A && B.
   :feedback_b: Use A and B to represent the expressions -- A becomes !(x >= 7), B becomes (x > 2). ! (A && B) does NOT equal A && !B. !(x >= 7) is the same as (x < 7).
   :feedback_c: Use A and B to represent the expressions -- A becomes !(x >= 7), B becomes (x > 2). ! (A && B) does NOT equal !A && !B. Also, the negation of (x > 2) is (x <= 2), not (x < 2).
   :feedback_d: Use A and B to represent the expressions -- A becomes !(x >= 7), B becomes (x > 2). ! (A && B) is equal to !A && !B, according to DeMorgan's law. The negation of !(x >= 7) is (x >= 7), and the negation of (x > 2) is (x <= 2).
   :feedback_e: Use A and B to represent the expressions -- A becomes !(x >= 7), B becomes (x > 2). ! (A && B) does NOT equal A || !B. The negation of (x > 2) is (x <= 2), not (x < 2), and !(x >= 7) is the same as (x < 7).

   Which of the following is equivalent to ``! (!(x >= 7) && (x > 2))``?