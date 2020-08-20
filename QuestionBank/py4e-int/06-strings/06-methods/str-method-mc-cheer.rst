.. mchoice:: str-method-mc-cheer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-methods
    :topics: 06-strings/06-methods
    :from_source: T
    :practice: T
    :answer_a: 0
    :answer_b: 2
    :answer_c: 3
    :correct: c
    :feedback_a: There are definitely e and b characters.
    :feedback_b: There are 2 e characters but what about b?
    :feedback_c: Yes, add the number of e characters and the number of b characters.


    What is printed by the following statements?

    .. code-block:: python

      s = "let's go blue!"
      print(s.count("e") + s.count("b"))