.. mchoice:: listDel_MC_pop2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-deleteElement
    :topics: 08-lists/08-deleteElement
    :from_source: T
    :practice: T
    :answer_a: [2, 8, 6, 5]
    :answer_b: [4, 2, 8, 6, 5]
    :answer_c: 4
    :answer_d: None
    :correct: c
    :feedback_a: alist is now the value that was returned from pop(0).
    :feedback_b: pop(0) changes the list by removing the first item.
    :feedback_c: Yes, first the 4 was removed from the list, then returned and assigned to alist.  The list is lost.
    :feedback_d: pop(0) returns the first item in the list so alist has now been changed.

    What is printed by the following statements?

    ::

      alist = [4, 2, 8, 6, 5]
      alist = alist.pop(0)
      print(alist)