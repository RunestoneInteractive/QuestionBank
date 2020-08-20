.. mchoice:: listDel_MC_pop
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-deleteElement
    :topics: 08-lists/08-deleteElement
    :from_source: T
    :practice: T
    :answer_a: [4, 8, 6]
    :answer_b: [2, 6, 5]
    :answer_c: [4, 2, 6]
    :correct: c
    :feedback_a: pop(2) removes the item at index 2, not the 2 itself.
    :feedback_b: pop() removes the last item, not the first.
    :feedback_c: Yes, first the 8 was removed, then the last item, which was 5.

    What is printed by the following statements?

    ::

      alist = [4, 2, 8, 6, 5]
      temp = alist.pop(2)
      temp = alist.pop()
      print(alist)