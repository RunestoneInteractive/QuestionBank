.. mchoice:: str-ex-mc-ball
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: Ball
    :answer_b: BALL
    :answer_c: LLAB
    :correct: c
    :feedback_a: Each item is converted to upper case before concatenation.
    :feedback_b: Each character is converted to upper case but the order is wrong.
    :feedback_c: Yes, the order is reversed due to the order of the concatenation.

    What is printed by the following statements:

    .. code-block:: python

      s = "ball"
      r = ""
      for item in s:
          r = item.upper() + r
      print(r)