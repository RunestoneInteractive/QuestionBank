.. mchoice:: qtnt2_18
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: (x <= 7) && (y < 12)
   :answer_b: (x <= 7) || (y < 12)
   :answer_c: (x > 7) || (y >= 12)
   :answer_d: (x > 7) && (y >= 12)
   :answer_e: (x <= 7) || (y >= 12)
   :correct: b
   :feedback_a: Use A and B to represent the expressions -- A == (x > 7), B == !(y < 12). The AND needs to be changed to an OR.
   :feedback_b: Use A and B to represent the expressions -- A == (x > 7), B == !(y < 12)Using DeMorgan's law, !(A && B) is equivalent to !A || !B. The negation of (x > 7) is (x <= 7), and the negation of !(y < 12) is (y < 12).
   :feedback_c: Use A and B to represent the expressions -- A == (x > 7), B == !(y < 12)!(A && B) is NOT equivalent to (A || B). It should be (!A || !B). Also, (y >= 12) is equivalent to !(y < 12).
   :feedback_d: Use A and B to represent the expressions -- A == (x > 7), B == !(y < 12)!(A && B) is NOT equivalent to (A && B). !(y < 12) and (y >=12) mean the same thing; changing this does not make the statement the opposite.
   :feedback_e: Use A and B to represent the expressions -- A == (x > 7), B == !(y < 12)!(A && B) is NOT equivalent to (!A && B). Changing !(y < 12) to (y >= 12) does not negate the statement; these two are equivalent.

   Which statement is equivalent to ``!( (x > 7) && !(y < 12) )``?