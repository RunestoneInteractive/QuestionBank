.. mchoice:: str-trav-mc-plus2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-traversal
    :topics: 06-strings/06-traversal
    :from_source: T
    :practice: T
    :answer_a: 1
    :answer_b: 2
    :answer_c: 3
    :correct: a
    :feedback_a: Yes, idx goes through the odd numbers starting at 1. r is at position 2, 7, and 8.
    :feedback_b: r is at positions 2, 7, and 8. idx starts at 1, not 0.
    :feedback_c: There are 3 r characters but idx does not take on the correct index values.


    How many times is the letter r printed by the following statements?

    .. code-block:: python

      s = "strawberry"
      idx = 1
      while idx < len(s):
          print(s[idx])
          idx = idx + 2