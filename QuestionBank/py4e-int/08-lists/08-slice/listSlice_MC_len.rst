.. mchoice:: listSlice_MC_len
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-slice
    :topics: 08-lists/08-slice
    :from_source: T
    :answer_a: 2
    :answer_b: 3
    :answer_c: 4
    :answer_d: 5
    :correct: b
    :feedback_a: The list begins with the second item of L and includes everything up to but not including the last item.
    :feedback_b: Yes, there are 3 items in this list.
    :feedback_c: The list begins with the second item of L and includes everything up to but not including the last item.
    :feedback_d: The list begins with the second item of L and includes everything up to but not including the last item.
    :practice: T

    What is printed by the following statements?

    ::

      L = [0.34, '6', 'SI106', 'Python', -2]
      print(len(L[1:-1]))