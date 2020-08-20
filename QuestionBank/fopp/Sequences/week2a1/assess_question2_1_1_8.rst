.. mchoice:: assess_question2_1_1_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: T
   :answer_a: string
   :answer_b: integer
   :answer_c: float
   :answer_d: list
   :correct: a
   :feedback_a: Yes, the string is split into a list, then joined back into a string, then split again, and finally joined back into a string.
   :feedback_b: Not quite, look again at what types are present and what the result of .split() is.
   :feedback_c: Not quite, look again at what types are present and what the result of .split() is.
   :feedback_d: Not quite, think about what .split() and .join() return.
   :practice: T
   :topics: Sequences/SplitandJoin

   What is the type of ``a``?

   .. sourcecode:: python

    b = "My, what a lovely day"
    x = b.split(',')
    z = "".join(x)
    y = z.split()
    a = "".join(y)