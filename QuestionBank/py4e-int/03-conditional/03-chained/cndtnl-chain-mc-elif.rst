.. mchoice:: cndtnl-chain-mc-elif
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-chained
    :topics: 03-conditional/03-chained
    :from_source: T
    :practice: T
    :answer_a: a
    :answer_b: b
    :answer_c: c
    :correct: c
    :feedback_a: While the value in x is less than the value in y (3 is less than 5) it is not less than the value in z (3 is not less than 2).
    :feedback_b: The value in y is not less than the value in x (5 is not less than 3).
    :feedback_c: Since the first two Boolean expressions are false the else will be executed.

    What will the following code print if x = 3, y = 5, and z = 2?

    .. code-block:: python

      if x < y and x < z:
          print("a")
      elif y < x and y < z:
          print("b")
      else:
          print("c")