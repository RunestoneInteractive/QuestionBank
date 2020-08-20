.. mchoice:: str-imm-mc-ball
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-immutable
    :topics: 06-strings/06-immutable
    :from_source: T
    :practice: T
    :answer_a: Ball
    :answer_b: Call
    :answer_c: Error
    :correct: c
    :feedback_a: Assignment is not allowed with strings.
    :feedback_b: Assignment is not allowed with strings.
    :feedback_c: Yes, strings are immutable.

    What is printed by the following statements:

    .. code-block:: python

      s = "Ball"
      s[0] = "C"
      print(s)