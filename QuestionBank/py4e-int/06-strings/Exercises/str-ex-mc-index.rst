.. mchoice:: str-ex-mc-index
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: Exercises
    :topics: 06-strings/Exercises
    :from_source: T
    :practice: T
    :answer_a: yyyyy
    :answer_b: 55555
    :answer_c: n
    :answer_d: Error, you cannot combine all those things together.
    :correct: a
    :feedback_a: Yes, s[1] is y and the index of n is 5, so 5 y characters.  It is important to realize that the index method has precedence over the repetition operator.  Repetition is done last.
    :feedback_b: Close.  5 is not repeated, it is the number of times to repeat.
    :feedback_c: This expression uses the index of n
    :feedback_d: This is fine, the repetition operator used the result of indexing and the index method.


    What is printed by the following statements?

    .. code-block:: python

      s = "python rocks"
      print(s[1] * s.index("n"))