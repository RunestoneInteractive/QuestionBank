.. mchoice:: str-ex-mc-print
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: t
    :answer_b: h
    :answer_c: c
    :answer_d: Error, you cannot use the [ ] operator with a string.
    :correct: b
    :feedback_a: Index locations do not start with 1, they start with 0.
    :feedback_b: Yes, index locations start with 0.
    :feedback_c: s[-3] would return c, counting from right to left.
    :feedback_d: [ ] is the index operator


    What is printed by the following statements?

    .. code-block:: python

      s = "python rocks"
      print(s[3])