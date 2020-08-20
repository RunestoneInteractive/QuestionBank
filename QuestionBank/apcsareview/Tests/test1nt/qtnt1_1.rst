.. mchoice:: qtnt1_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: (a >= b) && (b >= 0)
   :answer_b: !(a > b) || !(b >= 0)
   :answer_c: (a >= b) || (b > 0)
   :answer_d: (a > b) || (b >= 0)
   :answer_e: (a > b) && (b >= 0)
   :correct: d
   :feedback_a: The "!" would negate everything inside the parentheses. There are a few mistakes here. The opposite of <= is not >= and the opposite of AND is OR.
   :feedback_b: Both of the expressions inside the parentheses were altered. If we wanted to distribute the negation symbol "!" then we would leave the expressions inside the parentheses alone.
   :feedback_c: Negating less than or equals (<=) results in greater than (>). In addition, less than (<) in the second argument should have been changed to greater than or equals (>=).
   :feedback_d: Using DeMorgan's Law we negate everything.  This includes our AND statement (which becomes an OR) and everything inside both parentheses.
   :feedback_e: Here we forgot to negate our AND (&&) into an OR (||).

   Which of the following is equivalent to the statement below? Recall DeMorgan's Law.

   .. code-block:: java

     !((a <= b) && (b < 0))