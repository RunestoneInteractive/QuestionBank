.. mchoice:: cndtnl-chain-mc-grades
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-chained
    :topics: 03-conditional/03-chained
    :from_source: T
    :practice: T
    :answer_a: A
    :answer_b: B
    :answer_c: C
    :answer_d: D
    :answer_e: E
    :correct: a
    :feedback_a: Because the first statement is satisfied, it does not continue to the following elif or else statements.
    :feedback_b: Try again. This code skips the elif/else statements once an if/elif statement has been satisfied.
    :feedback_c: Try again. This code skips the elif/else statements once an if/elif statement has been satisfied.
    :feedback_d: Try again. This code skips the elif/else statements once an if/elif statement has been satisfied.
    :feedback_e: This will only be true when score does not satisfy the other if/elif statements (so it will only execute when score < 60).

    If x = 93, what will print when the following code executes?

    ::

      if score >= 90:
          grade = "A"
      elif score >= 80:
          grade = "B"
      elif score >= 70:
          grade = "C"
      elif score >= 60:
          grade = "D"
      else:
          grade = "E"
      print(grade)