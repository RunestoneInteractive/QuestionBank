.. mchoice:: listEx_MC1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: Exercises
    :topics: 08-lists/Exercises
    :from_source: T
    :practice: T
    :answer_a: [ [ ], 3.14, False]
    :answer_b: ["cat", [56, 57, "dog"]]
    :answer_c: [ [56, 57, "dog"], [ ], 3.14, False]
    :correct: b
    :feedback_a: No, this slice starts at index 4 and goes up to and including the last item.
    :feedback_b: "cat" is at index 2 and [56, 57, "dog"] is what you get when index 4 is exclusive.
    :feedback_c: Remember that index values start at 0!

    What is printed by the following statements?

    ::

      alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
      print(alist[2:4])