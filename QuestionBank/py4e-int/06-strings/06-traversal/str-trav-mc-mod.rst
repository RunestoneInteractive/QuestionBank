.. mchoice:: str-trav-mc-mod
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
    :answer_c: 4
    :answer_d: Error, the for statement cannot have an if inside.
    :correct: c
    :feedback_a: The for loop visits each index but the selection only prints some of them.
    :feedback_b: Yes, it will print all the characters in even index positions and the i character appears twice in an even location.
    :feedback_c: i is at positions 1, 4, 7, and 10.
    :feedback_d: The for statement can have any statements inside, including if as well as for.


    How many times is the letter i printed by the following statements?

    .. code-block:: python

      s = "mississippi"
      for idx in range(len(s)):
          if idx % 2 == 0:
              print(s[idx])