.. mchoice:: str-ex-mc-add
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: tr
    :answer_b: ps
    :answer_c: nn
    :answer_d: Error, you cannot use the [ ] operator with the + operator.
    :correct: a
    :feedback_a: Yes, indexing operator has precedence over concatenation.
    :feedback_b: p is at location 0, not 2.
    :feedback_c: n is at location 5, not 2.
    :feedback_d: [ ] operator returns a string that can be concatenated with another string.


    What is printed by the following statements?

    .. code-block:: python

      s = "python rocks"
      print(s[2] + s[-5])