.. mchoice:: qtnt5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test5nt
   :topics: Tests/test5nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II only
   :answer_e: II and III only
   :correct: e
   :feedback_a: We don't know the value of z
   :feedback_b: II is true but there is (are) other statements that evaluate to true
   :feedback_c: III is true but there is (are) other statements that evaluate to true
   :feedback_d: For I, we don't know the value of z
   :feedback_e: III executes to true if either a||b true, III is true because x-y will become 0 then 0 * a *b... = 0

   Suppose ``x, y, and z`` are variables of type ``int``. Consider the following three conditions
      I. (x == y) && (y == z)  && (x == z)
      II. (x==y) || (y==z) && (x == z)
      III. (x - y) * (x - z) * (y - z) == 0

      Which of these conditions is (are) always true if x == y is true?