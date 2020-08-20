.. mchoice:: str-len-mc-apple
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-length
    :topics: 06-strings/06-length
    :from_source: T
    :practice: T
    :answer_a: l
    :answer_b: p
    :answer_c: a
    :answer_d: Error, len(s) is 12 and there is no index 12.
    :correct: b
    :feedback_a: Take a look at the index calculation again, len(s)-5.
    :feedback_b: Yes, len(s) is 12 and 12-5 is 7.  Use 7 as index and remember to start counting with 0.
    :feedback_c: a is at index 6
    :feedback_d: You subtract 5 before using the index operator so it will work.


    What is printed by the following statements?

    .. code-block:: python

      s = "green apples"
      print(s[len(s)-5])