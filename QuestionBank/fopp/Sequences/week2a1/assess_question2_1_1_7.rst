.. mchoice:: assess_question2_1_1_7
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
   :correct: d
   :feedback_a: Not quite; .split() returns a list, each of whose elements is a string.
   :feedback_b: Not quite, look again at what types are present and what the result of .split() is.
   :feedback_c: Not quite, look again at what types are present and what the result of .split() is.
   :feedback_d: Yes, the .split() method returns a list.
   :practice: T

   What is the type of ``x``?

   .. sourcecode:: python

    b = "My, what a lovely day"
    x = b.split(',')