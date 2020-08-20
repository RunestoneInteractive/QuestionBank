.. mchoice:: str-count-mc-t
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-count
    :topics: 06-strings/06-count
    :from_source: T
    :practice: T
    :answer_a: 1
    :answer_b: 2
    :answer_c: 3
    :answer_d: 4
    :correct: d
    :feedback_a: This is the value count starts at.
    :feedback_b: The letter t appears more than 2 times in "peanut butter".
    :feedback_c: Keep in mind the value count starts at.
    :feedback_d: Correct! Count starts at 1 and then increases 3 times - 1 for each t in "peanut butter".

    What is printed by the following statements:

    .. code-block:: python

      s = "peanut butter"
      count = 1
      for char in s:
          if char is t:
          count += 1
      print(count)