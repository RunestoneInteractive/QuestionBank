.. mchoice:: cndtnl-altex-mc-print
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-altExecution
    :topics: 03-conditional/03-altExecution
    :from_source: T
    :practice: T
    :answer_a: TRUE
    :answer_b: FALSE
    :answer_c: TRUE on one line and FALSE on the next
    :answer_d: Nothing will be printed
    :correct: b
    :feedback_a: TRUE is printed by the if-block, which only executes if the conditional (in this case, 4+5 == 10) is true.  In this case 5+4 is not equal to 10.
    :feedback_b: Since 4+5==10 evaluates to False, Python will skip over the if block and execute the statement in the else block.
    :feedback_c: Python would never print both TRUE and FALSE because it will only execute one of the if-block or the else-block, but not both.
    :feedback_d: Python will always execute either the if-block (if the condition is true) or the else-block (if the condition is false).  It would never skip over both blocks.

    What does the following code print?

    .. code-block:: python

      if 4 + 5 == 10:
          print("TRUE")
      else:
          print("FALSE")