.. mchoice:: listOp_MC_AplusB
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-listOperations
    :topics: 08-lists/08-listOperations
    :from_source: T
    :practice: T
    :answer_a: 6
    :answer_b: [1, 2, 3, 4, 5, 6]
    :answer_c: [1, 3, 5, 2, 4, 6]
    :answer_d: [3, 7, 11]
    :correct: c
    :feedback_a: Concatenation does not add the lengths of the lists.
    :feedback_b: Concatenation does not reorder the items.
    :feedback_c: Yes, a new list with all the items of the first list followed by all those from the second.
    :feedback_d: Concatenation does not add the individual items.

    What is printed by the following statements?

    ::

      alist = [1, 3, 5]
      blist = [2, 4, 6]
      print(alist + blist)