.. mchoice:: listMut_MC_in
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-mutable
    :topics: 08-lists/08-mutable
    :from_source: T
    :practice: T
    :answer_a: True
    :answer_b: False
    :correct: b
    :feedback_a: in returns True for top level items only.  57 is in a sublist.
    :feedback_b: Yes, 57 is not a top level item in alist.  It is in a sublist.

    What is printed by the following statements?

    ::

      alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
      print(57 in alist)