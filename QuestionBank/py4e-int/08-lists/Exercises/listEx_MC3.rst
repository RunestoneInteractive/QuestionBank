.. mchoice:: listEx_MC3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: Exercises
    :topics: 08-lists/Exercises
    :from_source: T
    :practice: T
    :answer_a: Error, you cannot use the upper method on a list.
    :answer_b: 2
    :answer_c: CAT
    :correct: c
    :feedback_a: alist[2] is the string cat so the upper method is legal
    :feedback_b: 2 is the index.  We want the item at that index.
    :feedback_c: Yes, the string cat is upper cased to become CAT.

    What is printed by the following statements?

    ::

      alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
      print(alist[2].upper())