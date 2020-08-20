.. mchoice:: listSlice_MC_empty
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-slice
    :topics: 08-lists/08-slice
    :from_source: T
    :answer_a: []
    :answer_b: [3]
    :answer_c: [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
    :correct: c
    :feedback_a: An empty slice like this would not produce an empty list. Think about how the slice indexes.
    :feedback_b: This would be correct if the slice was [:1]
    :feedback_c: Omitting both indexes in a slice will create a copy of the whole list.
    :practice: T

    What is printed by the following statements?

    ::

      alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
      print(alist[:])