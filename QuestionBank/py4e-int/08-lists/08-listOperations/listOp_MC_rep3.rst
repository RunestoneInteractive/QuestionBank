.. mchoice:: listOp_MC_rep3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listOperations
    :topics: 08-lists/08-listOperations
    :from_source: T
    :practice: T
    :answer_a: 9
    :answer_b: [1, 1, 1, 3, 3, 3, 5, 5, 5]
    :answer_c: [1, 3, 5, 1, 3, 5, 1, 3, 5]
    :answer_d: [3, 9, 15]
    :correct: c
    :feedback_a: Repetition does not multiply the lengths of the lists.  It repeats the items.
    :feedback_b: Repetition does not repeat each item individually.
    :feedback_c: Yes, the items of the list are repeated 3 times, one after another.
    :feedback_d: Repetition does not multiply the individual items.

    What is printed by the following statements?

    ::

      alist = [1, 3, 5]
      print(alist * 3)